import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients
from amerigo_py_files.amerigo_functions import *

import os

st.set_page_config(initial_sidebar_state="collapsed")
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

parent_dir = os.getcwd()
filepath = os.path.join(parent_dir, "background", "light_blue-lewagon-project-fresh-colourful-ingredients-mexican-cuisine.jpg")
set_background(filepath)


st.title("Restrictions :man-gesturing-no:")

# Define your list of preferences
preferences = ["gluten free", "vegan", "vegetarian", "light", "healthy"]
st.session_state.selected_preferences = st.multiselect("Select Elements", preferences)


st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space

# Create two columns for the buttons
col1, spacer, col2 = st.columns([1, 2, 1])


# Place the first button in the first column
with col1:
    backbtn = st.button('Back: Time')
    if backbtn:
        switch_page('Time')


# Place the second button in the second column
with col2:
    btn = st.button('See recipes!')
    if btn:
        switch_page('Recipes')


st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space
