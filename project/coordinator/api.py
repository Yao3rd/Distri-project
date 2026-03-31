from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from shared.database import SessionLocal, engine
from shared import models
from shared.schemas import TaskCreate, TaskResponse
from coordinator.task_service import create_task, get_task
from coordinator.scheduler import select_worker
from coordinator.worker_registry import get_workers

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks", response_model=TaskResponse)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task.type)
    workers = get_workers()
    worker = select_worker(task.type, workers)

    if worker:
        print(f"Assigned to worker {worker['id']}")

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    return get_task(db, task_id)
