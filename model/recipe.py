import numpy as np
import pandas as pd
import ast
import os
import pickle
from model.params import *
from google.cloud import storage
import io

from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document

from st_files_connection import FilesConnection
conn = st.connection('gcs', type=FilesConnection)
preprocessed_data = conn.read("recipe-lewagon-madrid-project/preprocessed_data.csv", input_format="csv", ttl=600)
preprocessed_data_with_ingredients = conn.read("recipe-lewagon-madrid-project/preprocessed_dataset_with_ingredients.csv", input_format="csv", ttl=600)




def load_preprocessed_dataset():
    '''Load the preprocessed dataset'''

    if LOAD_MODEL == "gcp":
        # # Specify your bucket name and file name
        # bucket_name = BUCKET_NAME
        # blob_name = 'preprocessed_data.pkl'

        # # Initialize the client
        # client = storage.Client()

        # # Get the bucket and blob
        # bucket = client.get_bucket(bucket_name)
        # blob = bucket.blob(blob_name)

        # # Download the blob to an in-memory file
        # in_memory_file = io.BytesIO()
        # blob.download_to_file(in_memory_file)
        # in_memory_file.seek(0)  # Important: move back to the start of the file before reading

        # Load the model directly from the in-memory file
        preprocessed_dataset = preprocessed_data#conn.load_file("gs://bucket-for-testing-madrid/preprocessed_data.pkl")#pickle.load(in_memory_file)

    else:
        parent_dir = os.getcwd()
        filepath = os.path.join(parent_dir, "raw_data", "preprocessed_data.pkl")
        preprocessed_dataset = pickle.load(open(filepath,"rb"))

    print("\n✅ preprocessed_dataset loaded \n")

    return preprocessed_dataset


def load_preprocessed_dataset_with_ingredients():
    '''Load the preprocessed dataset with ingredients'''

    if LOAD_MODEL == "gcp":
        # # Specify your bucket name and file name
        # bucket_name = BUCKET_NAME
        # blob_name = 'preprocessed_data_with_ingredients.pkl'

        # # Initialize the client
        # client = storage.Client()

        # # Get the bucket and blob
        # bucket = client.get_bucket(bucket_name)
        # blob = bucket.blob(blob_name)

        # # Download the blob to an in-memory file
        # in_memory_file = io.BytesIO()
        # blob.download_to_file(in_memory_file)
        # in_memory_file.seek(0)  # Important: move back to the start of the file before reading

        # # Load the model directly from the in-memory file
        preprocessed_dataset_with_ingredients = preprocessed_data_with_ingredients#conn.load_file("gs://bucket-for-testing-madrid/preprocessed_data_with_ingredients.pkl")#pickle.load(in_memory_file)

    else:
        parent_dir = os.getcwd()
        filepath = os.path.join(parent_dir, "raw_data", "preprocessed_data_with_ingredients.pkl")
        preprocessed_dataset_with_ingredients = pickle.load(open(filepath,"rb"))

    print("\n✅ preprocessed_dataset_with_ingredients loaded \n")

    return preprocessed_dataset_with_ingredients



def get_selected_recipe_link_list(cluster_label, query, ingredient_list = [], filter_mode =""):

    warning = ""
    ingredient_list = [item.lower() for item in ingredient_list]

    if filter_mode != "":
        WITH_FILTER = filter_mode

    print("You are in mode: "+ WITH_FILTER)

    if WITH_FILTER == "filter_only":
        preprocessed_dataset = load_preprocessed_dataset_with_ingredients()

        selected_data = preprocessed_dataset
        for ingredient in ingredient_list:
            selected_data = selected_data.loc[selected_data['ingredients'].str.contains(ingredient)]
            print("Filtering this ingredient: "+ ingredient+". Nb left: "+str(len(selected_data)))

        print("Number of recipes selected via filter: "+str(len(selected_data))+" (it will be capped at 6600)")
        selected_data = selected_data.iloc[:6600]

        if len(selected_data) == 0:
            warning = "No recipe matches your combination of ingredients, we selected recipes that had close ingredients"
            print(warning)
            selected_data = preprocessed_dataset[preprocessed_dataset["cluster_label"]==cluster_label]
            print("Number of recipes selected via cluster: "+ str(len(selected_data)))

    elif WITH_FILTER == "cluster_filter":
        preprocessed_dataset = load_preprocessed_dataset_with_ingredients()
        selected_data = preprocessed_dataset[preprocessed_dataset["cluster_label"]==cluster_label]
        print("Number of recipes selected via cluster: "+ str(len(selected_data)))

        for ingredient in ingredient_list:
            selected_data = selected_data.loc[selected_data['ingredients'].str.contains(ingredient)]
            print("Filtering this ingredient: "+ ingredient+". Nb left: "+str(len(selected_data)))

        print("Number of recipes selected after filter: "+str(len(selected_data))+" (it will be capped at 6600)")
        selected_data = selected_data.iloc[:6600]

        if len(selected_data) == 0:
            warning = "No recipe matches your combination of ingredients, we selected recipes that had close ingredients"
            print(warning)
            selected_data = preprocessed_dataset[preprocessed_dataset["cluster_label"]==cluster_label]
            print("Number of recipes selected via cluster: "+ str(len(selected_data)))

    else:
        preprocessed_dataset = load_preprocessed_dataset()
        selected_data = preprocessed_dataset[preprocessed_dataset["cluster_label"]==cluster_label]
        print("Number of recipes selected via cluster: "+ str(len(selected_data)))


    nb_recipe_selected = len(selected_data)
    print("Number of recipes selected: "+ str(nb_recipe_selected))

    if nb_recipe_selected > 0:
        ## Create langchain list of documents

        docs = []
        for row in range(len(selected_data)):
            docs.append(Document(page_content=selected_data["final_text"].iloc[row], metadata={"source": "local"}))

        ## Set up Chroma vector
        vector_db = Chroma.from_documents(docs,
                                        OpenAIEmbeddings(openai_api_key = OPENAI_KEY,
                                                        model="text-embedding-ada-002"))

        # Querying the data
        total_query = "Can you find the recipe the most adapted to a person that indicated me: "+query

        selected_docs = vector_db.similarity_search(total_query, k = min(LANGCHAIN_CLOSEST_DOCS,nb_recipe_selected))
        print("Number of selected docs in Langchain: "+ str(len(selected_docs)))

        recipe_link_list = []
        name_list = []
        for item in selected_docs:
            search_string = item.page_content
            try:
                filtered_df = selected_data.loc[selected_data['final_text'].str.contains(search_string)]
                recipe_link_list.append(filtered_df["link"].tolist())
                name_list.append(filtered_df["name"].tolist())
            except:
                pass


        name_list = [item for sublist in name_list for item in sublist]
        recipe_link_list = [item for sublist in recipe_link_list for item in sublist]
        print("Number of matched docs between Langchain selection & original data: "+ str(len(name_list)))

    else:
        name_list = []
        recipe_link_list = []

    print("\n✅ name_list is \n")
    print(name_list)

    return name_list, recipe_link_list, warning
