import streamlit as st

st.set_page_config(page_title="My App", page_icon="🚀")

st.title("My First App")
st.write("Welcome! My Streamlit app is running.")

name = st.text_input("What is your name?")

if st.button("Say hello"):
    if name.strip():
        st.success(f"Hello, {name}!")
    else:
        st.warning("Please enter your name first.")
