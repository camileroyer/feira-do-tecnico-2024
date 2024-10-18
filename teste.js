document.getElementById("submit").addEventListener("click", function () {
    const day = document.getElementById("day").value;
    const month = document.getElementById("month").value;
    const year = document.getElementById("year").value;

    if (day && month && year) {
        const date = `${year}-${month}-${day}`;
        const apiKey = "V7wcscMm12k2aJcrJh7oacrgKyDdmYxzt7nuASY5";
        const url = `https://api.nasa.gov/planetary/apod?api_key=${apiKey}&date=${date}`;

        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erro na requisição: ' + response.status);
                }
                return response.json();
            })
            .then(data => {
                document.getElementById("result-title").innerText = data.title;
                document.getElementById("result-description").innerText = data.explanation;
                document.getElementById("result-image").src = data.url;
            })
            .catch(error => {
                alert(error.message);
            });
    } else {
        alert("Por favor, selecione uma data válida.");
    }
});
