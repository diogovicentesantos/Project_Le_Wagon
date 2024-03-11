import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients
from amerigo_py_files.amerigo_functions import *
#set_background('/Users/amerigogiol/code/diogovicentesantos/Project_Le_Wagon/app/backgrounds/Presentation1_page-0001.jpg')

st.title("Restrictions 🙅‍♂️")

# Define your list of preferences
preferences = ["gluten free", "vegan", "vegetarian", "light", "healthy"]

st.session_state.selected_preferences = st.multiselect("Select Elements", preferences)

# Show the selected elements
st.write("Selected Preferences:", st.session_state.selected_preferences)

st.write('So far: ')
st.write(st.session_state.selected_ingredients)
st.write(st.session_state.user_text)
st.write(st.session_state.selected_time)
st.write(st.session_state.selected_preferences)


btn = st.button('See recipes!')

if btn:
    switch_page('output')

backbtn = st.button('go back to Time')
if backbtn:
    switch_page('time')
