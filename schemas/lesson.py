from sqlalchemy import String
from pydantic import BaseModel
from sqlalchemy import Column


class LessonCreate(BaseModel):
    course_id: int
    title: str
    video_url: str
    content: str

class LessonOut(BaseModel):
    id: int
    course_id: int
    title: str
    video_url: str
    content: str

    class Config:
        orm_mode = True