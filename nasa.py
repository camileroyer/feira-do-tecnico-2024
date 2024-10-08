import requests
import webbrowser

# Chave da API
api_key = "V7wcscMm12k2aJcrJh7oacrgKyDdmYxzt7nuASY5"

# Solicita ao usuário para inserir a data
date = input("Digite a data no formato AAAA-MM-DD para ver a foto do dia: ")

# URL da API
url = "https://api.nasa.gov/planetary/apod"

# Parâmetros da requisição
params = {
    'api_key': api_key,
    'date': date
}

# Faz a requisição à API
response = requests.get(url, params=params)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()

    # Verifica se 'hdurl' ou 'url' estão disponíveis
    image_url = data.get('hdurl') or data.get('url')
    title = data.get('title')
    explanation = data.get('explanation')

    if image_url:
        print(f"Título: {title}")
        print(f"Descrição: {explanation}\n")
        print(f"URL da imagem: {image_url}")

        # Abre a imagem no navegador
        webbrowser.open(image_url)
    else:
        print("Nenhuma imagem disponível para esta data.")
else:
    print(f"Erro ao obter a foto do dia: {response.status_code}")
