// document.getElementById("Register").addEventListener("click", function () {
//   const userInput = prompt("Enter your age:");
//   if (userInput > 13) {
//     alert("You can use our store.");
//   } else {
//     alert("You are too young to use our store.");
//   }
// });

document.getElementById("Register").onmouseover = function () {
  document.getElementById("Register").style.fontSize = "200%";
};

document.getElementById("Register").onmouseout = function () {
  document.getElementById("Register").style.fontSize = "125%";
};

document.getElementById("Login").onmouseover = function () {
  document.getElementById("Login").style.fontSize = "200%";
};

document.getElementById("Login").onmouseout = function () {
  document.getElementById("Login").style.fontSize = "125%";
};
