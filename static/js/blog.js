const root = document.documentElement;
root.classList.add('dark');

document.getElementById('theme-toggle').addEventListener('click', function() {
  root.classList.toggle('light');
  root.classList.toggle('dark')
});