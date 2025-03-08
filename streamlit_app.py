import openai
import streamlit as st

# Set up OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# App title
st.title("Skincare Expert ChatBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask me anything about skincare...")

def get_response(messages):
    # System prompt to keep the bot focused on skincare
    messages.insert(0, {
        "role": "system",
        "content": "You are a skincare expert. You can only answer questions related to skincare, such as skincare routines, ingredients, skin types, and best practices. If the user asks anything off-topic, politely redirect them back to skincare."
    })

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    return response["choices"][0]["message"]["content"]

if user_input:
    # Define allowed topics
    allowed_topics = ["skincare", "skin", "moisturizer", "acne", "sunscreen", "routine", "beauty", "face wash"]

    # Check if the user's message contains relevant keywords
    if not any(topic in user_input.lower() for topic in allowed_topics):
        response_text = "I'm here to talk about skincare! Let's discuss skincare routines, products, or tips."
    else:
        # Append user's message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Display user's message
        with st.chat_message("user"):
            st.markdown(user_input)

        # Get assistant response
        response_text = get_response(st.session_state.messages)

        # Append assistant's response
        st.session_state.messages.append({"role": "assistant", "content": response_text})

    # Display assistant's response
    with st.chat_message("assistant"):
        st.markdown(response_text)
