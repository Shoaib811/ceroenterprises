from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from api_logic import analyze_answers, get_questions

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-questions")
def read_questions(role: str):
    return get_questions(role)

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    return analyze_answers(data)
