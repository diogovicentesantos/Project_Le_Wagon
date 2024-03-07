import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients
from amerigo_py_files.amerigo_functions import *

set_background('/Users/amerigogiol/code/diogovicentesantos/Project_Le_Wagon/app/backgrounds/337207f4a4f73a42ac67d4173524a25d.jpg')

st.title("What do u feel like having?🍝 ")
st.subheader('(e.g: Italian food, something cold...)')
# Text input box for the user
user_text = st.text_input("Enter your text:")
st.write('your prompt: ' + user_text) #checking user_text

btn = st.button('Next: Time')

if btn:
    switch_page('time')
