import whisper
import numpy as np


class AudioTranscriber():

    def __init__(self):
        self.model = whisper.load_model("small")
        print("AudioTranscriber 😀")

    def transcribe(self, filename):
        audio = whisper.load_audio(filename)
        audio = whisper.pad_or_trim(audio)

        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)

        _, probs = self.model.detect_language(mel)
        print(f"Detected language: {max(probs, key=probs.get)}")

        options = whisper.DecodingOptions()
        result = whisper.decode(self.model, mel, options)
        print(result)

        return result.text

