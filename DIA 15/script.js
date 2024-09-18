// Seleciona o textarea e o span onde o contador será atualizado
const textInput = document.getElementById('text-input');
const charCount = document.getElementById('char-count');

// Adiciona um evento para detectar mudanças no texto
textInput.addEventListener('input', function() {
    // Remove os espaços e conta os caracteres restantes
    const textWithoutSpaces = textInput.value.replace(/\s+/g, '');
    charCount.textContent = textWithoutSpaces.length;
});
