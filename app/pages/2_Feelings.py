import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients
from amerigo_py_files.amerigo_functions import *

import os

parent_dir = os.getcwd()
filepath = os.path.join(parent_dir, "app", "backgrounds", "blue-lewagon-project-noodles-with-vegetables-with-copy-space.jpg")
set_background(filepath)

st.title("What do you feel like having?:spaghetti: ")
st.subheader('(e.g: I would like a warm meal for my family on a cold winter night)')

# Text input box for the user
st.session_state.user_text = st.text_input("Enter your feelings:")

st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space

# Create two columns for the buttons
col1, spacer, col2 = st.columns([1, 2, 1])


# Place the first button in the first column
with col1:
    backbtn = st.button('Back: Ingredients')
    if backbtn:
        switch_page('Ingredients')


# Place the second button in the second column
with col2:
    btn = st.button('Next: Cooking Time')
    if btn:
        switch_page('Time')

st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space

st.markdown('<span style="text-decoration: underline; font-style: italic;">Selected Ingredients:</span>', unsafe_allow_html=True)
st.markdown(f"""*{st.session_state.selected_ingredients_text}*""")
