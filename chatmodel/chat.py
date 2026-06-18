from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA


load_dotenv()

model = ChatNVIDIA(
    model="google/gemma-2-2b-it",
    temperature=0.9,
    top_p=0.95,
    max_completion_tokens=100
)       

response = model.invoke("write a small story on AI?")

print(response.content)