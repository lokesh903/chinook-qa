import streamlit as st
from langchain_helper import get_few_shot_db_chain
import os
st.title("Chatbot for enquiring chinook Database 'A music store database'")

# Define example questions
suggestions = [
    "tell me sell of date 2021-01-03 ?",
    "tell me the name of all the tracks that was bought on 1st of march 2021 ?",
    "tell me Title of my employee Mitchell?",
    "how is Luís give his info ",
]



question = st.text_input("Question: ")

# Display question suggestions
st.markdown("#### Question Suggestions:")
for suggest in suggestions:
    st.write(suggest)
try:
    if question:
        chain = get_few_shot_db_chain()
        response = chain.run(question)

        st.header("Answer")
        st.write(response)
except:
    st.header("Unable to do that !")
    os.system("streamlit run main.py")