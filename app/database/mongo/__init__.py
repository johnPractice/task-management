from motor.motor_asyncio import AsyncIOMotorClient
from app.utils.interfaces.database_connection import DatabaseConnection
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.settings import MONGO_URI, MONGO_DB_NAME


class MongoDBConnection(DatabaseConnection):
    def __init__(
        self, mongo_uri: str = MONGO_URI, db_name: str = MONGO_DB_NAME, **kwargs
    ):
        self.mongo_uri = mongo_uri
        self.db_name = db_name

    async def get_database(self) -> AsyncIOMotorDatabase:
        try:
            client = AsyncIOMotorClient(self.mongo_uri)
            db = client[self.db_name]
            return db
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            raise e
