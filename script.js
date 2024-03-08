// script.js

// Function to read a random line from a file
function getRandomLine() {
    fetch('/get-random-line') // Endpoint for server-side logic (defined in Python)
        .then(response => response.text())
        .then(data => {
            const randomLine = data;

            // Display the random line on the webpage
            document.getElementById('randomLine').textContent = randomLine;
        })
        .catch(error => console.error('Error fetching random line:', error));
}
