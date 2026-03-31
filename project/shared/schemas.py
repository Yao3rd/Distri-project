from pydantic import BaseModel

class TaskCreate(BaseModel):
    type: str

class TaskResponse(BaseModel):
    id: int
    type: str
    status: str
    result: str | None

    class Config:
        from_attributes = True
