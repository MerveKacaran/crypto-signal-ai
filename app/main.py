from fastapi import FastAPI

app = FastAPI(
    title="Crypto Signal AI",
    version="1.0.0",
    description="AI Destekli BTCTürk Teknik Analiz Platformu"
)

@app.get("/")
def root():
    return {
        "project": "Crypto Signal AI",
        "status": "running",
        "version": "1.0.0"
    }
