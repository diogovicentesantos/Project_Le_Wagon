import pickle
import os
from sklearn.cluster import KMeans
import openai
from sklearn.metrics.pairwise import cosine_similarity
from model.params import *
import numpy as np
from google.cloud import storage
import io
import subprocess

from st_files_connection import FilesConnection
conn = st.connection('gcs', type=FilesConnection)

ten_embeddings_temp_array_nom = conn.read("recipe-lewagon-madrid-project/ten_embeddings_temp_array_nom.csv", input_format="csv", ttl=600)


def load_model():
  """Loads the KMeans model from the 'model' folder."""
  parent_dir = os.getcwd()
  filepath = os.path.join(parent_dir,'model', "local_model.pkl")
  with open(filepath, "rb") as f:
      model = pickle.load(f)
  return model


# def load_model():
#     #try:
#     model_data = subprocess.check_output(["gsutil", "cat", "gs://bucket-for-testing-madrid/km_model_OpenAi.pkl"])
#     with io.BytesIO(model_data) as f:
#         loaded_model = pickle.load(f)

#         # if loaded_model is None:

#     return loaded_model


    #except Exception as e:
    #    print(f"Error loading model: {e}")
    #    return None


# def load_model():
#     '''Load the fited kmeans cluster model'''

#     if LOAD_MODEL == "gcp":
    #     # Specify your bucket name and file name
    #     bucket_name = BUCKET_NAME
    #     blob_name = 'km_model_OpenAi.pkl'

    #     # Initialize the client
    #     client = storage.Client()

    #     # Get the bucket and blob
    #     bucket = client.get_bucket(bucket_name)
    #     blob = bucket.blob(blob_name)

    #     # Download the blob to an in-memory file
    #     in_memory_file = io.BytesIO()
    #     blob.download_to_file(in_memory_file)
    #     in_memory_file.seek(0)  # Important: move back to the start of the file before reading

        # Load the model directly from the in-memory file
    #     model = pickle.loads(conn._instance.download("gs://bucket-for-testing-madrid/km_model_OpenAi.pkl"))#pickle.load(in_memory_file)

    # else:
    #     parent_dir = os.getcwd()
    #     filepath = os.path.join(parent_dir, "raw_data", "km_model_OpenAi.pkl")
    #     model = pickle.load(open(filepath,"rb"))

    # return model


def get_embedding(ingredients_text):
    '''Get embedding of the ingredients text'''
    openai_model = "text-embedding-ada-002"
    openai.api_key = OPENAI_KEY
    igre_embedding = openai.embeddings.create(input = ingredients_text, model = openai_model)

    return np.array(igre_embedding.data[0].embedding)


# def get_cosine(igre_embedding):
#     ''' Get cosine matrix vs. trained embeddings'''

#     if LOAD_MODEL == "gcp":
#         # Specify your bucket name and file name
#         # bucket_name = BUCKET_NAME
#         # blob_name = 'ten_embeddings_temp_array_nom.pkl'

#         # # Initialize the client
#         # client = storage.Client()

#         # # Get the bucket and blob
#         # bucket = client.get_bucket(bucket_name)
#         # blob = bucket.blob(blob_name)

#         # # Download the blob to an in-memory file
#         # in_memory_file = io.BytesIO()
#         # blob.download_to_file(in_memory_file)
#         # in_memory_file.seek(0)  # Important: move back to the start of the file before reading

#         # Load the model directly from the in-memory file
#         # dataset_embeddings_10 = pickle.load(in_memory_file)
#         ten_embed = subprocess.check_output(["gsutil", "cat", "gs://bucket-for-testing-madrid/ten_embeddings_temp_array_nom.pkl"])
#         with io.BytesIO(ten_embed) as f:
#             dataset_embeddings_10 = pickle.load(f)
#         print(len(dataset_embeddings_10))

#     else:
#         parent_dir = os.getcwd()
#         filepath = os.path.join(parent_dir, "raw_data", "ten_embeddings_temp_array_nom.pkl")
#         dataset_embeddings_10 = pickle.load(open(filepath,"rb"))

#     ingre_embedding_reshapped = igre_embedding.reshape(1, 1536)
#     print(len(ingre_embedding_reshapped))
#     cos_sim_ingre_embed = cosine_similarity(ingre_embedding_reshapped, dataset_embeddings_10)
#     print(len(cos_sim_ingre_embed))

#     return cos_sim_ingre_embed



def get_cosine(igre_embedding):
    if LOAD_MODEL == "gcp":
        # bucket_name = BUCKET_NAME
        # blob_name = 'ten_embeddings_temp_array_nom.pkl'

        # try:
            # Initialize the client
            # client = storage.Client()

            # Get the bucket and blob
            # bucket = client.get_bucket(bucket_name)
            # blob = bucket.blob(blob_name)

            # Download the blob to an in-memory file (optional)
            # in_memory_file = io.BytesIO()
            # blob.download_to_file(in_memory_file)
            # in_memory_file.seek(0)  # Important: move back to the start of the file

            # Load the model directly from the downloaded blob (preferred)
            dataset_embeddings_10 = ten_embeddings_temp_array_nom#pickle.loads(blob.download_as_string())
            return dataset_embeddings_10
        # except Exception as e:
        #     print(f"Error loading embeddings from GCS: {e}")
        #     return None
    else:
        parent_dir = os.getcwd()
        filepath = os.path.join(parent_dir, "raw_data", "ten_embeddings_temp_array_nom.pkl")
        dataset_embeddings_10 = pickle.load(open(filepath,"rb"))
    ingre_embedding_reshapped = igre_embedding.reshape(1, 1536)
    cos_sim_ingre_embed = cosine_similarity(ingre_embedding_reshapped, dataset_embeddings_10)

    return cos_sim_ingre_embed






# def get_cosine(igre_embedding):
#     ''' Get cosine matrix vs. trained embeddings'''

#     if LOAD_MODEL == "gcp":
#         # # Specify your bucket name and file name
#         bucket_name = BUCKET_NAME
#         blob_name = 'ten_embeddings_temp_array_nom.pkl'

#         # # Initialize the client
#         client = storage.Client()

#         # # Get the bucket and blob
#         bucket = client.get_bucket(bucket_name)
#         blob = bucket.blob(blob_name)

#         # # Download the blob to an in-memory file
#         in_memory_file = io.BytesIO()
#         blob.download_to_file(in_memory_file)
#         in_memory_file.seek(0)  # Important: move back to the start of the file before reading

#         # Load the model directly from the in-memory file
#         dataset_embeddings_10 = pickle.loads(conn._instance.download("gs://bucket-for-testing-madrid/ten_embeddings_temp_array_nom.pkl"))#pickle.load(in_memory_file)

#     else:
#         parent_dir = os.getcwd()
#         filepath = os.path.join(parent_dir, "raw_data", "ten_embeddings_temp_array_nom.pkl")
#         dataset_embeddings_10 = pickle.load(open(filepath,"rb"))

#     ingre_embedding_reshapped = igre_embedding.reshape(1, 1536)
#     cos_sim_ingre_embed = cosine_similarity(ingre_embedding_reshapped, dataset_embeddings_10)

#     return cos_sim_ingre_embed


def get_cluster(ingredients_text):
    '''Get Cluster based on ingredients'''

    #Load Model
    model = load_model()

    # Get embedding of the ingredients text
    ingre_embedding = get_embedding(ingredients_text)

    # Get cosine matrix vs. trained embeddings
    cos_sim_ingre_embed = get_cosine(ingre_embedding)

    # Get clusters
    cluster_label = model.predict(cos_sim_ingre_embed)

    print("\n✅ get_cluster() done \n")
    print(f"Cluster label for ingredients '{ingredients_text}' is {cluster_label[0]}\n")

    return cluster_label[0]
