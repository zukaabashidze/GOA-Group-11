const button = document.getElementById("changeColor");

button.addEventListener("click", function() {
  document.body.style.backgroundColor = `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255})`;
});
