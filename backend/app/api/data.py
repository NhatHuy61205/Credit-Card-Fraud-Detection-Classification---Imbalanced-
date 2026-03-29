# app/api/data.py
from fastapi import APIRouter
from app.services.data_service import *

router = APIRouter()

@router.get("/")
def read_data(skip: int = 0, limit: int = 1000, status: str = None):
    return { "data": get_data(skip, limit, status) }

@router.get("/total")
def all():
    return total()

@router.get("/amount-per-hour")
def amount():
    return amount_per_hour()

@router.get("/amount-per-status")
def amountStatus():
    return amount_per_status()
