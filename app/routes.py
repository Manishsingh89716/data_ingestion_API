import os
from fastapi import APIRouter, UploadFile, File
from app.ingestion import ingest_csv_excel, ingest_json, ingest_pdf, ingest_text

router = APIRouter()

TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

#to post csv/excel file

@router.post("/ingest/csv-excel")
async def upload_csv_excel(file: UploadFile = File(...)):
    path = os.path.join(TEMP_DIR, file.filename)
    with open(path, "wb") as f:
        f.write(file.file.read())
    return {"message": ingest_csv_excel(path)}

#to post json file

@router.post("/ingest/json")
async def upload_json(file: UploadFile = File(...)):
    path = os.path.join(TEMP_DIR, file.filename)
    with open(path, "wb") as f:
        f.write(file.file.read())
    return {"message": ingest_json(path)}

#to post pdf files

@router.post("/ingest/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    path = os.path.join(TEMP_DIR, file.filename)
    with open(path, "wb") as f:
        f.write(file.file.read())
    return {"message": ingest_pdf(path)}

#to post text files

@router.post("/ingest/text")
async def upload_text(file: UploadFile = File(...)):
    path = os.path.join(TEMP_DIR, file.filename)
    with open(path, "wb") as f:
        f.write(file.file.read())
    return {"message": ingest_text(path)}