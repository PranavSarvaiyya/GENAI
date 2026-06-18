
from dotenv import load_dotenv
load_dotenv(override=True)
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


model = ChatNVIDIA(
    model="google/gemma-2-2b-it",
    temperature=0.3,
    top_p=0.70,
    max_completion_tokens=1000
)  

message = [
]


print("-------AI Chatbot-------")  
while True:
    prompt = input("User: ")
    if prompt == "0":
        break
    message.append(HumanMessage(content=prompt))
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("Bot: ",response.content)

print(message)