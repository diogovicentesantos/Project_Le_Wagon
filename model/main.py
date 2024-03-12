from model.clusters import get_cluster
from model.recipe import get_selected_recipe_link_list


def main(ingredient_text, user_prompt, selected_ingredients_list=[], filter_mode=""):


    #predict function
    my_clust = get_cluster(ingredient_text)
    name_list, recipe_link_list, warning = get_selected_recipe_link_list(my_clust, user_prompt, selected_ingredients_list, filter_mode)
    print("\n:white_check_mark: Main Executed \n")

    return name_list, recipe_link_list, warning
