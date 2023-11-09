from fastapi import Request, APIRouter, HTTPException, Depends, Query
from app.models.task import TaskCreate, Task
from app.database.mongo.task import get_task_repository
from app.utils.interfaces.task_model_query import TaskRepository
from app.utils.mongo_object_id import checking_mongo_object_id
from app.utils.prepare_search_query import prepare_query_params_for_custome_field


task_router = APIRouter(
    prefix="/task",
)


@task_router.post("/", response_model=Task)
async def create_task(
    task: TaskCreate, task_repo: TaskRepository = Depends(get_task_repository)
):
    created_task = await task_repo.create_task(task)
    return created_task


@task_router.get("/{task_id}", response_model=Task)
async def read_task(
    task_id: str, task_repo: TaskRepository = Depends(get_task_repository)
):
    if checking_mongo_object_id(task_id) is False:
        raise HTTPException(status_code=400, detail="Check your input")
    task = await task_repo.get_task(task_id)
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")


@task_router.get("/", response_model=list[Task])
async def list_all_tasks(
    request: Request,
    name: str = Query(None, description="Filter by task name"),
    status: str = Query(None, description="Filter by task status"),
    skip: int = Query(default=0, description="Skip for next step on list"),
    limit: int = Query(default=10, description="Determine the size of list"),
    task_repo: TaskRepository = Depends(get_task_repository),
):
    custome_fields_query = prepare_query_params_for_custome_field(request)
    tasks = await task_repo.list_tasks(name, status, skip, limit, custome_fields_query)
    return tasks


@task_router.put("/{task_id}", response_model=Task)
async def update_existing_task(
    task_id: str,
    task: TaskCreate,
    task_repo: TaskRepository = Depends(get_task_repository),
):
    if checking_mongo_object_id(task_id) is False:
        raise HTTPException(status_code=400, detail="Check your input")
    updated_task = await task_repo.update_task(task_id, task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@task_router.delete("/{task_id}", response_model=Task)
async def delete_existing_task(
    task_id: str, task_repo: TaskRepository = Depends(get_task_repository)
):
    if checking_mongo_object_id(task_id) is False:
        raise HTTPException(status_code=400, detail="Check your input")
    deleted_task = await task_repo.delete_task(task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task
