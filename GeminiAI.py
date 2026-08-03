import os

from google import genai

os.environ["GEMINI_API_KEY"] = str(os.getenv("GEMINI_API_KEY"))

client = genai.Client()

response = client.models.generate_content(model="gemini-3.5-flash", contents= "O que é a Inteligência Artificial?")

print(response.text)

