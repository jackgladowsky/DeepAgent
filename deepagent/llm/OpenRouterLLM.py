from openai import OpenAI
from .BaseLLM import BaseLLM, LLMResponse

class OpenRouterLLM(BaseLLM):
    def __init__(self):
        super().__init__()
        self.llm_provider = "openrouter"
        self.llm_name = "google/gemini-flash-1.5"
        self.client = OpenAI(api_key=self.api_key, base_url="https://openrouter.ai/api/v1",)

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