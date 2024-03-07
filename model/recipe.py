import numpy as np
import pandas as pd
import ast
import os
import pickle
from params import *

from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document

def load_preprocessed_dataset():
    '''Load the preprocessed dataset'''

    if LOAD_MODEL == "gcp":
        ## add the part to load from Google Cloud
        pass
    else:
        parent_dir = os.path.dirname(os.getcwd())
        filepath = os.path.join(parent_dir, "raw_data", "preprocessed_dataset.pkl")
        preprocessed_dataset = pickle.load(open(filepath,"rb"))

    return preprocessed_dataset


def get_selected_recipe_link_list(cluster_label, query):

    preprocessed_dataset = load_preprocessed_dataset()

    selected_data = preprocessed_dataset[preprocessed_dataset["cluster_label"]==cluster_label]
    #"final_text"
    #"cluster_label"
    #"recipe_id"
    # "link"
    nb_recipe_in_cluster = len(selected_data)

    if nb_recipe_in_cluster > 0:
        ## Create langchain list of documents
        docs = []
        for row in range(len(selected_data)):
            docs.append(Document(page_content=selected_data["final_text"].iloc[row], metadata={"source": "local"}))

        ## Set up Chroma vector
        vector_db = Chroma.from_documents(docs,
                                        OpenAIEmbeddings(openai_api_key = OPENAI_KEY,
                                                        model="text-embedding-ada-002"))

        # Querying the data
        selected_docs = vector_db.similarity_search(query, k = min(LANGCHAIN_CLOSEST_DOCS,len()))

        recipe_link_list = []
        for item in selected_docs:
            search_string = item.page_content
            try:
                filtered_df = selected_data.loc[selected_data['final_text'].str.contains(search_string)]
                recipe_link_list.append(filtered_df["link"].tolist())
            except:
                pass

        return recipe_link_list

    else:
        return []
