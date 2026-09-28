from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session
from typing import List


task_routes = APIRouter(prefix="/tasks")


@task_routes.post("/create", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema, db :Session = Depends(get_db)):
    return controller.create_task(body, db)

@task_routes.get("/all-tasks", response_model=List[TaskResponseSchema], status_code=status.HTTP_200_OK)
def get_all_tasks(db:Session = Depends(get_db)):
    return controller.get_all_tasks(db)

@task_routes.get("/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
def get_one_task(task_id:int, db:Session = Depends(get_db)):
    return controller.get_one_task(task_id, db)

@task_routes.put("/update/{task_id}", status_code=status.HTTP_200_OK)
def update_task(body:TaskSchema, task_id:int, db:Session = Depends(get_db)):
    return controller.update_task(body, task_id, db)

@task_routes.delete("/delete/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id:int, db:Session = Depends(get_db)):
    return controller.delete_task(task_id, db)

