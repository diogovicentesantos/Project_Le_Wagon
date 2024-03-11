import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients
from amerigo_py_files.amerigo_functions import *

#set_background('/Users/amerigogiol/code/diogovicentesantos/Project_Le_Wagon/app/backgrounds/Presentation1_page-0001.jpg')


# Select Time Interface
st.subheader("Time Available")

# Display a slider for time selection
st.session_state.selected_time = st.slider("Select Time(min):", 0, 240, step=5, value=(0, 240))
st.write(st.session_state.selected_time)

st.write('So far: ')
st.write(st.session_state.selected_ingredients)
st.write(st.session_state.user_text)

btn = st.button('Next: restrictions')
if btn:
    switch_page('restrictions')

backbtn = st.button('go back to Text')
if backbtn:
    switch_page('Text')

st.write(st.session_state.selected_ingredients)
