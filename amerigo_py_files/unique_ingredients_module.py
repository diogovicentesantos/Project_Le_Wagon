import pandas as pd
import ast
import string

def remove_punctuation_and_capitalize(word_list):
    # Define a translation table to remove punctuation
    translation_table = str.maketrans('', '', string.punctuation)

    # Remove punctuation and capitalize for each word in the list
    cleaned_words = [word.translate(translation_table).capitalize() for word in word_list]

    return cleaned_words
def get_unique_ingredients():
    df = pd.read_csv('raw_data/RAW_recipes.csv')
    df['ingredients'] = df['ingredients'].apply(ast.literal_eval)

    # Create a set to store unique ingredients
    unique_ingredients = set()

    # Iterate through each row and add ingredients to the set
    for ingredients_list in df['ingredients']:
        unique_ingredients.update(ingredients_list)

    # Take out punctuation from text and capitalize
    unique_ingredients = remove_punctuation_and_capitalize(unique_ingredients)

    return unique_ingredients
