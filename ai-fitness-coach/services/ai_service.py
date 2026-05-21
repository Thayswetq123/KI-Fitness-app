import requests
import os

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
}

def analyze_fitness(age, weight, height, goal):

    prompt = f"""
Du bist ein professioneller Fitness Coach.

Person:
- Alter: {age}
- Gewicht: {weight} kg
- Größe: {height} cm
- Ziel: {goal}

Erstelle:

1. Körperanalyse
2. Trainingsplan
3. Ernährung
4. Kalorien Empfehlung
5. Fokus Muskelgruppen

Antworte motivierend und modern.
"""

    payload = {
        "inputs": prompt
    }

    try:

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload
        )

        data = response.json()

        return data[0]["generated_text"]

    except Exception as e:
        return f"Fehler: {str(e)}"
