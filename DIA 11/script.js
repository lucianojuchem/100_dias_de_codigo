document.getElementById('changeStyleBtn').addEventListener('click', function () {
    const myDiv = document.getElementById('myDiv');

    // Alterna entre adicionar ou remover a classe 'changed'
    myDiv.classList.toggle('changed');
});
