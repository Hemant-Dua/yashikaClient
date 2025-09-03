import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen():
    """Capture speech from mic and return recognized text or error string."""
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎤 Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except sr.UnknownValueError:
        return "[ERROR] Could not understand audio."
    except sr.RequestError as e:
        return f"[ERROR] STT service error: {e}"
