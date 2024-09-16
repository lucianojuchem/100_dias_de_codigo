const clockElement = document.getElementById('clock');
const startBtn = document.getElementById('startBtn');
const resetBtn = document.getElementById('resetBtn');
let timerInterval = null;

// Função para obter o horário local da máquina
function updateLocalTime() {
  const currentTime = new Date(); // Pega o horário local da máquina
  const hours = String(currentTime.getHours()).padStart(2, '0');
  const minutes = String(currentTime.getMinutes()).padStart(2, '0');
  const seconds = String(currentTime.getSeconds()).padStart(2, '0');
  clockElement.textContent = `${hours}:${minutes}:${seconds}`;
}

// Inicia o temporizador
startBtn.addEventListener('click', () => {
  if (!timerInterval) {
    timerInterval = setInterval(updateLocalTime, 1000); // Atualiza a cada segundo
  }
});

// Reseta o temporizador
resetBtn.addEventListener('click', () => {
  clearInterval(timerInterval);
  timerInterval = null;
  clockElement.textContent = '00:00:00';
});
