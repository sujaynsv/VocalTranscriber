import pyttsx3
import speech_recognition as sr
import pyfiglet
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def banner():
    """Displays a fancy ASCII banner."""
    print("\033[1;32m")  # Green color
    print(pyfiglet.figlet_format("Voice Assistant"))
    print("\033[0m")  # Reset color

def get_audio():
    """Captures and processes speech input."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙️ Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("✅ Processing...")

    try:
        text = recognizer.recognize_google(audio).lower()
        print(f"🗣️ You said: \033[1;34m{text}\033[0m")  # Blue color
        speak(f"You said {text}")

        # Check if the user wants to stop
        if text in ["stop", "exit", "quit"]:
            print("\033[1;31m👋 Exiting voice assistant... Goodbye!\033[0m")  # Red color
            speak("Goodbye! Have a nice day!")
            return False  # Signal to stop the loop

    except sr.UnknownValueError:
        print("\033[1;31m❌ Sorry, I couldn't understand that.\033[0m")  # Red color
        speak("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("\033[1;31m🔗 Error connecting to Google API.\033[0m")
        speak("Error connecting to Google API.")

    return True  # Continue listening

def main():
    """Main function to handle continuous speech recognition."""
    banner()
    speak("Welcome to your voice assistant. Say something!")

    while True:
        if not get_audio():
            break  # Exit loop when "stop" or "exit" is detected
        time.sleep(1)  # Short delay before next input

if __name__ == "__main__":
    main()
