
function getRandomLine() {
    fetch('/get-random-line') 
        .then(response => response.text())
        .then(data => {
            const randomLine = data;

            document.getElementById('randomLine').textContent = randomLine;
        })
        .catch(error => console.error('Error fetching random line:', error));
}
