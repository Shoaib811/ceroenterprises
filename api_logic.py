import json

def get_questions(role):
    with open("data/questions.json", "r") as f:
        questions_data = json.load(f)
    return questions_data.get(role, [])

def analyze_answers(data):
    role = data.get("role", "")
    responses = data.get("responses", [])
    # Mock scoring
    score = sum(30 for r in responses if len(r.strip()) > 30)
    traits = ["Creative", "Detail Oriented"] if score > 50 else ["Needs Clarity"]
    explanation = "Strong articulation and professional tone." if score > 50 else "Responses lacked sufficient detail."
    return {
        "score": score,
        "traits": traits,
        "explanation": explanation
    }
