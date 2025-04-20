import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

# Load Groq API key from environment
groq_api_key = os.getenv("GROQ_API_KEY")

# Quick check (optional, remove after testing)
if not groq_api_key:
    raise ValueError("🚨 GROQ_API_KEY is not set. Please check your .env file.")

# Initialize the Groq LLM with the model you want to use
llm = ChatGroq(
    temperature=0.7,
    groq_api_key=groq_api_key,
    model_name="llama3-70b-8192"  # You can also try llama3-8b-8192
)

# Define the prompt structure
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a mental health companion that offers kind, supportive, and emotionally intelligent responses."),
    ("user", "{input}")
])

# Output parser to extract final string
output_parser = StrOutputParser()

# Chain the prompt, model, and parser together
chain = prompt | llm | output_parser

# CLI-style chat loop
print("🧘 Mental Health Companion")
print("Type something to begin. Type 'exit' to end.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Companion: Take care, and remember you're not alone. 💛")
        break

    try:
        response = chain.invoke({"input": user_input})
        print(f"Companion: {response.strip()}\n")
    except Exception as e:
        print(f"⚠️ Error: {e}")
