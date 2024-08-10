// Gérer la soumission du formulaire pour ajouter un livre
document.getElementById('addBookForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Récupérer les valeurs des champs
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const isbn = document.getElementById('isbn').value;
    const successMessage = document.getElementById('successMessage');

    // Simuler l'ajout du livre (cette logique serait reliée à une base de données réelle)
    if (title && author && isbn) {
        successMessage.textContent = 'Livre ajouté avec succès!';
        successMessage.style.visibility = 'visible';
    } else {
        successMessage.textContent = 'Erreur lors de l\'ajout du livre.';
        successMessage.style.visibility = 'visible';
    }
});
