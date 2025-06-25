from fastapi import FastAPI
from router.school import school_router
from router.student import student_router
from router.teachers import teacher_router


app = FastAPI(docs_url="/")


app.include_router(school_router, tags=["school"])
app.include_router(student_router, tags=["student"])
app.include_router(teacher_router, tags=["teacher"])
