# 🧠 CV Analyzer AI

Application full stack qui analyse un CV et le compare à une offre d'emploi grâce à une IA simple.

---

## 🚀 Fonctionnalités

- Analyse de CV vs offre d’emploi
- Score de matching sur 100
- Détection des mots-clés manquants
- Interface web simple (Streamlit)
- API backend FastAPI

---

## 🧠 Stack technique

- Python
- FastAPI
- Streamlit
- Pydantic
- Requests

---

## 📊 Architecture

Frontend (Streamlit) → API (FastAPI) → IA (Python analyzer)

---

## ▶️ Lancer le projet

### 1. Backend
```bash
python -m uvicorn backend.main:app --reload