from langchain.llms import Gemini
import toml
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Load the gemini_api_key from the .env file
gemini_api_key = os.getenv("GOOGLE_API_KEY")

llm = Gemini(
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"],
    model="gemini-1.5-turbo",
    api_key=gemini_api_key)

name = llm("What is your name?")
print(name)