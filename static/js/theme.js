const button = document.getElementById("theme-toggle");

// When button is clicked
button.addEventListener("click", () => {

    // Toggle dark mode
    document.body.classList.toggle("dark");

    // Check if dark mode is enabled
    if(document.body.classList.contains("dark")){

        // Save preference
        localStorage.setItem("theme", "dark");

        // Change icon
        button.textContent = "☀️";

    }else{

        // Save preference
        localStorage.setItem("theme", "light");

        // Change icon
        button.textContent = "🌙";

    }

});

// When page loads
if(localStorage.getItem("theme") === "dark"){

    document.body.classList.add("dark");

    button.textContent = "☀️";

}