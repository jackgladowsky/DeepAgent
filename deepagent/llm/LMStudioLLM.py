from openai import OpenAI, APIConnectionError
from .BaseLLM import BaseLLM, LLMResponse

class LMStudioLLM(BaseLLM):
    def __init__(self, base_url: str = "http://192.168.7.106:1234/v1"):
        super().__init__()
        self.base_url = base_url
        try:
            self.client = OpenAI(
                api_key="not-needed",  # LM Studio doesn't require an API key
                base_url=base_url
            )
        except Exception as e:
            raise ConnectionError(f"Failed to initialize LM Studio client: {str(e)}")

    def run(self, messages: list[dict], model: str) -> LLMResponse:
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
            )
            
            return LLMResponse(
                completion=response.choices[0].message.content,
                raw_response=response.model_dump(),
                usage=response.usage.model_dump(),
                finish_reason=response.choices[0].finish_reason
            )
        except APIConnectionError:
            raise ConnectionError(
                f"Could not connect to LM Studio server at {self.base_url}. "
                "Please make sure LM Studio is running and the server is started."
            )
        except Exception as e:
            raise RuntimeError(f"Error while calling LM Studio: {str(e)}")
        
    def get_models(self) -> list[dict]:
        try:
            response = self.client.models.list()
            return [
                {
                    "label": model.id,
                    "value": model.id,
                    "provider": "lmstudio"
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
        
