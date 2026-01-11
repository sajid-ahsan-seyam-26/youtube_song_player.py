# youtube_song_player.py
# 🎙️ YouTube Voice Assistant
A Python-based voice-controlled assistant that allows you to search for and play videos on YouTube, open the YouTube website, and interact using voice commands. This project leverages speech recognition and text-to-speech technologies.

# ✨ Features
Voice Recognition: Uses Google Speech Recognition to understand commands.

Text-to-Speech: Responds to user actions with a synthesized voice.

Automated Search: Automatically finds and plays videos on YouTube using pywhatkit.

Ambient Noise Adjustment: Automatically adjusts to room noise for better accuracy.

# 🛠️ Prerequisites & Installation
Before running the assistant, ensure you have Python installed and the necessary libraries.

# 1. Install Dependencies
Run the following command in your terminal:

# Bash

pip install speechrecognition pyttsx3 pywhatkit
2. Audio Driver (Optional)
If you encounter errors with pyttsx3 on Linux, you may need to install espeak:

# Bash

sudo apt-get install espeak
