$(function () {
  $(".workers__profile").slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    prevArrow: false,
    nextArrow: $(".workers__slider_right"),
  });
});

function toggleAnswer(id) {
  var answer = document.getElementById(id);
  if (answer.style.display === "none") {
    answer.style.display = "block";
  } else {
    answer.style.display = "none";
  }
}
const textInput = document.getElementById("text-input");

function getText() {
  const text = textInput.value;
  console.log(text);
}

button.addEventListener("click", getText);
