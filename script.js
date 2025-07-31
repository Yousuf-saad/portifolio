const texts = ["a Full-Stack Developer.", "a Problem-Solver.", "an AI Enthusiast."];
let currentIndex = 0;
let charIndex = 0;
let isDeleting = false;
function typeEffect() {
    const display = document.querySelector(".typing-text");
    if (!display) return;
    const currentText = texts[currentIndex];
    let updatedText = isDeleting ? currentText.substring(0, charIndex--) : currentText.substring(0, charIndex++);
    display.textContent = updatedText;
    //adjust speed
    let speed = isDeleting ? 60 : 100;
    if (!isDeleting && updatedText === currentText) {
        speed = 1200;
        isDeleting = true;
    }
    else if (isDeleting && updatedText === "") {
        isDeleting = false;
        currentIndex = (currentIndex + 1) % texts.length;
        speed=1500;
    }
    setTimeout(typeEffect,speed)
}

typeEffect();

document.getElementById('contact-form').addEventListener("submit", function (e) {
    e.preventDefault();
    alert("Thank you for your message,Yousuf will resppond soon!")
});