from os import getenv
from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
PLUGIN = getenv("PLUGIN")