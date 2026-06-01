import streamlit as st
import json
import random

with open("questions.json", "r") as file:
    questions = json.load(file)

st.title("AI Interview Coach")

question = random.choice(questions)

st.subheader("Interview Question")
st.write(question)

answer = st.text_area("Your Answer")

if st.button("Submit"):
    st.success("Answer Submitted!")