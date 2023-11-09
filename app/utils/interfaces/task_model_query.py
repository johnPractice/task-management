from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.task import TaskCreate, Task


class TaskRepository(ABC):
    @abstractmethod
    async def create_task(self, task: TaskCreate) -> Task:
        pass

    @abstractmethod
    async def get_task(self, task_id: str) -> Optional[Task]:
        pass

    @abstractmethod
    async def list_tasks(
        self,
        name: Optional[str],
        status: Optional[str],
        skip: int,
        limit: int,
        custome_filter: dict = dict(),
    ) -> List[Task]:
        pass

    @abstractmethod
    async def update_task(self, task_id: str, task: TaskCreate) -> Optional[Task]:
        pass

    @abstractmethod
    async def delete_task(self, task_id: str) -> Optional[Task]:
        pass
