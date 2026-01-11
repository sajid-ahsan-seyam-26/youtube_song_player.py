import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser

# Initialize recognizer and speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Listen to user voice and convert to text."""
    try:
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"🗣️ You said: {command}")
            return command
    except sr.UnknownValueError:
        talk("Sorry, I didn’t catch that. Please say again.")
        return ""
    except sr.RequestError:
        talk("Network error. Try again later.")
        return ""

def run_youtube_assistant():
    """Run the main assistant loop."""
    talk("Hi! What do you want me to do?")
    while True:
        command = listen_command()

        if 'play' in command:
            song = command.replace('play', '').strip()
            talk(f"Playing {song} on YouTube.")
            print(f"🎬 Searching and playing: {song}")
            pywhatkit.playonyt(song)

        elif 'open youtube' in command:
            talk("Opening YouTube.")
            print("🌐 Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif 'stop' in command or 'exit' in command or 'quit' in command:
            talk("Goodbye! Have a nice day.")
            print("🛑 Exiting assistant.")
            break

        elif command != "":
            talk("Please say 'play' followed by a video name, or say 'open YouTube'.")

if __name__ == "__main__":
    run_youtube_assistant()
