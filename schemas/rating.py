from datetime import datetime

from pydantic import BaseModel, Field

class RatingCreate(BaseModel):
    user_id: int
    lesson_id: int
    stars: int = Field(..., gt=0, le=5)


class RatingOut(BaseModel):
    id: int
    user_id: int
    lesson_id: int
    stars: int = Field(..., gt=0, le=5)

    class Config:
        orm_mode = True

class CommentCreate(BaseModel):
    user_id: int
    lesson_id: int
    text: str
    created_at: datetime

class CommentOut(BaseModel):
    id: int
    user_id: int
    lesson_id: int
    text: str
    created_at: datetime

    class Config:
        orm_mode = True