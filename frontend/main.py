from gtts import gTTS
import audioop
import pyaudio
import wave
import requests
import pygame.mixer
import time
PASSIVE_THRESHOLD = 2500
ACTIVE_THRESHOLD = 2000
MEMORY = 100
CHUNK = 1024

FILENAME = "input.wav"
url = "http://192.168.2.35:5000"
url = "http://127.0.0.1:5000"

def play_response(response: str):
    tts = gTTS(response, lang="no")
    tts.save("audio.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("audio.mp3")

    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.04)
    pygame.mixer.quit()


def listen():
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    memory = -1
    while True:
        data = stream.read(CHUNK)
        rms_value = audioop.rms(data, 2)
        if memory == -1 and rms_value > PASSIVE_THRESHOLD:
            memory = MEMORY
        elif memory != -1 and rms_value > ACTIVE_THRESHOLD:
            memory = MEMORY
        if memory > 0:
            memory -= 1
            frames.append(data)
        elif memory == 0:
            break
        if (memory != -1):
            print(memory)
        # check level against threshold, you'll have to write getLevel()
    file = wave.open(FILENAME, 'wb')
    file.setnchannels(1)
    file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    file.setframerate(44100)

    # Write and Close the File
    file.writeframes(b''.join(frames))
    file.close()
    p.terminate()
def initialize():
    greet_response = requests.get(url + "/greet")
    return greet_response.json()["id"]

def send(id):
    with open(FILENAME, "rb") as f:
        response = requests.post(url + "/speak",
                                 data={"id": id},
                                 files={"file": f})
    print("query",  response.json()["query"])
    print("response",  response.json()["response"])

    return response.json()["response"]
def main():
    id = initialize()
    while True:
        listen()
        response = send(id)
        if len(response):
            play_response(response)
if __name__ == "__main__":
    main()