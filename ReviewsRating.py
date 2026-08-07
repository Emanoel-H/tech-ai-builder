import os
import pandas as pd
import time
from google import genai
from pathlib import Path

os.environ["GEMINI_API_KEY"] = str(os.getenv("GEMINI_API_KEY"))
client = genai.Client()

path_reviews = Path.home() / "Desktop" / "reviews.csv"
df_reviews = pd.read_csv(path_reviews)

df_reviews_text = df_reviews["reviewText"]

ratings = []
i = 0
while i < len(df_reviews_text):
    response = client.models.generate_content(model="gemini-3.5-flash-lite",
                                              contents="Classifique o sentimento desse feedback (Negativo, Positivo, Neutro), em uma única palavra: " + df_reviews_text.iloc[i])

    ratings.append(response.text)
    i = i + 1
    time.sleep(4)

df_reviews["Ratings"] = ratings

print(df_reviews.loc[df_reviews_text.index, ["Ratings", "reviewText"]])
