import os

from google import genai

os.environ["GEMINI_API_KEY"] = str(os.getenv("GEMINI_API_KEY"))

client = genai.Client()

chat = client.chats.create(model="gemini-3.5-flash")
continuar = True
while(continuar):
    prompt = input("Faça uma pergunta ao chat: ")
    response = chat.send_message(prompt)
    print(response.text)
    answer = input("Quer continuar conversando com o chat? \n Digite \n 1 - Sim \n 0 - Não  ")
    continuar = answer == "1"