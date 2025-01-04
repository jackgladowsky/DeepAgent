from openai import OpenAI, APIConnectionError
from .BaseLLM import BaseLLM, LLMResponse

class OpenRouterLLM(BaseLLM):
    def __init__(self):
        super().__init__()
        self.client = OpenAI(api_key=self.api_key, base_url="https://openrouter.ai/api/v1",)

    def run(self, messages: list[dict], model: str) -> LLMResponse:
        response = self.client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "none",
                "X-Title": "DeepAgent",
            },
            model=model,
            messages=messages,
        )
        
        # Convert response and usage to dictionaries
        return LLMResponse(
            completion=response.choices[0].message.content,
            raw_response=response.model_dump(),  # Convert to dict
            usage=response.usage.model_dump(),   # Convert to dict
            finish_reason=response.choices[0].finish_reason
        )
    
    def get_models(self) -> list[dict]:
        try:
            response = self.client.models.list()
            return [
                {
                    "label": model.id,
                    "value": model.id,
                    "provider": "openrouter"
                }
                for model in response.data
            ]
        except APIConnectionError:
            raise ConnectionError(
                f"Could not connect to LM Studio server at {self.base_url}. "
                "Please make sure LM Studio is running and the server is started."
            )
        except Exception as e:
            raise RuntimeError(f"Error while fetching models from LM Studio: {str(e)}")