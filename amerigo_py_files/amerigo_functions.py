import streamlit as st
from amerigo_py_files.unique_ingredients_module import get_unique_ingredients

def main_text_storage():
    user_text = st.text_input("Enter your text:")

    return user_text

def select_ingredients_interface():

    # Define your list of elements
    elements = get_unique_ingredients()

    selected_elements = st.multiselect("Select Elements", elements)

    return selected_elements

def select_time():
    # Display a slider for time selection
    selected_time = st.slider("Select Time (in minutes):", 0, 240, step=5, value=(0, 240))

    return selected_time

def preferences():
    """
    Section for preferences with a search box providing customized suggestions.
    """
    st.title("Select restriction🥩🧀")

    preferences = ["gluten free", "vegan", "vegetarian", "light", "healthy"]

    selected_preferences = st.multiselect("Select Elements", preferences)


    return selected_preferences


def background():
    # Set background color
    st.markdown(
        """
        <style>
            body {
                background-color: #f0f2f6; /* Set your desired background color */
            }
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


def save_text(text): #not used for now
    # Here you can implement the logic to save the text to a file or database
    # For demonstration, let's just append it to a text file
    with open("stored_text.txt", "a") as file:
        file.write(text + "\n")
