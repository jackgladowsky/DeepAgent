from llm.OpenRouterLLM import OpenRouterLLM

llm = OpenRouterLLM()

response = llm.run([{"role": "user", "content": "Hello! How are you?"}])
print(response.completion)