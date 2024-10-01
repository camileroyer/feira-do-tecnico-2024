import requests
import webbrowser

# Definindo a chave da API da NASA (substitua pela sua se necessário)
api_key = "V7wcscMm12k2aJcrJh7oacrgKyDdmYxzt7nuASY5"

# Solicitar que o usuário insira uma data no formato YYYY-MM-DD
date = input("Digite a data (no formato AAAA-MM-DD) para ver a foto: ")

# URL da API APOD (Astronomy Picture of the Day)
url = "https://api.nasa.gov/planetary/apod"

# Parâmetros que serão enviados para a API, incluindo a data selecionada
params = {'api_key': api_key, 'date': date}

# Fazendo a requisição para a API da NASA
response = requests.get(url, params=params)

# Verificando se a requisição foi bem-sucedida (status code 200)
if response.status_code == 200:
    # Convertendo a resposta em JSON
    data = response.json()
    # Extraindo informações da resposta
    image_url = data.get('url')  # URL da imagem ou vídeo
    title = data.get('title')  # Título da imagem
    explanation = data.get('explanation')  # Descrição da imagem
    # Exibindo o título e a descrição da imagem
    print(f"\nTítulo: {title}")
    print(f"Descrição: {explanation}")
    # Verificando se a URL da imagem é de um vídeo ou imagem
    if image_url and "youtube.com" in image_url:
        print("\nA imagem do dia é um vídeo. Abrindo no navegador...")
        webbrowser.open(image_url)
    elif image_url:
        print("\nAbrindo a imagem no navegador...")
        webbrowser.open(image_url)
    else:
        print("Nenhuma imagem ou vídeo disponível.")
else:
    # Caso ocorra algum erro na requisição, exibe o status code
    print("Erro ao obter a imagem:", response.status_code)