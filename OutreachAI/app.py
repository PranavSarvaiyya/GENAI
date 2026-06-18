from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from pydantic import BaseModel
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from st_copy_to_clipboard import st_copy_to_clipboard

# ==========================
# Pydantic Schema
# ==========================

class Outreach(BaseModel):
    subject: str
    body: str


parser = PydanticOutputParser(
    pydantic_object=Outreach
)

# ==========================
# Model
# ==========================

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.4,
    top_p=0.70,
    max_completion_tokens=1000
)

# ==========================
# Prompt
# ==========================

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert cold email writing assistant.

You write highly personalized professional emails.

{format_instructions}
"""
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

# ==========================
# Page Config
# ==========================

st.set_page_config(
    page_title="AI Cold Email Generator",
    page_icon="📧",
    layout="wide"
)

# ==========================
# Custom CSS
# ==========================

st.markdown("""
<style>

.block-container{
    padding-top: 1.5rem;
    padding-bottom: 1rem;
}

.email-card{
    background-color:#0E1117;
    border:1px solid #31333F;
    border-radius:12px;
    padding:18px;
    margin-top:10px;
    white-space:pre-wrap;
    font-family:monospace;
}

.small-label{
    font-size:14px;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# Header
# ==========================

st.title("📧 AI Cold Email Generator")
st.caption("Generate personalized cold emails using Mistral AI")

# ==========================
# Layout
# ==========================

left, right = st.columns([1, 1.2])

# ==========================
# LEFT PANEL
# ==========================

with left:

    st.subheader("Input")

    recipient_profile = st.text_area(
        "Recipient Profile",
        height=120,
        placeholder="Founder of AI startup, recruiter, hiring manager..."
    )

    sender_info = st.text_area(
        "Sender Information",
        height=120,
        placeholder="AI/ML student, GenAI projects, internship experience..."
    )

    goal = st.text_input(
        "Goal",
        placeholder="Seeking AI/ML Internship"
    )

    generate_btn = st.button(
        "🚀 Generate Email",
        use_container_width=True
    )

# ==========================
# RIGHT PANEL
# ==========================

with right:

    st.subheader("Output")

    if generate_btn:

        if not recipient_profile or not sender_info or not goal:
            st.warning("Please fill all fields.")
            st.stop()

        with st.spinner("Generating email..."):

            final_prompt = prompt.invoke(
                {
                    "recipient_profile": recipient_profile,
                    "sender_info": sender_info,
                    "goal": goal,
                    "format_instructions":
                        parser.get_format_instructions()
                }
            )

            response = model.invoke(final_prompt)

            try:

                parsed_output = parser.parse(
                    response.content
                )

                email_preview = f"""Subject: {parsed_output.subject}

{parsed_output.body}
"""

                tab1, tab2 = st.tabs(
                    ["📨 Email Preview", "📄 JSON"]
                )

                # ==================
                # EMAIL TAB
                # ==================

                with tab1:

                    st_copy_to_clipboard(
                        email_preview,
                        "📋 Copy Email"
                    )

                    st.markdown(
                        f"""
<div class="email-card">
{email_preview}
</div>
""",
                        unsafe_allow_html=True
                    )

                # ==================
                # JSON TAB
                # ==================

                with tab2:

                    st.json(
                        {
                            "subject":
                                parsed_output.subject,
                            "body":
                                parsed_output.body
                        }
                    )

            except Exception as e:

                st.error("Parsing Error")

                st.code(response.content)

                st.exception(e)

    else:

        st.info(
            "Fill the form on the left and click Generate Email."
        )
