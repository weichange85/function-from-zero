from fastapi import FastAPI, HTTPException
from app.wikipedia_service import get_summary

app = FastAPI(title="Wikipedia Summary API")

@app.get("/summary/{topic}")
def read_summary(topic: str):
    try:
        summary = get_summary(topic)
        return {"topic": topic, "summary": summary}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
