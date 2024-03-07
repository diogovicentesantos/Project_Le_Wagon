import pickle
import os
from sklearn.cluster import KMeans
import openai
from sklearn.metrics.pairwise import cosine_similarity
from params import *


def load_model():
    '''Load the fited kmeans cluster model'''

    if LOAD_MODEL == "gcp":
        ## add the part to load from Google Cloud
        pass
    else:
        parent_dir = os.path.dirname(os.getcwd())
        filepath = os.path.join(parent_dir, "raw_data", "km_model_OpenAi.pkl")
        model = pickle.load(open(filepath,"rb"))

    return model


def get_embedding(ingredients_text):
    '''Get embedding of the ingredients text'''
    model = "text-embedding-ada-002"
    igre_embedding = openai.Embedding.create(input = ingredients_text, model = model)

    return igre_embedding


def get_cosine(igre_embedding):
    ''' Get cosine matrix vs. trained embeddings'''

    if LOAD_MODEL == "gcp":
        ## add the part to load from Google Cloud
        pass
    else:
        parent_dir = os.path.dirname(os.path.dirname(os.getcwd()))
        filepath = os.path.join(parent_dir, "raw_data", "dataset_embeddings_10.pkl")
        dataset_embeddings_10 = pickle.load(open(filepath,"rb"))

    #### do i need to reshape igre_embedding ??? ########
    cos_sim_ingre_embed = cosine_similarity(igre_embedding, dataset_embeddings_10)

    return cos_sim_ingre_embed


def get_cluster(ingredients_text):
    '''Get Cluster based on ingredients'''

    #Load Model
    model = load_model()

    # Get embedding of the ingredients text
    ingre_embedding = get_embedding(ingredients_text)

    # Get cosine matrix vs. trained embeddings
    cos_sim_ingre_embed = get_cosine(ingre_embedding)

    # Get clusters
    #### result might be an array, to be changed ########
    cluster_label = model.predict(cos_sim_ingre_embed)

    return cluster_label
