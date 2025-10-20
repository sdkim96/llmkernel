from pydantic import BaseModel, Field


class Event(BaseModel):
    data: str = Field(
        ...,
        description="Content 의 실제 데이터",
    )