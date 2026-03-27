# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.data import router as data_router  
from app.api.predict import router as pre_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data_router, prefix="/api/data")
app.include_router(pre_router, prefix="/api/pre")