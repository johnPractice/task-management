import os

ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev").lower()
if ENVIRONMENT == "prod":
    from .production import *
elif ENVIRONMENT == "stag":
    from .staging import *
else:
    from .dev import *


MONGO_URI = f"mongodb://{MONGO_USER_NAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"
# Checking essentail env variables
assert MONGO_HOST is not None, "MONGO_HOST bust be defined"
assert MONGO_USER_NAME is not None, "MONGO_USER_NAME bust be defined"
assert MONGO_PASSWORD is not None, "MONGO_PASSWORD bust be defined"
assert MONGO_DB_NAME is not None, "MONGO_DB_NAME bust be defined"
