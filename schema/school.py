from pydantic import BaseModel, Field


class SchemaSchool(BaseModel):
    name: str = Field(min_length=2, max_length=30)
