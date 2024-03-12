
import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients
from amerigo_py_files.amerigo_functions import *
'''
#from streamlit_extras.switch_page_button import switch_page

#############################BACKGROUND IMAGE#######################################



#st.markdown(page_bg_img, unsafe_allow_html=True)
#backgroundColor = "#DDF7DD"
set_background('/Users/amerigogiol/code/diogovicentesantos/Project_Le_Wagon/app/pages/background.jpg')

##################################TEXTBOX#######################################
st.title("What do u feel like having?🍝 ")
st.subheader('(e.g: Italian food, something cold...)')
# Text input box for the user
user_text = st.text_input("Enter your text:")
st.write('your prompt: ' + user_text) #checking user_text

##################################INGREDIENTS#######################################

st.title("Ingredients🥬🍎")

# Define your list of elements
elements = get_unique_ingredients()

selected_ingredients = st.multiselect("Select ingredients", elements)

# Show the selected elements
st.write("Selected ingredients:", selected_ingredients)

##################################TIME#######################################

# Select Time Interface
st.subheader("Time Available")

# Display a slider for time selection
selected_time = st.slider("Select Time(min):", 0, 240, step=5, value=(0, 240))
st.write(selected_time)

##############################RESTRICTIONS#######################################


st.title("Restrictions 🙅‍♂️")

# Define your list of preferences
preferences = ["gluten free", "vegan", "vegetarian", "light", "healthy"]

selected_preferences = st.multiselect("Select Elements", preferences)

# Show the selected elements
st.write("Selected Preferences:", selected_preferences)


'''

st.header('WELCOME TO RECEIPT GENERATOR')
st.subheader('Find recipes that suits you based on: the ingredients you have, your allergies, time available and, HOW YOU ARE FEELING!')

btn = st.button('Press Here to start')
if btn:
   switch_page('ingredients')
