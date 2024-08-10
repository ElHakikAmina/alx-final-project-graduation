document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('errorMessage');

    // Simple validation for demonstration
    if (email === 'admin@example.com' && password === 'password') {
        alert('Connexion réussie!');
        errorMessage.style.visibility = 'hidden';
        // Redirect to another page or perform any further actions
    } else {
        errorMessage.textContent = 'Adresse e-mail ou mot de passe incorrect';
        errorMessage.style.visibility = 'visible';
    }
});
