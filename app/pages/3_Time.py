import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients
from amerigo_py_files.amerigo_functions import *

import os

parent_dir = os.getcwd()
filepath = os.path.join(parent_dir, "app", "backgrounds", "doughnuts-yellow-lewagon-projecttop-view-donuts-chocolate-yellow-floor.jpg")
set_background(filepath)

# Select Time Interface
st.subheader("Time Available")

# Display a slider for time selection
st.session_state.selected_time = st.slider("Select Time(min):", 0, 240, step=5, value=(0, 240))
st.write(st.session_state.selected_time)

st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space

# Create two columns for the buttons
col1, spacer, col2 = st.columns([1, 2, 1])


# Place the first button in the first column
with col1:
    backbtn = st.button('Back: Feelings')
    if backbtn:
        switch_page('Feelings')


# Place the second button in the second column
with col2:
    btn = st.button('Next: Restrictions')
    if btn:
        switch_page('Restrictions')


st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space


st.markdown("""
<style>
.custom-font {
    font-style: italic;
    text-decoration: underline;
}
</style>
<div class='custom-font'>Selected Ingredients:</div>
""", unsafe_allow_html=True)
st.markdown(st.session_state.selected_ingredients_text)


st.markdown("""
<style>
.custom-font {
    font-style: italic;
    text-decoration: underline;
}
</style>
<div class='custom-font'>Your Feelings:</div>
""", unsafe_allow_html=True)
st.write(st.session_state.user_text)
