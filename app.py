from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import streamlit as st
import os
import time
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# This is where you fine-tune the model
def fine_tune_gemini_model():
    base_model = "models/gemini-1.5-flash-001-tuning"
    training_data = [
        {"text_input": "I'm going through some things with my feelings and myself. I barely sleep and I do nothing but think about how I'm worthless and how I shouldn't be here.",
         "output": "If everyone thinks you're worthless, then maybe you need to find new people to hang out with.Seriously, the social context in which a person lives is a big influence in self-esteem.Otherwise, you can go round and round trying to understand why you're not worthless, then go back to the same crowd and be knocked down again.There are many inspirational messages you can find in social media. Maybe read some of the ones which state that no person is worthless, and that everyone has a good purpose to their life.Also, since our culture is so saturated with the belief that if someone doesn't feel good about themselves that this is somehow terrible.Bad feelings are part of living. They are the motivation to remove ourselves from situations and relationships which do us more harm than good.Bad feelings do feel terrible. Your feeling of worthlessness may be good in the sense of motivating you to find out that you are much better than your feelings today."},
        {"text_input": "I suffer from adult ADHD, anxiety disorder, and depression. It has been difficult to find a doctor in my area and my primary physician won't help.",
         "output": "I would check out agencies that offer affordable counseling based on your income or very low cost counseling sessions, i.e., Pacific Clinics, Hathaway Sycamore, Pasadena Mental Health Center, Burbank Family Center. If you google affordable or low cost therapy in your particular area you will find resources to help you."},
        {"text_input" : "I struggle with depression as well as pretty intense mood swings throughout the month. I experience highs where I feel amazing and energetic and then lows where I lack focus, energy, and generally have a more dark",
         "output" : "You may already be living a balanced life because you are aware of your ups and downs due to hormonal changes of your menstrual cycle.As much as posible, schedule activities around your expected mood swings.This way you'll avoid feeling even more tired from a busy scheduled during a low energy time in the month.The hormonal cycle is normal.Opinions vary as to taking natural, homeopathic supplements or Pharma drugs which will influence your cycle and make your mood more even.There are side effects to at least the Pharma drugs, which is a consideration as to the value of taking them.Reflect on which is your style of living and what will make you feel successful in handling this problem.Sticking to a system which mirrors the type of person you are, means more than any one particular answer anyone gives you."}

    ]

    operation = genai.create_tuned_model(
        display_name="mental_health_support_bot",
        source_model=base_model,
        epoch_count=20,
        batch_size=1,
        learning_rate=0.001,
        training_data=training_data,
    )

    for status in operation.wait_bar():
        time.sleep(10)

    result = operation.result()
    print("Fine-tuned model created: ", result.name)

    return result.name  # return the name of the fine-tuned model


# Function to load the fine-tuned Gemini model and get responses
def get_gemini_response(question, model_name):
    model = genai.GenerativeModel(model_name)  # Use the fine-tuned model
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")

input_question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# Run the fine-tuning process and get the model name
fine_tuned_model_name = "tunedModels/mentalhealthsupportbot-5gs2qgpwa1c3"  # This runs the fine-tuning job

# If ask button is clicked
if submit:
    response = get_gemini_response(input_question, fine_tuned_model_name)
    st.subheader("The Response is")
    st.write(response)