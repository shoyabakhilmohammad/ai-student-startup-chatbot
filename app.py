import streamlit as st
import random

# Sample chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey 👋"],
    "how are you": ["I'm good, thank you!", "Doing great!", "All good here 😃"],
    "student": ["I can help with study tips 📚", "Focus on consistency and practice!"],
    "startup": ["Start small, validate your idea 🚀", "Build an MVP first!"],
    "bye": ["Goodbye!", "See you later!", "Bye 👋"]
}

# Function to get response
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I don’t understand that yet."

# Streamlit UI
st.title("🤖 AI Chatbot for Students & Startups")
st.write("Ask me something!")

user_input = st.text_input("You: ")

if st.button("Send"):
    reply = get_response(user_input)
    st.text_area("Chatbot:", value=reply, height=100)
