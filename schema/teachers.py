from pydantic import BaseModel, Field


class SchemaTeacher(BaseModel):
    name: str = Field(min_length=2, max_length=30)
    science: str = Field(min_length=2, max_length=40)
