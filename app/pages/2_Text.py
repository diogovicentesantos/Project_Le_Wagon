import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients
from amerigo_py_files.amerigo_functions import *

#set_background('/Users/amerigogiol/code/diogovicentesantos/Project_Le_Wagon/app/backgrounds/1c346cf092cb426720c1828906babd83.jpg')

st.title("What do u feel like having?🍝 ")
st.subheader('(e.g: Italian food, something cold...)')
# Text input box for the user
st.session_state.user_text = st.text_input("Enter your text:")
st.write('your prompt: ' + st.session_state.user_text) #checking user_text

btn = st.button('Next: Time')

st.write('So far: ')
st.write(st.session_state.selected_ingredients)

if btn:
    switch_page('time')



backbtn = st.button('go back to Ingredients')
if backbtn:
    switch_page('ingredients')
