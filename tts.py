import re
import subprocess

def clean_for_tts(text):
    # Remove markdown code blocks and inline code
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"`.*?`", "", text)

    # Remove emojis and symbols
    text = re.sub(r"[^\w\s.,!?']", "", text)

    # Collapse extra spaces
    # text = re.sub(r"\s+", " ", text).strip()

    return text

def yashika_speak(text):
    voice = "en+f3"  # female variant
    pitch = "50"
    speed = "140"

    cleaned_text = clean_for_tts(text)

    subprocess.run([
        "espeak-ng",
        "-v", voice,
        "-p", pitch,
        "-s", speed,
        cleaned_text
    ])

if __name__ == "__main__":
    raw_ai_text = "Sure Boss. 😏 Here's the plan:\n```python\nprint('Hello')\n```"
    yashika_speak(raw_ai_text)
