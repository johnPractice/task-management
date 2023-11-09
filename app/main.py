from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.settings import API_PREFIX, ORIGINS, DOCS_URL
from app.api import task_router, health_check_router


app = FastAPI(
    docs_url=DOCS_URL,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router, prefix=API_PREFIX, tags=["Task"])
app.include_router(health_check_router, prefix=API_PREFIX, tags=["Health Checking"])
