import requests

def test_ingestion():
    files = {'file': open("industry.csv", "rb")}
    response = requests.post("http://localhost:8000/ingest/csv-excel", files=files)
    print(response.json())

if __name__ == "__main__":
    test_ingestion()
