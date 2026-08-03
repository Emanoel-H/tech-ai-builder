import os

from google import genai

os.environ["GEMINI_API_KEY"] = str(os.getenv("GEMINI_API_KEY"))

client = genai.Client()

chat = client.chats.create(model="gemini-3.5-flash")

response = chat.send_message("Com poucas palavras, escreva para Rhaissa Melo o quanto eu sinto por ela")

print(response.text)