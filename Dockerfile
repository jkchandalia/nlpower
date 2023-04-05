FROM python:3.8-slim-buster

RUN pip install openai

COPY . /mnt/nlp/

WORKDIR /mnt/nlp/

# CMD python hello.py
# CMD python chatgpt.py