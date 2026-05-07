import streamlit as st
from dotenv import load_dotenv
import os
from services.ai_service import analyze_fitness

load_dotenv()

st.set_page_config(page_title="AI Fitness Coach", layout="centered")

st.title("💪 AI Fitness Coach")

st.write("Gib deine Daten ein und erhalte deinen KI Trainingsplan")

age = st.number_input("Alter", 16, 100, 25)
weight = st.number_input("Gewicht (kg)", 40, 200, 80)
height = st.number_input("Größe (cm)", 140, 220, 180)

goal = st.selectbox("Ziel", ["Muskelaufbau", "Fett verlieren", "Body Recomp"])

image = st.file_uploader("Körperbild hochladen", type=["png", "jpg", "jpeg"])

if st.button("Analyse starten 🚀"):
    if image:
        st.image(image)

        result = analyze_fitness(age, weight, height, goal)

        st.markdown("## 🧠 Ergebnis")
        st.write(result)
    else:
        st.warning("Bitte Bild hochladen")
