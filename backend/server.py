from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from deepagent.llm.OpenRouterLLM import OpenRouterLLM
from deepagent.llm.OllamaLLM import OllamaLLM
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Initialize LLM instances
openrouter_llm = OpenRouterLLM()
ollama_llm = OllamaLLM()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    model: str = "openrouter"  # default to openrouter, can be "ollama"

class ChatResponse(BaseModel):
    completion: str

@app.post("/chat", response_model=ChatResponse)
async def chat_completion(request: ChatRequest):
    try:
        if request.model.lower() == "openrouter":
            response = openrouter_llm.run(request.messages)
            return ChatResponse(completion=response.completion)
        elif request.model.lower() == "ollama":
            response = ollama_llm.run(request.messages)
            return ChatResponse(completion=response.completion)
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported model: {request.model}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}