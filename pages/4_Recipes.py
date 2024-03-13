import streamlit as st
from amerigo_py_files.amerigo_functions import *
from model.main import main

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

import os

parent_dir = os.getcwd()
filepath = os.path.join(parent_dir, "background", "rsz_output-flat-lay-concept-clipboard.jpg")
set_background(filepath)


final_df, warning = main(ingredient_text= st.session_state.selected_ingredients_text,
                                            user_prompt= st.session_state.user_text,
                                            time= st.session_state.selected_time,
                                            selected_ingredients_list = st.session_state.selected_ingredients_list,
                                            filter_mode= st.session_state.filter_mode)

if len(final_df) == 0:
    st.write("Sorry, we couldn't indentify recipes suited to your request")
else:
    st.markdown(" ")  # Adds a space
    st.markdown(" ")  # Adds a space
    st.markdown(" ")  # Adds a space
    st.header('Here are our suggested recipes!')
    st.markdown(" ")  # Adds a space
    st.markdown(warning)
    st.markdown(" ")  # Adds a space

    # for i in range(len(final_df)):
    #     st.markdown(f'{i+1}) <a href="{final_df["recipe_link"][i]}">{final_df["recipe_name"][i]}</a>: <span style="padding-left: 20px;">{final_df["avg_rating"][i]:.1f} ⭐ ({final_df["nb_reviews"][i]})</span>', unsafe_allow_html=True)
    #     st.markdown(f'<span style="padding-left: 20px;">Present Ingredients: {final_df["perc_ingre"][i]*100:.0f}%</span>', unsafe_allow_html=True)


    #     # Get the color based on the rating
    #     if final_df["similarity_score"][i] < 0.35:
    #         color = "green"
    #     elif final_df["similarity_score"][i] < 0.40:
    #         color = "orange"
    #     else:
    #         color = "red"

    #     # Display the rating with the corresponding color
    #     # Using a circle (●) to represent the rating visually
    #     st.markdown(f"<span style=\"padding-left: 20px;\">Feeling's affinity: <span style=\"color: {color}; font-size: 30px;\">●</span>", unsafe_allow_html=True)
    #     if final_df["time_ok"][i] == "yes":
    #         st.markdown(f'<span style="padding-left: 20px;">Time: <span style="color: green; font-size: 30px;">✓</span>', unsafe_allow_html=True)
    #     else:
    #         st.markdown(f'<span style="padding-left: 20px;">Time: <span style="color: red; font-size: 30px;">✗</span>', unsafe_allow_html=True)

    for i in range(len(final_df)):
        # Get the color based on the rating
        if final_df["similarity_score"][i] < 0.35:
            color = "green"
        elif final_df["similarity_score"][i] < 0.40:
            color = "orange"
        else:
            color = "red"

        # Time check
        time_color = "green" if final_df["time_ok"][i] == "yes" else "red"
        time_symbol = "✓" if final_df["time_ok"][i] == "yes" else "✗"

        # Combine everything into one markdown call
        st.markdown(f'''
            <div style="margin-bottom: 10px;">
                {i+1}) <a href="{final_df["recipe_link"][i]}">{final_df["recipe_name"][i]}</a>: <span style="padding-left: 20px;">{final_df["avg_rating"][i]:.1f} ⭐ ({final_df["nb_reviews"][i]})</span>
                <br>
                <span style="padding-left: 20px;">Ingredients: {final_df["perc_ingre"][i]*100:.0f}%</span>
                <span style="padding-left: 20px;">Feeling's affinity: <span style="color: {color}; font-size: 30px;">●</span></span>
                <span style="padding-left: 20px;">Time: <span style="color: {time_color}; font-size: 30px;">{time_symbol}</span></span>
                <br>
            </div>
        ''', unsafe_allow_html=True)

st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space


btn2 = st.button('Restart')

if btn2:
    st.session_state.clear()
    switch_page('Ingredients')
