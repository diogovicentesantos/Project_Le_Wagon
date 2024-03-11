import os
from dotenv import load_dotenv
load_dotenv()

LOAD_MODEL = os.environ.get("LOAD_MODEL")
OPENAI_KEY = os.environ.get("OPENAI_KEY")
LANGCHAIN_CLOSEST_DOCS = int(os.environ.get("LANGCHAIN_CLOSEST_DOCS"))
BUCKET_NAME = os.environ.get("BUCKET_NAME")
