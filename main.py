# import module
import streamlit as st
from app import chat

# Title
st.title("Career Counselling")


st.header("Career Counselling")
user=st.container()
system=user.text_input("How do I behave like mentor or friend")
user_input=st.text_input("What is your interest")
response_fn_test = chat(f"You are a {system}.",[f"I am interested in {user_input} suggest me the career path"])

st.text(response_fn_test)
