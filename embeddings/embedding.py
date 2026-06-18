from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = NVIDIAEmbeddings(
    model="nvidia/nv-embed-v1"
)

text = [
    "What is the capital of india?",
    "What is the currency of india?",
    "What is the population of india?",
    "What is the largest city in india?",
    "What is the smallest city in india?"
]

vector = embeddings.embed_documents(text)

print(vector)


