from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.orchestrator import run_mentor_ai

app = FastAPI(title="MENTOR.AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "MENTOR.AI backend running"}

@app.get("/mentor")
def mentor(query: str):
    response = run_mentor_ai(query)
    return {"response": response}
