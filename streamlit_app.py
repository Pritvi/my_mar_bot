import streamlit as st
from openai import OpenAI

# Initialize OpenAI client using Streamlit's secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Title of the app
st.title("Your Health Symptom Checker")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    role, content = message["role"], message["content"]
    with st.chat_message(role):
        st.markdown(content)

# Collect user input for symptoms
user_input = st.chat_input("Ask me anything about skincare...")

# Function to get a response from OpenAI with health advice
def get_response(prompt):

     messages.insert(0, {
        "role": "system",
        "content": "You are a skincare expert. You can only answer questions related to skincare, such as skincare routines, ingredients, skin types, and best practices. If the user asks anything off-topic, politely redirect them back to skincare."
    })
    # Here, you may include a more specific prompt or fine-tune the assistant's instructions to provide general remedies
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ] + [{"role": "user", "content": prompt}]
    )
    # Access the content directly as an attribute
  
   return response["choices"][0]["message"]["content"]

# Process and display response if there's input
if user_input:

     # Define allowed topics
    allowed_topics = ["skincare", "skin", "moisturizer", "acne", "sunscreen", "routine", "beauty", "face wash"]

    if not any(topic in user_input.lower() for topic in allowed_topics):
        response_text = "I'm here to talk about skincare! Let's discuss skincare routines, products, or tips."
    else:
        # Append user's message
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)
                # Get assistant response
        response_text = get_response(st.session_state.messages)

        # Append assistant's response
        st.session_state.messages.append({"role": "assistant", "content": response_text})
    
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
