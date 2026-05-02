def analyze_cv(cv_text, job_text):
    cv = cv_text.lower()
    job = job_text.lower()

    score = 50
    missing_keywords = []

    # mots clés techniques importants
    keywords = ["python", "data", "machine learning", "sql", "api", "fastapi", "ai", "docker"]

    # scoring basé sur mots présents
    for word in keywords:
        if word in cv:
            score += 5
        elif word in job:
            missing_keywords.append(word)

    # bonus si match direct CV / job
    for word in job.split():
        if word in cv:
            score += 1

    score = min(100, max(0, score))

    return {
        "score": score,
        "missing_keywords": list(set(missing_keywords))
    }