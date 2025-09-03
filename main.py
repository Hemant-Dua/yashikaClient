import requests
from tts import yashika_speak

ip = input("Enter the Server IP : ")
BASE_URL = "http://"+ ip +":7860"  # change to your laptop's IP

def ask_yashika(message):
    resp = requests.post(f"{BASE_URL}/chat", json={"message": message}, stream=True)
    resp.raise_for_status()
    return "".join(chunk.decode() for chunk in resp.iter_content(chunk_size=None))

if __name__ == "__main__":
    while True:
        msg = input("You: ")
        reply = ask_yashika(msg)
        print("Yashika:", reply)
        yashika_speak(reply)

