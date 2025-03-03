import os

#setup database
class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SQL_DB_URL = f"sqlite:///{os.path.join(BASE_DIR, 'data.db')}"