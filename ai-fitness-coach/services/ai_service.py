def analyze_fitness(age, weight, height, goal):

    bmi = weight / ((height / 100) ** 2)

    if goal == "Muskelaufbau":

        return f"""
💪 Muskelaufbau Analyse

📊 Dein geschätzter BMI:
{bmi:.1f}

🏋️ Trainingsfokus:
- Push Pull Legs Split
- Progressive Overload
- Fokus auf Brust, Rücken und Schultern

🍗 Ernährung:
- Hohe Proteinaufnahme
- Ca. 300 kcal Überschuss
- Viel Wasser trinken

🔥 Empfehlung:
Trainiere 4-5x pro Woche.
"""

    elif goal == "Fett verlieren":

        return f"""
🔥 Fettverlust Analyse

📊 Dein geschätzter BMI:
{bmi:.1f}

🏃 Trainingsfokus:
- Cardio + Krafttraining
- HIIT Workouts
- Core Training

🥗 Ernährung:
- Kaloriendefizit
- Weniger Zucker
- Mehr Protein

🔥 Empfehlung:
4x Training + tägliche Bewegung.
"""

    else:

        return f"""
⚡ Body Recomp Analyse

📊 Dein geschätzter BMI:
{bmi:.1f}

🏋️ Trainingsfokus:
- Krafttraining
- Ganzkörperplan
- Fokus auf Definition

🥗 Ernährung:
- Hohe Proteinaufnahme
- Ausgewogene Ernährung

🔥 Empfehlung:
3-5x Training pro Woche.
"""
