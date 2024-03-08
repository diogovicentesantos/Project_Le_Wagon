
import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients
from amerigo_py_files.amerigo_functions import *

#set_background('/Users/amerigogiol/code/diogovicentesantos/Project_Le_Wagon/app/backgrounds/Presentation1_page-0001.jpg')
st.header('WELCOME TO RECEIPT GENERATOR')
st.subheader('Find recipes that suits you based on: the ingredients you have, your allergies, time available and, HOW YOU ARE FEELING!')

btn = st.button('Press Here to start')

if btn:
   switch_page('ingredients')
