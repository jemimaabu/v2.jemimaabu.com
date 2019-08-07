const root = document.documentElement;
root.classList.add("dark");
var themeToggle = document.getElementById("theme-toggle");

themeToggle.addEventListener("click", function() {
  root.classList.toggle("light");
  root.classList.toggle("dark");
});

themeToggle.addEventListener("keypress", function(event) {
    var keycode = event.keyCode ? event.keyCode : event.which;
    if (keycode == 13) {
      themeToggle.checked ? themeToggle.checked = false : themeToggle.checked = true
      root.classList.toggle("light");
      root.classList.toggle("dark");
    }
  });
