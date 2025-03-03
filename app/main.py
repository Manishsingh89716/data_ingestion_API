from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Multi-Source Data Ingestion (SQLite)")
app.include_router(router)