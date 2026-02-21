from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent_service import agent

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # או ["*"] בזמן פיתוח
    allow_methods=["*"],
    allow_headers=["*"],
)

# מודל הבקשה
class ChatRequest(BaseModel):
    message: str

# Route
@app.post("/chat")
def chat(req: ChatRequest):
    return {"response": agent(req.message)}