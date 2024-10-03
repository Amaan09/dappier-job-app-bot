import os
from pinecone import Pinecone

api_key = os.environ.get("PINECONE_API_KEY")
resume_index_name = os.environ.get("RESUME_INDEX_NAME")

if not resume_index_name:
    raise ValueError("RESUME_INDEX_NAME is not set in the environment variables.")

pc = Pinecone(api_key=api_key)

resume_index = pc.Index(resume_index_name)
