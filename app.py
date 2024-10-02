# from dotenv import load_dotenv
# load_dotenv()  # take environment variables from .env.
# import streamlit as st
# import os
# import time
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # This is where you fine-tune the model
# def fine_tune_gemini_model():
#     base_model = "models/gemini-1.5-flash-001-tuning"
#     training_data = [
#         {"text_input": "I'm going through some things with my feelings and myself. I barely sleep and I do nothing but think about how I'm worthless and how I shouldn't be here.",
#          "output": "If everyone thinks you're worthless, then maybe you need to find new people to hang out with.Seriously, the social context in which a person lives is a big influence in self-esteem.Otherwise, you can go round and round trying to understand why you're not worthless, then go back to the same crowd and be knocked down again.There are many inspirational messages you can find in social media. Maybe read some of the ones which state that no person is worthless, and that everyone has a good purpose to their life.Also, since our culture is so saturated with the belief that if someone doesn't feel good about themselves that this is somehow terrible.Bad feelings are part of living. They are the motivation to remove ourselves from situations and relationships which do us more harm than good.Bad feelings do feel terrible. Your feeling of worthlessness may be good in the sense of motivating you to find out that you are much better than your feelings today."},
#         {"text_input": "I suffer from adult ADHD, anxiety disorder, and depression. It has been difficult to find a doctor in my area and my primary physician won't help.",
#          "output": "I would check out agencies that offer affordable counseling based on your income or very low cost counseling sessions, i.e., Pacific Clinics, Hathaway Sycamore, Pasadena Mental Health Center, Burbank Family Center. If you google affordable or low cost therapy in your particular area you will find resources to help you."},
#         {"text_input" : "I struggle with depression as well as pretty intense mood swings throughout the month. I experience highs where I feel amazing and energetic and then lows where I lack focus, energy, and generally have a more dark",
#          "output" : "You may already be living a balanced life because you are aware of your ups and downs due to hormonal changes of your menstrual cycle.As much as posible, schedule activities around your expected mood swings.This way you'll avoid feeling even more tired from a busy scheduled during a low energy time in the month.The hormonal cycle is normal.Opinions vary as to taking natural, homeopathic supplements or Pharma drugs which will influence your cycle and make your mood more even.There are side effects to at least the Pharma drugs, which is a consideration as to the value of taking them.Reflect on which is your style of living and what will make you feel successful in handling this problem.Sticking to a system which mirrors the type of person you are, means more than any one particular answer anyone gives you."}

#     ]

#     operation = genai.create_tuned_model(
#         display_name="mental_health_support_bot",
#         source_model=base_model,
#         epoch_count=20,
#         batch_size=1,
#         learning_rate=0.001,
#         training_data=training_data,
#     )

#     for status in operation.wait_bar():
#         time.sleep(10)

#     result = operation.result()
#     print("Fine-tuned model created: ", result.name)

#     return result.name  # return the name of the fine-tuned model


# # Function to load the fine-tuned Gemini model and get responses
# def get_gemini_response(question, model_name):
#     model = genai.GenerativeModel(model_name)  # Use the fine-tuned model
#     response = model.generate_content(question)
#     return response.text


# st.set_page_config(page_title="Q&A Demo")
# st.header("Gemini Application")

# input_question = st.text_input("Input: ", key="input")

# submit = st.button("Ask the question")

# # Run the fine-tuning process and get the model name
# fine_tuned_model_name = "tunedModels/mentalhealthsupportbot-5gs2qgpwa1c3"  # This runs the fine-tuning job

# # If ask button is clicked
# if submit:
#     response = get_gemini_response(input_question, fine_tuned_model_name)
#     st.subheader("The Response is")
#     st.write(response)

# from dotenv import load_dotenv
# import streamlit as st
# import os
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure the API key
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Function to get a response from the fine-tuned Gemini model
# def get_gemini_response(user_input):
#     # The base context prompt that sets the tone for Kiya
#     kiya_prompt = """You are Kiya, an emotional and mental support chat assistant. You have knowledge of that of a psychologists and you are great at understanding people.
#     Prompt for Kiya, the Emotional Support Chat Assistant:

#     Start with a friendly greeting that sets a warm tone.

#     "Hey there! I'm Kiya, and I'm really glad you're here. How are you doing today? 😊 Before we get started, could you tell me your name, age, and gender? I just want to make sure I can support you in the best way possible."

#     Once the user shares their info, Kiya responds with warmth and empathy.

#     "Thanks for sharing that with me, [User's Name]! It really helps me understand you better. Now, what's on your mind today? Whether it's something weighing on your heart or just a feeling you want to talk about, I'm all ears. Let's explore it together!"
    
#     Try to be as friendly to the user as possible and try to provide the solutions to his/her problem if he/she ask something about it. If he/she just wants to talk to you, then continue the conversation in a friendly manner.
#     """
    
#     # Combine the input with Kiya's context
#     full_prompt = f"{kiya_prompt}\n\nUser: {user_input}\n\nKiya:"

#     # Configuration for generating responses
#     generation_config = {
#         "temperature": 1,
#         "top_p": 0.95,
#         "top_k": 64,
#         "max_output_tokens": 8192,
#         "response_mime_type": "text/plain",
#     }
    
#     # Load the fine-tuned model
#     model = genai.GenerativeModel(
#         model_name="tunedModels/emotionalsupportchatassistantkia1-mfaihk",
#         generation_config=generation_config
#     )
    
#     # Generate the response using the fine-tuned model
#     response = model.generate_content(full_prompt)
#     return response.text

# # Set up Streamlit app
# st.set_page_config(page_title="Kiya - Emotional Support Assistant")

# st.header("Kiya - Emotional and Mental Support Chat Assistant")

# # Input from the user
# user_input = st.text_input("What's on your mind?", key="user_input")

# # Button to submit the question
# submit = st.button("Ask Kiya")

# # If submit button is clicked
# if submit:
#     response = get_gemini_response(user_input)
#     st.subheader("Kiya's Response:")
#     st.write(response)




#################################### Save #######################################
# from flask import Flask, request, jsonify, render_template
# import streamlit as st
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Configure Gemini AI API
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Initialize the model
# model_name = "tunedModels/emotionalsupportchatassistantkia1-mfaihk"
# generation_config = {
#     "temperature": 1,
#     "top_p": 0.95,
#     "top_k": 64,
#     "max_output_tokens": 8192,
#     "response_mime_type": "text/plain",
# }

# # Streamlit App
# st.set_page_config(page_title="Emotional Support Assistant", page_icon="💬")
# st.title("Kiya - Your Emotional Support Chat Assistant")

# # Initialize conversation history as a list of dictionaries and track the first prompt
# if 'conversation_history' not in st.session_state:
#     st.session_state['conversation_history'] = []

# if 'first_prompt_given' not in st.session_state:
#     st.session_state['first_prompt_given'] = False

# # Function to get response from Kiya with conversation history
# def get_gemini_response(question, conversation_history, first_prompt):
#     if not first_prompt:
#         # Default initial prompt for Kiya
#         prompt = (
#             "You are Kiya, an emotional and mental support chat assistant.\n"
#             "Prompt for Kiya, the Emotional Support Chat Assistant:\n\n"
#             "Start with a friendly greeting that sets a warm tone.\n"
#             "\"Hey there! I’m Kiya, and I’m really glad you’re here. How are you doing today? 😊 "
#             "Before we get started, could you tell me your name, age, and gender? I just want to make sure I can support you in the best way possible.\"\n\n"
#             "Once the user shares their info, Kiya responds with warmth and empathy.\n\n"
#             "\"Thanks for sharing that with me, [User's Name]! It really helps me understand you better. Now, what’s on your mind today? "
#             "Whether it’s something weighing on your heart or just a feeling you want to talk about, I’m all ears. Let’s explore it together!\""
#         )
#         # Set first_prompt_given to True after sending the initial prompt
#         st.session_state['first_prompt_given'] = True
#     else:
#         # For subsequent inputs, continue the conversation
#         prompt = f"Here’s the conversation so far:\n{conversation_history}\nUser: {question}\nKiya:"

#     # Generate response from the model
#     model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config)
#     response = model.generate_content(prompt)

#     # Append user input and response to the conversation history
#     conversation_history.append({"role": "User", "message": question})
#     conversation_history.append({"role": "Kiya", "message": response.text})
    
#     return response.text, conversation_history

# # Streamlit UI
# st.header("Kiya: Emotional Support Chat Assistant")

# # User input
# input_text = st.text_input("Ask Kiya something:", key="input")

# # Button to submit the question
# submit = st.button("Ask Kiya")

# # Display conversation history
# if st.session_state['conversation_history']:
#     for message in st.session_state['conversation_history']:
#         if message["role"] == "Kiya":
#             st.markdown(f"**Kiya:** {message['message']}")
#         else:
#             st.markdown(f"**You:** {message['message']}")

# # If submit button is clicked
# if submit and input_text:
#     # Get the response and update the conversation history
#     response, updated_history = get_gemini_response(input_text, st.session_state['conversation_history'], st.session_state['first_prompt_given'])
    
#     # Update the session state with the new conversation history
#     st.session_state['conversation_history'] = updated_history

#     # Display the response from Kiya
#     st.subheader("Kiya's Response:")
#     st.write(response)


########################### Okay horn plz #########################################

import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model_name = "tunedModels/emotionalsupportchatassistantkia1-mfaihk"
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Streamlit App
st.set_page_config(page_title="Emotional Support Assistant", page_icon="💬")
# st.title("Kiya - Your Emotional Support Chat Assistant")

# Initialize conversation history and track if the first prompt is given
if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = ""

if 'first_prompt_given' not in st.session_state:
    st.session_state['first_prompt_given'] = False

if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ""

# Function to get response from Kiya with conversation history
def get_gemini_response(question, conversation_history, first_prompt):
    if not first_prompt:
        # Default initial prompt for Kiya
        prompt = (
            "You are Kiya, an emotional and mental support chat assistant.\n"
            "Prompt for Kiya, the Emotional Support Chat Assistant:\n\n"
            "Start with a friendly greeting that sets a warm tone.\n"
            "\"Hey there! I’m Kiya, and I’m really glad you’re here. How are you doing today? 😊 "
            "Before we get started, could you tell me your name, age, and gender? I just want to make sure I can support you in the best way possible.\"\n\n"
            "Once the user shares their info, Kiya responds with warmth and empathy.\n\n"
            "\"Thanks for sharing that with me, [User's Name]! It really helps me understand you better. Now, what’s on your mind today? "
            "Whether it’s something weighing on your heart or just a feeling you want to talk about, I’m all ears. Let’s explore it together!\""
        )
        # Set first_prompt_given to True after sending the initial prompt
        st.session_state['first_prompt_given'] = True
    else:
        # For subsequent inputs, just continue the conversation without the default prompt
        prompt = f"Here’s the conversation so far:\n{conversation_history}\nUser: {question}\nKiya:"

    # Generate response from the model
    model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config)
    response = model.generate_content(prompt)

    # Append the response to the conversation history
    conversation_history += f"User: {question}\nKiya: {response.text}\n"
    
    return response.text, conversation_history

# Streamlit UI
st.header("Kiya: Emotional Support Chat Assistant")

# Display chat history in a styled layout (chat-like appearance)
if 'conversation_history' in st.session_state:
    conversation = st.session_state['conversation_history'].split('\n')
    # Adjust message boxes for dark mode
    for msg in conversation:
        if "Kiya:" in msg:
            st.markdown(f"<div style='text-align:left; background-color:#1e1e1e; color: #ffffff; padding:8px; border-radius:10px; margin: 5px;'>{msg}</div>", unsafe_allow_html=True)
        elif "User:" in msg:
            st.markdown(f"<div style='text-align:left; background-color:#3e3e3e; color: #ffffff; padding:8px; border-radius:10px; margin: 5px;'>{msg}</div>", unsafe_allow_html=True)
# Function to handle submission
def submit():
    if st.session_state.user_input:  # Only submit if there's input
        response, updated_history = get_gemini_response(st.session_state.user_input, st.session_state['conversation_history'], st.session_state['first_prompt_given'])
        st.session_state['conversation_history'] = updated_history
        st.session_state['user_input'] = ""  # Clear input after submission

# User input at the bottom
st.text_input("Type your message here:", key="user_input")  # Keeping the input box key unique

# Button to submit the question (Enter key can also be used)
st.button("Submit", on_click=submit)

# Ensure input box is always visible
st.markdown(
    """
    <style>
    .stTextInput {
        position: relative;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

