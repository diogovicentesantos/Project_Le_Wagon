import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients
from amerigo_py_files.amerigo_functions import *

set_background('/Users/amerigogiol/code/diogovicentesantos/Project_Le_Wagon/app/backgrounds/1c346cf092cb426720c1828906babd83.jpg')

st.title("Ingredients🥬🍎")

# Define your list of elements
elements = get_unique_ingredients()

selected_ingredients = st.multiselect("Select ingredients", elements)

# Show the selected elements
st.write("Selected ingredients:", selected_ingredients)

btn = st.button('next: prompt')

if btn:
    switch_page('Text')
