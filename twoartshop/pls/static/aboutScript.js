document
  .getElementById("showHiddenButton")
  .addEventListener("click", function () {
    document.getElementById("hiddenDiv").style.display = "block";
  });

const emailInput = document.getElementById("FormControlInput1");
const submitButton = document.getElementById("submitButton");

submitButton.addEventListener("click", function (event) {
  const email = emailInput.value.trim();
  if (!isValidEmail(email)) {
    alert("Please enter a valid email address.");
    event.preventDefault();
  }
});

function isValidEmail(email) {
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailPattern.test(email);
}

const imageContainer = document.getElementById("image-container");
const sliderImages = document.querySelectorAll(".slider-image");
const prevButton = document.getElementById("prevButton");
const nextButton = document.getElementById("nextButton");

let currentImageIndex = 0;

nextButton.addEventListener("click", () => {
  currentImageIndex = (currentImageIndex + 1) % sliderImages.length;
  updateSlider();
});

prevButton.addEventListener("click", () => {
  currentImageIndex =
    (currentImageIndex - 1 + sliderImages.length) % sliderImages.length;
  updateSlider();
});

function updateSlider() {
  const position = -currentImageIndex * sliderImages[0].offsetWidth;
  imageContainer.style.transform = `translateX(${position}px)`;
}
