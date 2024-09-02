const fileInput = document.getElementById('fileInput');
const convertButton = document.getElementById('convertButton');
const output = document.getElementById('output');

convertButton.addEventListener('click', () => {
  const selectedFile = fileInput.files[0];
  
  // Replace this with your conversion logic based on the file type
  // This example just displays the filename for demonstration purposes
  const outputText = `Selected file: ${selectedFile.name}`;
  output.textContent = outputText;
});
