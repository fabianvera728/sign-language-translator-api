import uuid
import os
from fastapi import WebSocket
from src.contexts.transcriber.application.audio_transcriber import AudioTranscriber

class AudioTranscriberWebSocket():
    
    def __init__(self, websocket: WebSocket):
        self.websocket = websocket
        self.audio_transcriber = AudioTranscriber()

    async def run(self):
        await self.websocket.accept()
        await self.__listen_messages()

    async def __listen_messages(self):
        while True:
            data_bytes = await self.websocket.receive_bytes()
            filename = str(uuid.uuid4()) + ".mp4"        
            file = open(filename, "wb")
            file.write(data_bytes)
            result = self.audio_transcriber.transcribe(filename)
            file.close()
            os.remove(filename)
            await self.websocket.send_text(f"Message text was: {result}")