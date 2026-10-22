import os
import pprint
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
load_dotenv()
os.getenv("OPENROUTER_API_KEY")

model = init_chat_model(
    "nvidia/nemotron-3-ultra-550b-a55b:free",
    model_provider="openrouter",
)
response = model.invoke("can you code?")

print(response.response_metadata['model_name'])
