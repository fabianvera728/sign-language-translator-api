from fastapi import APIRouter, WebSocket
from src.apps.audio_transcriber.audio_transcriber_web_socket import AudioTranscriberWebSocket

websocket_router = APIRouter(
  prefix="/ws",
  tags=["websocket"],
  responses={404: {"description": "Not found"}},
)

@websocket_router.websocket("/audio-transcriber")
async def websocket_endpoint(websocket: WebSocket):
    await AudioTranscriberWebSocket(websocket).run()