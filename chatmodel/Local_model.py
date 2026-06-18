from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(max_new_tokens=100, do_sample=True, temperature=0.7, repetition_penalty=1.1),
)

chat = ChatHuggingFace(llm=llm)

print("-------AI Chatbot-------")  
while True:
    prompt = input("User: ")
    if prompt == "0":
        break
    response = chat.invoke(prompt)

    print("Bot: ", response.content)