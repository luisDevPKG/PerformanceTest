import os
from dotenv import load_dotenv

load_dotenv()
# Globals variables
HOST = os.getenv("TARGET_HOST", "https://jsonplaceholder.typicode.com")