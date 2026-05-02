from fastapi import FastAPI
from pydantic import BaseModel
from backend.analyzer import analyze_cv

app = FastAPI()

# -----------------------
# 📦 MODEL DONNÉES
# -----------------------
class CVRequest(BaseModel):
    cv_text: str
    job_text: str


# -----------------------
# 🚀 ROUTE PRINCIPALE
# -----------------------
@app.post("/analyze")
def analyze(data: CVRequest):

    result = analyze_cv(data.cv_text, data.job_text)

    return {
        "message": "Analyse terminée",
        "score": result["score"],
        "missing_keywords": result["missing_keywords"]
    }


# -----------------------
# TEST API
# -----------------------
@app.get("/")
def home():
    return {"status": "CV Analyzer API running 🚀"}