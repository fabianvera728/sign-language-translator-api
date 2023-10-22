from fastapi import FastAPI
from src.apps.audio_transcriber.router import websocket_router

app = FastAPI()

@app.get("/health-check", description="Health check endpoint")
async def root():
    return {"status": "ok", "message": "Server is up and running"}


app.include_router(websocket_router)