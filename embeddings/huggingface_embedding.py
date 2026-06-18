from langchain_huggingface import HuggingFaceEmbeddings



embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = [
    "What is the capital of india?",
    "What is the currency of india?"
]

vector = embeddings.embed_documents(text)
print(vector)