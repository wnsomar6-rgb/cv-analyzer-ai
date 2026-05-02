import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.analyzer import analyze_cv
import PyPDF2

st.set_page_config(page_title="CV Analyzer AI", layout="wide")

# -----------------------
# 🎨 STYLE (SaaS)
# -----------------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #111827;
    color: white;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# HEADER
# -----------------------
st.title("🧠 CV Analyzer AI")
st.caption("Analyse intelligente de CV — niveau pro")

st.divider()

# -----------------------
# LAYOUT EN COLONNES
# -----------------------
col1, col2 = st.columns(2)

cv_text = ""

with col1:
    st.subheader("📄 CV")

    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_file:
        reader = PyPDF2.PdfReader(uploaded_file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                cv_text += text

        st.success("CV chargé ✔️")

    cv_input = st.text_area("Ou colle ton CV")

    if cv_input:
        cv_text = cv_input

with col2:
    st.subheader("💼 Offre d'emploi")
    job_text = st.text_area("Colle l'offre ici")

st.divider()

# -----------------------
# ANALYSE
# -----------------------
if st.button("🚀 Analyser"):

    if cv_text and job_text:

        result = analyze_cv(cv_text, job_text)
        score = result["score"]
        missing = result["missing_keywords"]

        st.divider()

        # -----------------------
        # SCORE CARD
        # -----------------------
        st.subheader("📊 Résultat")

        colA, colB = st.columns(2)

        with colA:
            st.metric("Score", f"{score}/100")
            st.progress(score / 100)

            if score > 80:
                st.success("🔥 Excellent match")
            elif score > 60:
                st.info("👍 Bon match")
            else:
                st.warning("⚠️ À améliorer")

        with colB:
            st.markdown("### 🔎 Mots-clés manquants")

            if missing:
                for word in missing:
                    st.markdown(f"- ❌ {word}")
            else:
                st.success("Aucun mot manquant 🎉")

    else:
        st.warning("Remplis les champs")

st.divider()

# -----------------------
# FOOTER
# -----------------------
st.caption("Projet IA - Wannessi 🚀")