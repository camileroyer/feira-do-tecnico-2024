from fastapi import FastAPI
import requests

app = FastAPI()

# Chave da API da NASA
api_key = "V7wcscMm12k2aJcrJh7oacrgKyDdmYxzt7nuASY5"


@app.get("/apod/")
def get_apod(date: str):
    """
    Rota para buscar a imagem da NASA APOD com base na data fornecida.
    O parâmetro 'date' deve estar no formato AAAA-MM-DD.
    """
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key': api_key,
        'date': date
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Verifica se 'hdurl' ou 'url' estão disponíveis
        image_url = data.get('hdurl') or data.get('url')
        title = data.get('title')
        explanation = data.get('explanation')

        if image_url:
            return {
                "title": title,
                "explanation": explanation,
                "image_url": image_url
            }
        else:
            return {"message": "Nenhuma imagem disponível para esta data."}
    else:
        return {"error": f"Erro ao obter dados da API: {response.status_code}"}
