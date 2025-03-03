🚀 Approach & Assumptions

🔹 Approach:

1️⃣ Multi-source ingestion: Collects structured (SQL, CSV, Excel) & unstructured (JSON, PDFs, Text) data.
2️⃣ Real-time processing: FastAPI handles uploads instantly, processing data as it arrives.
3️⃣ Storage optimization: SQLite is used for lightweight, structured storage to simplify deployment.
4️⃣ API-first design: Exposes RESTful endpoints (/ingest) for seamless integration.
5️⃣ Scalability-ready: Uses modular ingestion logic, making it easy to swap SQLite with Neo4j if needed.

🔹 Assumptions:

✔ The focus is on data ingestion, not complex relationship queries.
✔ SQLite is used instead of Neo4j to keep the solution lightweight for a hiring task.
✔ The ingestion module handles diverse file formats without requiring pre-cleaning.
✔ The system stores raw data for future analysis without immediate transformation.
