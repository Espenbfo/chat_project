from pathlib import Path

import whisper
import time
class WhisperModel():
    def __init__(self):
        self.model = whisper.load_model("medium")
        print("Model loaded")

    def parse(self, filename: str | Path = "audio.m4a"):
        print("transcribing", filename)
        return self.model.transcribe(filename)

if __name__ == "__main__":
    st = time.time()
    model = WhisperModel()
    print("starting parsing")
    print(model.parse())
    print(f"finished parsing in {time.time()-st} seconds")