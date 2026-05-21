import streamlit as st
from dotenv import load_dotenv
from services.ai_service import analyze_fitness

load_dotenv()

st.set_page_config(page_title="AI Fitness Coach", layout="centered")

st.title("💪 AI Fitness Coach")

st.write("Erhalte kostenlose KI Trainings- & Ernährungstipps")

age = st.number_input("Alter", 16, 100, 25)
weight = st.number_input("Gewicht (kg)", 40, 200, 80)
height = st.number_input("Größe (cm)", 140, 220, 180)

goal = st.selectbox(
    "Ziel",
    [
        "Muskelaufbau",
        "Fett verlieren",
        "Body Recomp"
    ]
)

image = st.file_uploader(
    "Körperbild hochladen",
    type=["png", "jpg", "jpeg"]
)

if st.button("Analyse starten 🚀"):

    with st.spinner("KI analysiert deinen Körper..."):

        result = analyze_fitness(
            age,
            weight,
            height,
            goal
        )

        st.markdown("## 🧠 Deine Analyse")

        st.write(result)
