
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from services.predict_service import prediction
from services.data_service import *
from schema.transaction_input import TransactionInput
from model.predict import predict_output, ensemble, MODEL_VERSION

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def home(skip: int = 0, limit: int = 20, status: str = None):
    return get_data(skip,limit,status)

@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': ensemble is not None
    }

@app.get("/total")
def all():
    return total()

@app.get("/amount-per-hour")
def amount():
    return amount_per_hour()

@app.get("/amount-per-status")
def amountStatus():
    return amount_per_status()

@app.get("/predict_incremental")
def predict_incremental_api():
    df = prediction()
    if df is None or df.empty:
        return {"message": "Không có dữ liệu mới", "new_rows": 0}
    return {
        "message": "Prediction completed",
        "new_rows": len(df)
    }

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)  

    df.to_sql("transactions", con=engine, if_exists="append", index=False)

    prediction()

    return True
