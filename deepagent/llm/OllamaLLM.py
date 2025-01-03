from openai import OpenAI
from ollama import chat, ChatResponse
from .BaseLLM import BaseLLM, LLMResponse

class OllamaLLM(BaseLLM):
    def __init__(self):
        super().__init__()
        self.llm_provider = "ollama"
        self.llm_name = "qwen2.5:14b"  # default model, can be changed
        self.client = OpenAI(api_key='ollama', base_url="http://localhost:11434/v1",)

    def run(self, messages: list[dict]) -> LLMResponse:
        response = self.client.chat.completions.create(
            model=self.llm_name,
            messages=messages,
        )
        
        # Convert response and usage to dictionaries
        return LLMResponse(
            completion=response.choices[0].message.content,
            raw_response=response.model_dump(),  # Convert to dict
            usage=response.usage.model_dump(),   # Convert to dict
            finish_reason=response.choices[0].finish_reason
        )
    
    def run_ollama(self, messages: list[dict]) -> ChatResponse:
        response = chat(model=self.llm_name, messages=messages)
        return response
