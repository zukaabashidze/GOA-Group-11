const num1 = document.getElementById("num1");
const num2 = document.getElementById("num2");
const resultElement = document.getElementById("result");

document.getElementById("calcForm").addEventListener("submit", function (event) {
    event.preventDefault(); 
    sumOfNum();
});

function sumOfNum() {
    const sum = parseFloat(num1.value) + parseFloat(num2.value);
    console.log(sum);


    resultElement.textContent = '${sum}.;'
}