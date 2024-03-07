import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients
from amerigo_py_files.amerigo_functions import *

set_background('/Users/amerigogiol/code/diogovicentesantos/Project_Le_Wagon/app/backgrounds/337207f4a4f73a42ac67d4173524a25d.jpg')


# Select Time Interface
st.subheader("Time Available")

# Display a slider for time selection
selected_time = st.slider("Select Time(min):", 0, 240, step=5, value=(0, 240))
st.write(selected_time)

btn = st.button('back to search!')

if btn:
    switch_page('restrictions')
