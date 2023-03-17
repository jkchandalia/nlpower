import os
import json

import requests

import openai

openai.organization = "org-pyHC73IrTntMeKFF1ogHPSb4"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()


URL = "https://api.openai.com/v1/chat/completions"

payload = {
"model": "gpt-3.5-turbo",
"messages": [{"role": "user", "content": f"Write 10 haikus about cats"}],
"temperature" : 1.0,
"top_p":1.0,
"n" : 1,
"stream": False,
"presence_penalty":0,
"frequency_penalty":0,
}

headers = {
"Content-Type": "application/json",
"Authorization": f"Bearer {openai.api_key}"
}

response = requests.post(URL, headers=headers, json=payload, stream=False)

print(response.content)

with open("haikus_10.json", "w+") as f:
    json.dump(response.json(), f)