import streamlit as st
from amerigo_py_files.amerigo_functions import *

import os

st.set_page_config(initial_sidebar_state="collapsed")
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

parent_dir = os.getcwd()
filepath = os.path.join(parent_dir, "background", "dipping-nacho-chips.jpg")
set_background(filepath)

st.header('WELCOME TO RECEIPT GENERATOR')
st.write('Find recipes that suits you based on:')
st.write('- the ingredients you have')
st.write('- your allergies')
st.write('- your available time')
st.write('- How You Are Feeling!')

st.write(" ")

btn = st.button('Press Here to start')

if btn:
   switch_page('ingredients')
