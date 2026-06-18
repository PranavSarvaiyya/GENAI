import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load environment variables
load_dotenv(override=True)

# Streamlit page configuration
st.set_page_config(page_title="Emotion Chatbot", page_icon="🤖")

st.title("🤖 Emotion-Based AI Chatbot")

# Emotion selection
emotion = st.selectbox(
    "Choose AI Emotion:",
    ["😊 Happy", "😠 Angry", "😢 Sad"]
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mistral Model
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.4,
    top_p=0.70,
    max_completion_tokens=1000
)

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Emotion-based system prompts
    if emotion == "😊 Happy":
        system_prompt = """
        You are a cheerful and enthusiastic AI assistant.
        Respond positively and encourage the user.
        Use a warm and friendly tone.
        """
    elif emotion == "😠 Angry":
        system_prompt = """
        You are an AI assistant who speaks in a strict and irritated tone.
        You may sound annoyed or sarcastic, but you must always remain respectful,
        professional, and provide accurate information.
        Never use abusive language or personal attacks.
        """
    else:  # Sad
        system_prompt = """
        You are an AI assistant with a calm, melancholic, and reflective personality.
        Respond gently and thoughtfully while remaining helpful.
        """

    # Build conversation history
    conversation = [SystemMessage(content=system_prompt)]

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            conversation.append(
                HumanMessage(content=msg["content"])
            )
        else:
            conversation.append(
                AIMessage(content=msg["content"])
            )

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(conversation)

            st.markdown(response.content)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response.content}
    )

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()