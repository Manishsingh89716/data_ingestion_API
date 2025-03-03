import pandas as pd
import json
import PyPDF2
from app.database import SessionLocal, IngestedData

#ingest CSV or Excel file
def ingest_csv_excel(file_path):
    df = pd.read_csv(file_path) if file_path.endswith(".csv") else pd.read_excel(file_path)
    db = SessionLocal()
    for _, row in df.iterrows():
        record = IngestedData(file_name=file_path, content=str(row.to_dict()))
        db.add(record)
    db.commit()
    db.close()
    return f"CSV/Excel {file_path} ingested successfully."

#ingest JSON file
def ingest_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    db = SessionLocal()
    record = IngestedData(file_name=file_path, content=json.dumps(data))
    db.add(record)
    db.commit()
    db.close()
    return f"JSON {file_path} ingested successfully."

#ingest PDF (Extracts text) file
def ingest_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    db = SessionLocal()
    record = IngestedData(file_name=file_path, content=text)
    db.add(record)
    db.commit()
    db.close()
    return f"PDF {file_path} ingested successfully."

#ingest Text files
def ingest_text(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    db = SessionLocal()
    record = IngestedData(file_name=file_path, content=text)
    db.add(record)
    db.commit()
    db.close()
    return f"Text file {file_path} ingested successfully."