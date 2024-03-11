import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients
from amerigo_py_files.amerigo_functions import *
import pickle

#set_background('/Users/amerigogiol/code/diogovicentesantos/Project_Le_Wagon/app/backgrounds/Presentation1_page-0001.jpg')

st.title("Ingredients🥬🍎")

# Define your list of elements
elements = pickle.load(open('/Users/amerigogiol/code/diogovicentesantos/Project_Le_Wagon/raw_data/element_list.pkl',"rb"))

st.session_state.selected_ingredients = st.multiselect("Select ingredients", elements)

# Show the selected elements
st.write("Selected ingredients:", st.session_state.selected_ingredients)

btn = st.button('next: prompt')

if btn:
    switch_page('Text')
