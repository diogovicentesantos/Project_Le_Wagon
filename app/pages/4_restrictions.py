import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients
from amerigo_py_files.amerigo_functions import *
set_background('/Users/amerigogiol/code/diogovicentesantos/Project_Le_Wagon/app/backgrounds/23004922017a36941020979baf7c1993.jpg')

st.title("Restrictions 🙅‍♂️")

# Define your list of preferences
preferences = ["gluten free", "vegan", "vegetarian", "light", "healthy"]

selected_preferences = st.multiselect("Select Elements", preferences)

# Show the selected elements
st.write("Selected Preferences:", selected_preferences)

btn = st.button('See recipes!')

if btn:
    switch_page('output')
