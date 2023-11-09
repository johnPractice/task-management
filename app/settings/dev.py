import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
# Load env file
## In dev mode can use .env for developing on own localhost
env_path = os.path.join(BASE_DIR, ".env")
load_dotenv(env_path)


API_PREFIX = os.environ.get("API_PREFIX", "/api")
ORIGINS = os.environ.get("ORIGINS", "http://localhost,").split(",")
DOCS_URL = os.environ.get("DOCS_URL", "/docs")
MONGO_USER_NAME = os.environ.get("MONGO_USER_NAME", None)
MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", None)
MONGO_PORT = os.environ.get("MONGO_PORT", "27017")
MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", None)
