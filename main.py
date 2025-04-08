import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in environment variables. Please set it in your .env file.")

url = "https://api.deepseek.com/v1/chat/completions"

headers = {
    "Autorization" : f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
data = {
    "model" : "deepseek-chat",
    "messages": [
        {
            "role": "user", "content": "Hola, ¿puedes explicarme cómo usar la API de DeepSeek?"
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code,response.text)