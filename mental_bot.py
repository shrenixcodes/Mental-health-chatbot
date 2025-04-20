from langchain_groq import ChatGroq

# STEP 1: Initialize the chatbot
llm = ChatGroq(
    temperature=0.7,
    groq_api_key="your_groq_api_key_here",  # <-- Replace this
    model_name="llama-3-70b-8192"
)

# STEP 2: Start a conversation
while True:
    user_input = input("🧠 You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("🫶 Take care! Bye.")
        break
    response = llm.invoke(f"You are a compassionate mental health assistant. {user_input}")
    print("🤖 Bot:", response.content)
