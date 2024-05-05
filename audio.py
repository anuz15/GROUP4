import speech_recognition as sr

# Function to capture audio and save it to a file
def save_audio_to_file(filename, duration=10):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Open the microphone for audio capture
    with sr.Microphone() as source:
        print("Recording...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Record audio for the specified duration
        audio_data = recognizer.listen(source, timeout=duration)

        # Save the recorded audio to a file
        with open(filename, "wb") as f:
            f.write(audio_data.get_wav_data())

        print(f"Audio saved to {filename}")

if __name__ == "__main__":
    save_audio_to_file("recorded_audio.wav")
