import streamlit as st
import requests
from backend.analyzer import analyze_cv

st.set_page_config(page_title="CV Analyzer AI", layout="wide")

st.title("🧠 CV Analyzer AI")
st.write("Analyse ton CV par rapport à une offre d'emploi")

# -----------------------
# INPUTS
# -----------------------
cv_text = st.text_area("📄 Ton CV")
job_text = st.text_area("💼 Offre d'emploi")

# -----------------------
# BUTTON
# -----------------------
if st.button("Analyser mon CV"):
    if cv_text and job_text:

        result = analyze_cv(cv_text, job_text)

        st.success("Analyse terminée ✔️")

        st.metric("Score CV", f"{result['score']}/100")

        st.subheader("🔎 Mots-clés manquants")
        st.write(result["missing_keywords"])

    else:
        st.warning("Remplis les deux champs")