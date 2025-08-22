// Typing effect (already in your script)
const typingText = document.querySelector('.typing-text');

const phrases = [
  "Software Developer & IT Professional",
  "Passionate Coder",
  "Open Source Enthusiast",
  "Web & Backend Developer"
];

let currentPhraseIndex = 0;
let currentCharIndex = 0;
let isDeleting = false;
let typingSpeed = 120;

function type() {
  const currentPhrase = phrases[currentPhraseIndex];
  
  if (!isDeleting) {
    typingText.textContent = currentPhrase.slice(0, currentCharIndex + 1);
    currentCharIndex++;

    if (currentCharIndex === currentPhrase.length) {
      isDeleting = true;
      typingSpeed = 1500;
    } else {
      typingSpeed = 120;
    }
  } else {
    typingText.textContent = currentPhrase.slice(0, currentCharIndex - 1);
    currentCharIndex--;

    if (currentCharIndex === 0) {
      isDeleting = false;
      currentPhraseIndex = (currentPhraseIndex + 1) % phrases.length;
      typingSpeed = 500;
    } else {
      typingSpeed = 80;
    }
  }

  setTimeout(type, typingSpeed);
}

document.addEventListener('DOMContentLoaded', () => {
  if (typingText) type();
});

// Scroll animations
const sections = document.querySelectorAll('.fade-in-section');
const cards = document.querySelectorAll('.card');

const observer = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.2 }
);

sections.forEach(section => observer.observe(section));
cards.forEach(card => observer.observe(card));

