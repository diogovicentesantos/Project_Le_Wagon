import streamlit as st
from amerigo_py_files.unique_ingredients_module import load_ingredient_list
from amerigo_py_files.amerigo_functions import *

import os

parent_dir = os.getcwd()
filepath = os.path.join(parent_dir, "app", "backgrounds", "red-fruits-vegetables-arrangement-top-view.jpg")
set_background(filepath)


st.title("Ingredients🥬🍎")

# Define your list of elements
elements = load_ingredient_list()
st.session_state.selected_ingredients_list = st.multiselect("Select ingredients", elements)
st.session_state.selected_ingredients_text = " ".join(st.session_state.selected_ingredients_list)

st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space

# Create two columns for the buttons
col1, spacer, col2 = st.columns([1, 2, 1])

# Place the second button in the second column
with col2:
    btn = st.button('Next: Your mood')
    if btn:
        switch_page('Feelings')
