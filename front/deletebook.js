// Gérer la soumission du formulaire pour supprimer un livre
document.getElementById('deleteBookForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Récupérer les valeurs des champs
    const isbn = document.getElementById('isbn').value;
    const successMessage = document.getElementById('successMessage');

    // Simuler la suppression du livre (cette logique serait reliée à une base de données réelle)
    if (isbn) {
        successMessage.textContent = 'Livre supprimé avec succès!';
        successMessage.style.visibility = 'visible';
    } else {
        successMessage.textContent = 'Erreur lors de la suppression du livre.';
        successMessage.style.visibility = 'visible';
    }
});