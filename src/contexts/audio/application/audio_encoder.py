from base64 import b64encode, b64decode

class AudioEncoder:
    def encode(self, audio_file_path):
        with open(audio_file_path, "rb") as audio_file:
            encoded_string = b64encode(audio_file.read())
        return encoded_string.decode("utf-8")
