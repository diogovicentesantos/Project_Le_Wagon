from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from clusters import get_cluster
from recipe import get_selected_recipe_link_list

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/recipe")
def recipe(
        query: str,
        ingredients: str,
    ):

    cluster_label = get_cluster(ingredients)
    url_list = get_selected_recipe_link_list(cluster_label, query)

    my_dict = {
    'url_list': url_list
    }

    return my_dict


@app.get("/")
def root():
    my_dict = {
    'greeting': 'Hello, this is a test'
    }

    return my_dict
