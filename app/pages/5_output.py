import streamlit as st
from amerigo_py_files.amerigo_functions import *

#set_background('/Users/amerigogiol/code/diogovicentesantos/Project_Le_Wagon/app/backgrounds/Presentation1_page-0001.jpg')

st.header('here are you cooking possibilities:')

st.session_state.dict_ = {
    'ingredients' : st.write(st.session_state.selected_ingredients),
    'query' : st.write(st.session_state.user_text)

}

#st.write(st.session_state.dict_)


btn2 = st.button('Restart')

if btn2:
    st.session_state.clear()
    #st.experimental_rerun()
    switch_page('ingredients')
