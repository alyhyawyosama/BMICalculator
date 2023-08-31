


function isValidValue(val) {
  return !isNaN(val) && parseFloat(val) > 0;
}


function calculateBMI(weight, height) {
  if (!isValidValue(weight) || !isValidValue(height)) {
    return false;
  }


  height = parseFloat(height) / 100;
  weight = parseFloat(weight);
  return weight / (height * height);
}


function interpretBMI(val) {
  if (val < 18.5) {
    return "Underweight";
  } else if (val >= 18.5 && val < 25) {
    return "Normal weight";
  } else if (val >= 25 && val < 30) {
    return "Overweight";
  } else if (val >= 30) {
    return "Obese";
  }
}


document.addEventListener("DOMContentLoaded", function() {
  var weightInput = document.getElementById("weight-input");
  var heightInput = document.getElementById("height-input");
  var calculateButton = document.getElementById("calculate-button");
  var resultContainer = document.getElementById("result-container");

  calculateButton.addEventListener("click", function() {
    var weight = weightInput.value;
    var height = heightInput.value;
    var bmi = calculateBMI(weight, height);
    if (bmi === false) {
      resultContainer.textContent = "Invalid input. Try again.";
      return;
    }
    var interpretation = interpretBMI(bmi);
    resultContainer.textContent = "BMI: " + bmi + " - " + interpretation;
  });
});