import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Displaying a header
st.header("Hello, Streamlit!")

# A simple text input widget
name = st.text_input("Enter your name:")

# Display the entered name
if name:
    st.write(f"Hello, {name}!")
else:
    st.write("Please enter your name.")
