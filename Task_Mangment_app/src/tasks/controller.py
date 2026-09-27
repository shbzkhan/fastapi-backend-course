from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel

def create_task(body:TaskSchema, db:Session):
    data = body.model_dump()
    new_task = TaskModel(title = data["title"], description = data["description"], is_completed = data["is_completed"])
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return{
        "status":"Created Successfully",
        "data": new_task
    }

def get_all_tasks(db:Session):
    all_tasks = db.query(TaskModel).all()
    print(all_tasks)
    return {
        "status":"Tasks fetched successfully",
        "data" : all_tasks
    }