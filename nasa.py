import webbrowser
import requests
import json
from fastapi import FastAPI
import requests, os

api_key = 'API_KEY'
api_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/'

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

API_KEY='V7wcscMm12k2aJcrJh7oacrgKyDdmYxzt7nuASY5'


url= 'https://api.nasa.gov/planetary/apod'

params={
    'api_key':API_KEY,
    'hd':'true',
    'date': '1995-09-17'
}

response = requests.get(url,params=params)
json_data = json.loads(response.text)
image_url = json_data['hdurl']
webbrowser.open(image_url)