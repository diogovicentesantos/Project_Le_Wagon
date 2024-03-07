import streamlit as st
from amerigo_py_files.amerigo_functions import *

set_background('/Users/amerigogiol/code/diogovicentesantos/Project_Le_Wagon/app/backgrounds/e9f6a650ec6f8b133f30fedd061378c5.jpg')

st.header('here are you cooking possibilities:')


btn2 = st.button('Restart')

if btn2:
    switch_page('ingredients')
