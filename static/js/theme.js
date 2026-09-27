const button = document.getElementById("theme-toggle");

const savedTheme = localStorage.getItem("theme");

function setTheme(theme) {
    const isDark = theme === "dark";
    document.body.classList.toggle("dark-mode", isDark);
    document.body.dataset.theme = isDark ? "dark" : "light";
    localStorage.setItem("theme", isDark ? "dark" : "light");

    if (button) {
        button.textContent = isDark ? "☀️" : "🌙";
        button.setAttribute("aria-label", isDark ? "Use light theme" : "Use dark theme");
    }
}

setTheme(savedTheme === "dark" ? "dark" : "light");

if (button) {
    button.addEventListener("click", () => {
        setTheme(document.body.classList.contains("dark-mode") ? "light" : "dark");
    });
}