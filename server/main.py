from fastapi import FastAPI
from pydantic import BaseModel
from agent_service import agent

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "response": agent(req.message)
    }