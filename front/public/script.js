const API_BASE_URL = 'http://localhost:5000'; // Change this to your API base URL

// Function to handle login
document.getElementById('loginForm')?.addEventListener('submit', async (event) => {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    const response = await fetch(`${API_BASE_URL}/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
    });
    const result = await response.json();
    document.getElementById('loginMessage').innerText = result.message;
});

// Function to handle signup
document.getElementById('signupForm')?.addEventListener('submit', async (event) => {
    event.preventDefault();
    const username = document.getElementById('signupUsername').value;
    const password = document.getElementById('signupPassword').value;

    const response = await fetch(`${API_BASE_URL}/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
    });
    const result = await response.json();
    document.getElementById('signupMessage').innerText = result.message;
});

// Function to handle adding a book
document.getElementById('addBookForm')?.addEventListener('submit', async (event) => {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const isbn = document.getElementById('isbn').value;

    const response = await fetch(`${API_BASE_URL}/books/add`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, author, isbn }),
    });
    const result = await response.json();
    document.getElementById('addBookMessage').innerText = result.message;
});

// Function to handle modifying a book
document.getElementById('modifyBookForm')?.addEventListener('submit', async (event) => {
    event.preventDefault();
    const id = document.getElementById('bookId').value;
    const title = document.getElementById('newTitle').value;
    const author = document.getElementById('newAuthor').value;
    const isbn = document.getElementById('newIsbn').value;

    const response = await fetch(`${API_BASE_URL}/books/modify/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, author, isbn }),
    });
    const result = await response.json();
    document.getElementById('modifyBookMessage').innerText = result.message;
});

// Function to handle deleting a book
document.getElementById('deleteBookForm')?.addEventListener('submit', async (event) => {
    event.preventDefault();
    const id = document.getElementById('bookId').value;

    const response = await fetch(`${API_BASE_URL}/books/delete/${id}`, {
        method: 'DELETE',
    });
    const result = await response.json();
    document.getElementById('deleteBookMessage').innerText = result.message;
});

// Function to handle searching for a book
document.getElementById('searchBookForm')?.addEventListener('submit', async (event) => {
    event.preventDefault();
    const title = document.getElementById('searchTitle').value;

    const response = await fetch(`${API_BASE_URL}/books/search?title=${title}`);
    const result = await response.json();
    
    const resultsList = document.getElementById('bookResults');
    resultsList.innerHTML = '';
    if (Array.isArray(result) && result.length) {
        result.forEach(book => {
            const listItem = document.createElement('li');
            listItem.innerHTML = `<strong>Titre:</strong> ${book.title} <br /><strong>Auteur:</strong> ${book.author} <br /><strong>ISBN:</strong> ${book.isbn}`;
            resultsList.appendChild(listItem);
        });
    } else {
        document.getElementById('searchBookMessage').innerText = result.message || 'Aucun livre trouvé';
    }
});
