from sqlalchemy.orm import Session
from shared.models import Task
from shared.enums import TaskStatus

def create_task(db: Session, task_type: str):
    task = Task(type=task_type, status=TaskStatus.PENDING.value)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()
