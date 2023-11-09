from abc import ABC, abstractmethod
from motor.motor_asyncio import AsyncIOMotorDatabase


class DatabaseConnection(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    async def get_database(self) -> AsyncIOMotorDatabase:
        pass
