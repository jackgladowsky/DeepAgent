from llm.OpenRouterLLM import OpenRouterLLM
from llm.OllamaLLM import OllamaLLM
from llm.LMStudioLLM import LMStudioLLM

llm1 = OpenRouterLLM()

response1 = llm1.run([{"role": "user", "content": "Hello! How are you?"}])
print(f"OpenRouterLLM: {response1.completion}")

llm2 = LMStudioLLM()

response2 = llm2.run([{"role": "user", "content": "Hello! How are you?"}])
print(f"LMStudioLLM: {response2.completion}")

# llm2 = OllamaLLM()

# response2 = llm2.run([{"role": "user", "content": "Hello! How are you?"}])
# print(f"OllamaLLM: {response2.completion}")

# response2_ollama = llm2.run_ollama([{"role": "user", "content": "Hello! How are you?"}])
# print(f"OllamaLLM: {response2_ollama.message.content}")
