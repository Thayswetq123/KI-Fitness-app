import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_fitness(age, weight, height, goal):

    prompt = f"""
Du bist ein Fitness Coach.

Daten:
- Alter: {age}
- Gewicht: {weight}
- Größe: {height}
- Ziel: {goal}

Erstelle:
1. Körperanalyse
2. Trainingsplan
3. Ernährungsplan
4. Fokus-Muskeln
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
