import streamlit as st
import json
import os

# Function to load the chatbot words from the JSON file
def load_chatbot_words():
    try:
        with open('chat.json', 'r') as file:
            content = file.read()
            if not content:
                st.error("The JSON file is empty.")
                return None
            chatbot_words = json.loads(content)  # Use loads to print the content first
        return chatbot_words
    except json.JSONDecodeError as e:
        st.error(f"Error reading the JSON file: {e}")
        return None
    except FileNotFoundError:
        st.error("The file chatbot_words.json was not found.")
        return None

# Function to generate a response based on user input
def generate_response(user_input, chatbot_words):
    # Check for greetings
    if any(word.lower() in user_input.lower() for word in chatbot_words["greetings"]):
        return "Hello! How can I assist you today?"
    
    # Check for gratitude
    if any(word.lower() in user_input.lower() for word in chatbot_words["gratitude"]):
        return "You're welcome! Let me know if you need anything else."
    
    # Check for questions
    if any(word.lower() in user_input.lower() for word in chatbot_words["questions"]):
        return "That's an interesting question! Let me try to help you."
    
    # Check for farewells
    if any(word.lower() in user_input.lower() for word in chatbot_words["farewells"]):
        return "Goodbye! Have a great day!"
    
    if any(word.lower() in user_input.lower() for word in chatbot_words["apologies"]):
        return "i apologies!"
    
    if any(word.lower() in user_input.lower() for word in chatbot_words["answers"]):
        return "this is the answer!"
    
    if any(word.lower() in user_input.lower() for word in chatbot_words["help"]):
        return "ok!"
    
    if any(word.lower() in user_input.lower() for word in chatbot_words["clarifications"]):
        return "clarify it!"
    
    if any(word.lower() in user_input.lower() for word in chatbot_words["confirmations"]):
        return "would you confirm!"
    
    if any(word.lower() in user_input.lower() for word in chatbot_words["negatives"]):
        return "are kidding me"
    
    if any(word.lower() in user_input.lower() for word in chatbot_words["affirmatives"]):
        return "too bad"
    
    if any(word.lower() in user_input.lower() for word in chatbot_words["expressions "]):
        return "Good job!"
    
    if any(word.lower() in user_input.lower() for word in chatbot_words["empathy "]):
        return "Have a great day!"
    
    if any(word.lower() in user_input.lower() for word in chatbot_words["encouragement "]):
        return "its ok! Have a great day!"
    
    if any(word.lower() in user_input.lower() for word in chatbot_words["fruits "]):
        return "which fruits!"
    
    if any(word.lower() in user_input.lower() for word in chatbot_words["vegetables "]):
        return "which vegetable!"
    
    if any(word.lower() in user_input.lower() for word in chatbot_words["animals "]):
        return "Tell me! which one!"
    
    
    return "Sorry, I didn't quite understand that. Could you rephrase?"

# Function to clear the cache
def clear_cache():
    st.cache_data.clear()
    st.success("Cache cleared!")

# Title and description
st.title(" Chatbot")
st.write("Start chatting with the chatbot!")

# Initialize session state to store conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Load the chatbot words from the JSON file
chatbot_words = load_chatbot_words()

# Only proceed if the chatbot words are loaded successfully
if chatbot_words:
    # Get user input (new input box each time)
    user_input = st.text_input("You: ", key="user_input")

    # If there is user input, process and generate response
    if user_input:
        # Add user message to conversation
        st.session_state.conversation.append({"role": "user", "content": user_input})
        
        # Generate AI response based on user input
        ai_response = generate_response(user_input, chatbot_words)
        
        # Add AI message to conversation
        st.session_state.conversation.append({"role": "assistant", "content": ai_response})
        
        # Display the conversation
        for message in st.session_state.conversation:
            if message["role"] == "user":
                st.write(f"**You:** {message['content']}")
            else:
                st.write(f"**AI:** {message['content']}")

    # Provide the option to save the conversation as JSON
    if st.button("Save Conversation as JSON"):
        # Convert the conversation list into a JSON string
        conversation_json = json.dumps(st.session_state.conversation, indent=4)
        
        # Write the JSON to a file
        with open("conversation.json", "w") as f:
            f.write(conversation_json)
        
        # Provide a download link for the conversation JSON file
        st.download_button(
            label="Download Conversation",
            data=conversation_json,
            file_name="conversation.json",
            mime="application/json"
        )
    
    # Button to clear the cache
    if st.button("Clear Cache"):
        clear_cache()
