// JavaScript for changing background images in the Hero section
const hero = document.querySelector('.hero');
const backgrounds = [
  'url("aff.jpg")',
  'url("bff.jpg")',
  'url("cff.jpg")',
  'url("dff.jpg")'
];

let currentImageIndex = 0;

function changeBackground() {
  // Update the background image
  hero.style.backgroundImage = backgrounds[currentImageIndex];
  hero.style.transition = "background-image 1s ease-in-out";

  // Increment the index, reset if it exceeds the array length
  currentImageIndex = (currentImageIndex + 1) % backgrounds.length;
}

// Change the background every 5 seconds
setInterval(changeBackground, 3000)