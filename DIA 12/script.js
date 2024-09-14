// Obtém o card pelo ID e adiciona o evento de clique
document.getElementById('card').addEventListener('click', function () {
    // Alterna a classe 'flipped' para o card
    this.classList.toggle('flipped');
});
