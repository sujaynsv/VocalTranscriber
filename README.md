# AI Voice Assistant

## 📌 Overview
The *AI Voice Assistant* is a Python-based speech recognition program that listens to voice commands, processes them, and provides spoken responses. It supports *continuous listening* and can be exited by saying *"stop", **"exit", or **"quit"*.

### 🔗 Features
- ✨ *Speech-to-text* using Google Speech Recognition
- 📝 *Text-to-speech* using pyttsx3
- 🎨 *Fancy ASCII UI* with pyfiglet
- 🛠 *Error handling for better user experience*

---

## 🛠 Installation

### *Step 1: Clone the Repository*
bash
git clone https://github.com/sujaynsv/VocalTranscriber.git
cd VocalTranscriber


### *Step 2: Install Dependencies*
Ensure you have *Python 3.8+* installed, then run:
bash
pip install pyttsx3 SpeechRecognition pyaudio pyfiglet

> *Note:* If you face issues with pyaudio, install it manually:  
> - *Windows:* pip install pipwin && pipwin install pyaudio  
> - *Linux/macOS:* brew install portaudio && pip install pyaudio

---

## 🚀 Usage

### *Run the Assistant*
Simply execute:
bash
python assistant.py


### *How It Works*
1. The assistant will start and display a fancy ASCII banner.
2. It will listen for your voice and convert speech to text.
3. It will respond with text-to-speech.
4. Say *"stop", **"exit", or **"quit"* to end the program.

---
