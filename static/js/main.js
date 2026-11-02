const typingElement = document.getElementById("typing");
if (typingElement) {
    const words = typingElement.dataset.words.split("|").map(word => word.trim());
    let wordIndex = 0;
    let charIndex = 0;
    let deleting = false;
    function type() {
        const currentWord = words[wordIndex];
        if (!deleting) {
            typingElement.textContent = currentWord.substring(0, charIndex + 1);
            charIndex++;
            if (charIndex === currentWord.length) {
                deleting = true;
                setTimeout(type, 1800);
                return;
            }
        }
        else {
            typingElement.textContent = currentWord.substring(0, charIndex - 1);
            charIndex--;
            if (charIndex === 0) {
                deleting = false;
                wordIndex = (wordIndex + 1) % words.length;
            }
        }
        setTimeout(type, deleting ? 50 : 100);
    }
    type();
}



document.querySelectorAll(".skill-progress").forEach(function (bar) {
    bar.style.width = bar.dataset.width + "%";
});
// Project category filtering
const filterButtons = document.querySelectorAll(".filter-btn");
const projectItems = document.querySelectorAll(".project-item");

filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
        const selectedCategory = button.dataset.filter;

        filterButtons.forEach((btn) => {
            btn.classList.remove("active", "btn-primary");
            btn.classList.add("btn-outline-primary");
        });

        button.classList.add("active", "btn-primary");
        button.classList.remove("btn-outline-primary");

        projectItems.forEach((project) => {
            const projectCategory = project.dataset.category;

            project.style.display =
                selectedCategory === "all" ||
                projectCategory === selectedCategory
                    ? ""
                    : "none";
        });
    });
});