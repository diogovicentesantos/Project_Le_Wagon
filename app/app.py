import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients


#############################'''BACKGROUND IMAGE'''#######################################

page_bg_img = '''
<style>
body {
background-image: url("background.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)



##################################'''TEXTBOX'''#######################################
st.title("What do u feel like having?🍝 ")
st.subheader('(e.g: Italian food, something cold...)')
# Text input box for the user
user_text = st.text_input("Enter your text:")
st.write('your prompt: ' + user_text) #checking user_text

##################################'''INGREDIENTS'''#######################################

st.title("Ingredients🥬🍎")

# Define your list of elements
elements = get_unique_ingredients()

selected_ingredients = st.multiselect("Select ingredients", elements)

# Show the selected elements
st.write("Selected ingredients:", selected_ingredients)

##################################'''TIME'''#######################################

# Select Time Interface
st.subheader("Time Available")

# Display a slider for time selection
selected_time = st.slider("Select Time(min):", 0, 240, step=5, value=(0, 240))
st.write(selected_time)

##############################'''RESTRICTIONS'''#######################################


st.title("Restrictions 🙅‍♂️")

# Define your list of preferences
preferences = ["gluten free", "vegan", "vegetarian", "light", "healthy"]

selected_preferences = st.multiselect("Select Elements", preferences)

# Show the selected elements
st.write("Selected Preferences:", selected_preferences)


#############################'''BACKGROUND'''###################################


st.markdown(
    """
    <style>
        body
        /* Set background image */
        body::before {
            content: '';
            background-image: url('background.jpg');
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: -1;
            opacity: 0.5; /* Adjust the opacity of the background image */
        }
    </style>
    """,
    unsafe_allow_html=True
)

#if st.button('submit'):
