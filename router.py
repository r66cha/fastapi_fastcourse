from typing import Annotated
from fastapi import APIRouter, Depends

from schemas import STaskAdd, STaskID
from repository import TaskRepository

router = APIRouter(prefix="/tasks", tags=["Таски"])
lst_tasks = []


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()]
) -> STaskID:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


print(lst_tasks)


@router.get("")
async def get_tasks() -> list[STaskAdd]:
    tasks = await TaskRepository.find_all()
    return tasks
