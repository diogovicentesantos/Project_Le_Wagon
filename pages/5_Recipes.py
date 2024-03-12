import streamlit as st
from amerigo_py_files.amerigo_functions import *
from model.main import main


import os

parent_dir = os.getcwd()
filepath = os.path.join(parent_dir, "background", "flat-lay-concept-clipboard.jpg")
set_background(filepath)

name_list, recipe_link_list, warning = main(st.session_state.selected_ingredients_text, st.session_state.user_text, st.session_state.selected_ingredients_text)

if name_list == []:
    st.write("Sorry, we couldn't indentify recipes suited to your request")
else:
    st.markdown(" ")  # Adds a space
    st.markdown(" ")  # Adds a space
    st.markdown(" ")  # Adds a space
    st.header('Here are our suggested recipes!')
    st.markdown(" ")  # Adds a space
    st.markdown(warning)
    st.markdown(" ")  # Adds a space

    for i, recipe_name in enumerate(name_list):
        st.markdown(f'{i+1}) [{recipe_name}]({recipe_link_list[i]})')


st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space


btn2 = st.button('Restart')

if btn2:
    st.session_state.clear()
    switch_page('Ingredients')
