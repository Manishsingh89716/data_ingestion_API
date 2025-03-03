🚀 Approach & Assumptions

🔹 Approach:

1. Multi-source ingestion: Collects structured (SQL, CSV, Excel) & unstructured (JSON, PDFs, Text) data.
2. Real-time processing: FastAPI handles uploads instantly, processing data as it arrives.
3. Storage optimization: SQLite is used for lightweight, structured storage to simplify deployment.
4. API-first design: Exposes RESTful endpoints (/ingest) for seamless integration.
5. Scalability-ready: Uses modular ingestion logic, making it easy to swap SQLite with Neo4j if needed.

🔹 Assumptions:

1. The focus is on data ingestion, not complex relationship queries.
2. SQLite is used instead of Neo4j to keep the solution lightweight for a hiring task.
3. The ingestion module handles diverse file formats without requiring pre-cleaning.
4. The system stores raw data for future analysis without immediate transformation.

🔹 How to run:
1. Clone the repository:- git clone https://github.com/Manishsingh89716/data_ingestion_API
2. cd data_ingestion_API
3. Install dependencies:- pip install -r requirements.txt
4. Run the application:- uvicorn app.main:app --reload
5. Swagger:- http://127.0.0.1:8000/docs
