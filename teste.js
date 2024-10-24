function translateText(text, targetLang = "pt") {
    const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=${targetLang}&dt=t&q=${encodeURI(text)}`;

    return fetch(url)
        .then(response => response.json())
        .then(data => data[0][0][0])
        .catch(error => {
            console.error("Erro ao traduzir: ", error);
            return text; // Retorna o texto original se houver erro
        });
}

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
                translateText(data.title).then(translatedTitle => {
                    document.getElementById("result-title").innerText = translatedTitle;
                });

                translateText(data.explanation).then(translatedDescription => {
                    document.getElementById("result-description").innerText = translatedDescription;
                });

                document.getElementById("result-image").src = data.url;
            })
            .catch(error => {
                alert(error.message);
            });
    } else {
        alert("Por favor, selecione uma data válida.");
    }
});
