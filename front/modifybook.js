// Gérer la soumission du formulaire pour modifier un livre
document.getElementById('modifyBookForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Récupérer les valeurs des champs
    const isbn = document.getElementById('isbn').value;
    const newTitle = document.getElementById('newTitle').value;
    const newAuthor = document.getElementById('newAuthor').value;
    const successMessage = document.getElementById('successMessage');

    // Simuler la modification du livre (cette logique serait reliée à une base de données réelle)
    if (isbn && (
