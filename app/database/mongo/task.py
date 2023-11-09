from bson import ObjectId
from typing import List, Optional

from app.database.mongo import MongoDBConnection
from app.utils.interfaces.task_model_query import TaskRepository
from app.utils.interfaces.database_connection import DatabaseConnection
from app.models.task import TaskCreate, Task


class MongoTaskRepository(TaskRepository):
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection

    async def create_task(self, task: TaskCreate) -> Task:
        db = await self.db_connection.get_database()
        collection = db["tasks"]
        task_id = await collection.insert_one(task.model_dump())
        created_task = await collection.find_one({"_id": task_id.inserted_id})
        return created_task

    async def get_task(self, task_id: str) -> Optional[Task]:
        db = await self.db_connection.get_database()
        collection = db["tasks"]
        task = await collection.find_one({"_id": ObjectId(task_id)})
        return task

    async def list_tasks(
        self,
        name: str | None,
        status: str | None,
        skip: int,
        limit: int,
        custome_filter: dict = dict(),
    ) -> List[Task]:
        db = await self.db_connection.get_database()
        collection = db["tasks"]
        query = {"custom_fields": custome_filter}
        if name:
            query["name"] = name
        if status:
            query["status"] = status
        tasks = []

        tasks = (
            await collection.find(query).skip(skip).limit(limit).to_list(length=limit)
        )
        return tasks

    async def update_task(self, task_id: str, task: TaskCreate) -> Optional[Task]:
        db = await self.db_connection.get_database()
        collection = db["tasks"]
        existing_task = await collection.find_one({"_id": ObjectId(task_id)})
        if existing_task is None:
            return None
        await collection.update_one(
            {"_id": ObjectId(task_id)}, {"$set": task.model_dump()}
        )
        updated_task = await collection.find_one({"_id": ObjectId(task_id)})
        return updated_task

    async def delete_task(self, task_id: str) -> Optional[Task]:
        db = await self.db_connection.get_database()
        collection = db["tasks"]
        task = await collection.find_one({"_id": ObjectId(task_id)})
        if task is None:
            return None
        await collection.delete_one({"_id": ObjectId(task_id)})
        return task


def get_task_repository():
    _db_connection = MongoDBConnection()
    return MongoTaskRepository(_db_connection)
