import streamlit as st
from amerigo_py_files.amerigo_functions import *

import os

######################### New code Diogo - test ################################
# from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
# conn = st.connection('gcs', type=FilesConnection)
# element_list_pkl = conn.read("recipe-lewagon-madrid-project/element_list.pkl", input_format=".pkl", ttl=600)
# km_model_OpenAI_pkl = conn.read("recipe-lewagon-madrid-project/km_model_OpenAI.pkl", input_format=".pkl", ttl=600)
# preprocessed_data_pkl = conn.read("recipe-lewagon-madrid-project/preprocessed_data.pkl", input_format=".pkl", ttl=600)
# preprocessed_data_with_ingredients_pkl = conn.read("recipe-lewagon-madrid-project/preprocessed_data_with_ingredients.pkl", input_format=".pkl", ttl=600)
# ten_embeddings_temp_array_nom_pkl = conn.read("recipe-lewagon-madrid-project/ten_embeddings_temp_array_nom.pkl", input_format=".pkl", ttl=600)



######################### End of Diogo Test ####################################

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
