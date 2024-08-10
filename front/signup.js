// Gérer la soumission du formulaire d'inscription
document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Récupérer les valeurs des champs
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('errorMessage');

    // Validation simple pour la démonstration
    if (name && email && password) {
        alert('Inscription réussie!');
        errorMessage.style.visibility = 'hidden';
        // Rediriger vers une autre page ou effectuer d'autres actions
    } else {
        errorMessage.textContent = 'Veuillez remplir tous les champs';
        errorMessage.style.visibility = 'visible';
    }
});
