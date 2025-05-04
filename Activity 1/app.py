import streamlit as st

st.title("Hello, Streamlit!")
st.header("🚀 Getting Started with Streamlit")
st.write("This is a simple app to demonstrate basic components.")

# Inputs
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=120)

# Output
if name and age:
    st.write(f"👋 Hello, {name}! You are {age} years old.")
