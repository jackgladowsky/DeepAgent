from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from deepagent.llm.OpenRouterLLM import OpenRouterLLM
from deepagent.llm.OllamaLLM import OllamaLLM
from deepagent.llm.LMStudioLLM import LMStudioLLM
from fastapi.middleware.cors import CORSMiddleware  

app = FastAPI()

# Initialize LLM instances
openrouter_llm = OpenRouterLLM()
ollama_llm = OllamaLLM()
lmstudio_llm = LMStudioLLM()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    model: str = "google/gemini-2.0-flash-exp:free"  # default to openrouter, can be "ollama"
    provider: str = "openrouter"  # default to openrouter, can be "ollama"

class ChatResponse(BaseModel):
    completion: str

@app.post("/chat", response_model=ChatResponse)
async def chat_completion(request: ChatRequest):
    print(request.model)
    try:
        if request.provider.lower() == "openrouter":
            response = openrouter_llm.run(request.messages, request.model)
            return ChatResponse(completion=response.completion)
        elif request.provider.lower() == "ollama":
            response = ollama_llm.run(request.messages, request.model)
            return ChatResponse(completion=response.completion)
        elif request.provider.lower() == "lmstudio":
            response = lmstudio_llm.run(request.messages, request.model)
            return ChatResponse(completion=response.completion)
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported model: {request.model}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/models")
async def get_models():
    models = lmstudio_llm.get_models()
    models.extend(openrouter_llm.get_models())
    
    #return {"models": [model['label'] for model in models], "provider": [model['provider'] for model in models]}
    return {"models": models}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}