from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import Config

# Database setup
engine = create_engine(Config.SQL_DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

#define table schema
class IngestedData(Base):
    __tablename__ = "ingested_data"
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, index=True)
    content = Column(Text)

#create tables
Base.metadata.create_all(engine)