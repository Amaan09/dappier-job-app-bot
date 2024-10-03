import os
from langchain_openai import ChatOpenAI

model = os.environ.get("OPENAI_MODEL")

if not model:
    raise ValueError("OPENAI_MODEL is not set in the environment variables.")

openai_model = ChatOpenAI(model=model, temperature=1)
