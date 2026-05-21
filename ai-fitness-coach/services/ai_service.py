import requests
import os

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

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
4. Kalorien
5. Fokus Muskelgruppen

Antworte modern und motivierend.
"""

    payload = {
        "inputs": prompt
    }

    try:

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        data = response.json()

        if isinstance(data, list):
            return data[0]["generated_text"]

        return str(data)

    except Exception as e:
        return f"Fehler: {str(e)}"
