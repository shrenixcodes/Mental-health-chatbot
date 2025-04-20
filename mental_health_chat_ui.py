import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 🧠 1. Page Config (must be first!)
st.set_page_config(page_title="🧠 Mental Health Companion", page_icon="💬")

# 🌿 2. Custom CSS
st.markdown("""
    <style>
        .block-container {
            max-width: 100% !important;
            padding: 2rem 3rem;
        }

        body {
            background-color: #0f1117;
            color: #e0f2f1;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Chat bubble container */
        .chat-container {
            display: flex;
            margin-bottom: 1rem;
        }

        /* Bubble styles */
        .chat-bubble {
            padding: 12px 18px;
            border-radius: 20px;
            max-width: 70%;
            font-size: 16px;
            line-height: 1.5;
        }

        /* User message: right aligned */
        .user-message {
            justify-content: flex-end;
        }

        .user-bubble {
            background-color: #b3e5fc;
            color: #004d40;
            text-align: right;
        }

        /* Bot message: left aligned */
        .bot-message {
            justify-content: flex-start;
        }

        .bot-bubble {
            background-color: #dcedc8;
            color: #33691e;
            text-align: left;
        }

        /* Chat input styling */
        .st-chat-input input {
            font-size: 16px;
            border-radius: 12px;
            padding: 10px;
            background-color: #ffffff;
            border: 1px solid #b2dfdb;
            width: 100%;
        }

        .stButton>button {
            background-color: #4caf50;
            color: white;
            border-radius: 20px;
            font-size: 16px;
            padding: 8px 16px;
        }

        .stButton>button:hover {
            background-color: #388e3c;
        }
    </style>
""", unsafe_allow_html=True)

# 🧠 3. App Header
st.markdown("""
    <div style="text-align: center; margin-top: 1rem; margin-bottom: 2rem;">
        <h1 style="font-size: 2.5rem;">🧠 Mental Health Companion</h1>
        <p style="color: #d1d1d1; font-size: 1.1rem;">Chat privately with a kind AI listener. 🤝</p>
    </div>
""", unsafe_allow_html=True)

# 🔐 4. Load keys
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# 🤖 5. Setup LLM
llm = ChatGroq(
    temperature=0.7,
    groq_api_key=groq_api_key,
    model_name="llama3-70b-8192"
)

# 🧾 6. Prompt & Chain
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a compassionate mental health companion who listens, supports, and encourages the user."),
    ("user", "{input}")
])
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# 💾 7. Session Storage
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 💬 8. Input box
user_input = st.chat_input("How are you feeling today?")

# 🧠 9. Process chat
if user_input:
    st.session_state.chat_history.append(("You", user_input))
    response = chain.invoke({"input": user_input})
    st.session_state.chat_history.append(("Companion", response.strip()))

# 🖥️ 10. Display chat
for speaker, msg in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"""
            <div class="chat-container user-message">
                <div class="chat-bubble user-bubble">{msg}</div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="chat-container bot-message">
                <div class="chat-bubble bot-bubble">{msg}</div>
            </div>
        """, unsafe_allow_html=True)
