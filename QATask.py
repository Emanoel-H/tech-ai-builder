import os
import pandas as pd
import csv
from google import genai
from pathlib import Path

questions = ["O que é IA?",
"Quantos anos tinha Jesus quando iniciou seu ministério?",
"De qual filme o Homem Aranha pega uma referência pra salvar o Doutor Estranho em Guerra Infinita?"]

path_questions = Path.home() / "Desktop" / "perguntas.csv"
with open(path_questions, "w", encoding="utf-8") as file:
    for question in questions:
        file.write(question + "\n")

with open(path_questions, "r", encoding="utf-8") as file:
    print(file.read())

os.environ["GEMINI_API_KEY"] = str(os.getenv("GEMINI_API_KEY"))
client = genai.Client()

q_a_list = {}
q_a_list["questions"] = "answers"
for question in questions:
    response = client.models.generate_content(model="gemini-3.5-flash", contents= question)

    q_a_list[question] = response.text

path_q_a = Path.home() / "Desktop" / "Q_and_A.csv"
with open(path_q_a, "w", encoding="utf-8") as file:
    # writer = csv.writer(file)
    # writer.writerow(["question", "answer"])
    # for q, a in q_a_list.items():
    #     writer.writerow([q, a])

    for q, a in q_a_list:
        file.write(f"{q}, {a}\n")

print(pd.read_csv(path_q_a).head())