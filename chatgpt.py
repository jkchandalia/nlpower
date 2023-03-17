import os
import json
from pathlib import Path

import requests

import openai

openai.organization = "org-pyHC73IrTntMeKFF1ogHPSb4"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()


URL = "https://api.openai.com/v1/chat/completions"


def ask_gpt(prompt, n_calls, save_path_base_filename):

    payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": prompt}],
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

    for n in range(n_calls):

        save_path_filename = f"{save_path_base_filename}_{n}.json"

        response = requests.post(URL, headers=headers, json=payload, stream=False)

        print(response.content)

        with open(save_path_filename, "w+") as f:
            json.dump(response.json(), f)

if __name__ == "__main__":

    prompt = "Write 10 haikus about cats"
    n_calls = 10
    base_filename = "cat_haikus_10"
    save_path = "./data/gpt_generated/cat_haikus"
    Path(save_path).mkdir(parents=True, exist_ok=True)

    save_path_base_filename = f"{save_path}/{base_filename}"
    print(save_path_base_filename)

    ask_gpt(prompt, n_calls, save_path_base_filename)