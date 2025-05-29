import speech_recognition as sr

def transcribe_audio():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as source
    with sr.Microphone() as source:
        print("Please speak now...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        print("Transcribing audio...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

# Run the transcription tool
if __name__ == "__main__":
    transcribe_audio()
