import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, Union

load_dotenv()

class LLMResponse(BaseModel):
    """Data structure to standardize LLM responses across different providers"""
    completion: str = Field(description="The text completion from the LLM")
    raw_response: Union[Dict[str, Any], Any] = Field(description="The full raw response object from the provider")
    usage: Optional[Union[Dict[str, Any], Any]] = Field(
        default={},
        description="Token usage statistics"
    )
    finish_reason: Optional[str] = Field(
        default=None,
        description="Why the LLM stopped generating (length, stop, etc.)"
    )

class BaseLLM:
    def __init__(self):
        self.llm_name = None # default model
        self.llm_provider = None
        try:
            self.api_key = os.getenv("OPENROUTER_API_KEY")
        except:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")

    def run(self, messages: list[dict]) -> LLMResponse:
        raise NotImplementedError("LLM RUN method not implemented")
    
