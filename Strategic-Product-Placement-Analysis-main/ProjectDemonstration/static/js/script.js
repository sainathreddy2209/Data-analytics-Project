document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector(".contact-form");
    form.addEventListener("submit", function() {
        alert("Message sent successfully! 📩");
    });
});
