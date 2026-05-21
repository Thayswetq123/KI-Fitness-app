from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def analyze_fitness(age, weight, height, goal):

    prompt = f"""
Du bist ein Fitness Coach.

Alter: {age}
Gewicht: {weight}
Größe: {height}
Ziel: {goal}

Erstelle:
- Körperanalyse
- Trainingsplan
- Ernährung
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
