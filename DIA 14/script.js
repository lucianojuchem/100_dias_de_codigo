
const toggleButton = document.getElementById('theme-toggle');
const body = document.body;


toggleButton.addEventListener('click', function() {
    
    body.classList.toggle('dark-theme');
    
    if (body.classList.contains('dark-theme')) {
        localStorage.setItem('theme', 'dark');
    } else {
        localStorage.setItem('theme', 'light');
    }
});


window.onload = function() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        body.classList.add('dark-theme');
    }
};
