import json
import os
from pathlib import Path

import openai
import requests

openai.organization = os.getenv("OPENAI_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.Model.list()


URL = "https://api.openai.com/v1/chat/completions"


def ask_gpt(prompt, model, n_calls, save_path_base_filename):
    """make a request to the openai api with a prompt for a given model

    Args:
        prompt (str): prompt to pass to chatgpt
        model (str): "gpt-3.5-turbo" or "gpt-4"
            ref for latest options: https://platform.openai.com/docs/models/gpt-4
        n_calls (int): number of times to call the openai api
        save_path_base_filename (str): where to save the output
    """

    payload = {
    "model": model,
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

    model = "gpt-3.5-turbo"
    prompt = "Write 10 haikus about cats"
    n_calls = 10
    base_filename = "cat_haikus_10"
    save_path = "./data/gpt_generated/cat_haikus"

    Path(save_path).mkdir(parents=True, exist_ok=True)

    save_path_base_filename = f"{save_path}/{base_filename}"
    print(save_path_base_filename)

    ask_gpt(prompt, n_calls, save_path_base_filename)