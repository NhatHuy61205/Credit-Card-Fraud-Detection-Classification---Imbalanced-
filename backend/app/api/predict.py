from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import pandas as pd
import joblib
from pathlib import Path

router = APIRouter()

MODEL_PATH = Path(__file__).parent.parent.parent.parent / "artifacts" / "Random_Forest.joblib"
model = joblib.load(MODEL_PATH)

