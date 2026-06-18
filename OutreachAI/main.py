from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser


class Outrach(BaseModel):
    subject: str
    body: str

parser = PydanticOutputParser(pydantic_object=Outrach)

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.4,
    top_p=0.70,
    max_completion_tokens=1000
)


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert cold email writing assistant. 
            You write highly personalized professional emails.
            {format_instructions}"""
        ),
        (
            "user",
            """
Recipient Profile:
{recipient_profile}

Sender Information:
{sender_info}

User Goal:
{goal}

Task:
Write a short professional cold email.

Rules:
- Mention something from recipient profile
- Be natural, not fake
- Keep under 150 words
- Include subject + email body
"""
        )
    ]
)

recipient_profile = input("Enter recipient profile: ")
sender_info = input("Enter  you info: ")
goal = input("Enter your goal: ")

final_prompts = prompt.invoke(
    {
        "recipient_profile":recipient_profile, 
        "sender_info":sender_info, 
        "goal":goal,
        "format_instructions": parser.get_format_instructions()
    }
)


response = model.invoke(final_prompts)
print(response.content)

parsed_output = parser.parse(response.content)

print("\n--- Cold Email Output ---")

print("Subject Line:", parsed_output.subject)

print("\n" + parsed_output.body)