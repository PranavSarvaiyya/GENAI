from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b"
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("how AI is transforming the Healthcare system?")
print(response.content)