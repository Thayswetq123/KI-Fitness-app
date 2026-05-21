import random

def analyze_fitness(age, weight, height, goal):

    bmi = weight / ((height / 100) ** 2)

    motivational_quotes = [
        "Disziplin schlägt Motivation.",
        "Jeder Fortschritt zählt.",
        "Konstanz ist der Schlüssel.",
        "Dein zukünftiges Ich wird dir danken."
    ]

    quote = random.choice(motivational_quotes)

    if bmi < 20:
        body_type = "eher schlank"
    elif bmi < 26:
        body_type = "athletisch"
    else:
        body_type = "kräftig"

    if goal == "Muskelaufbau":

        training = """
🏋️ Trainingsplan:
- Push Pull Legs Split
- 4-5x pro Woche
- Fokus auf Progressive Overload
"""

        nutrition = """
🍗 Ernährung:
- Hohe Proteinaufnahme
- +300 kcal Überschuss
- Reis, Hähnchen, Eier, Haferflocken
"""

    elif goal == "Fett verlieren":

        training = """
🔥 Trainingsplan:
- Krafttraining + Cardio
- HIIT 2x pro Woche
- Fokus auf Kalorienverbrauch
"""

        nutrition = """
🥗 Ernährung:
- Kaloriendefizit
- Viel Protein
- Weniger Zucker & Softdrinks
"""

    else:

        training = """
⚡ Trainingsplan:
- Ganzkörpertraining
- Fokus auf Muskeldefinition
- Moderate Gewichte + Cardio
"""

        nutrition = """
🥙 Ernährung:
- Ausgewogene Ernährung
- Hohe Proteinzufuhr
- Gesunde Fette & Gemüse
"""

    return f"""
🧠 AI Fitness Analyse

📊 BMI:
{bmi:.1f}

👤 Geschätzter Körpertyp:
{body_type}

🎯 Ziel:
{goal}

{training}

{nutrition}

💡 Motivation:
{quote}
"""
