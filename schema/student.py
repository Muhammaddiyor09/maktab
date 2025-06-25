from pydantic import BaseModel, Field

class SchemaStudent(BaseModel):
    name: str = Field(min_length=2, max_length=30)
    grade: int = Field(gt=0, lt=12)
    school_id: int
    science: str = Field(min_length=2, max_length=40)


