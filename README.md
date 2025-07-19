# 🤖 Jarvis - AI Voice Assistant 🎙️

Jarvis is a personal AI assistant built using Python. It uses voice recognition and AI (via OpenAI's GPT-3.5) to execute commands, answer questions, and open files or websites—just like a basic version of Siri or Alexa.

---

## 🚀 Features

- 🎧 Voice-controlled interaction (hotword: **"Jarvis"**)
- 🌐 Open websites like Google, YouTube, Facebook, LinkedIn
- 🎶 Play music (based on a predefined music library)
- 📰 Fetch latest news headlines using NewsAPI
- 📂 Open local files and system folders (like Recycle Bin)
- 🤖 Answer general queries using ChatGPT (OpenAI API)
- 🔊 Speaks responses using `gTTS` and `pygame` audio engine

---

## 🔧 Technologies Used

- `speechrecognition` – for capturing and recognizing voice input  
- `gTTS` + `pygame` – for converting text to speech  
- `pyttsx3` – optional alternate speech engine  
- `webbrowser` – to open URLs  
- `os` – to manage files and folders  
- `requests` – for NewsAPI integration  
- `openai` – for intelligent chat responses  

---

## 📁 Project Structure

Jarvis/ ├── main.py              # Main script ├── musiclibrary.py      # Dictionary of music name and links ├── requirements.txt     # Python dependencies (optional) └── README.md            # Project overview and documentation

---

## ▶️ How to Run

1. **Install Dependencies:**

```bash
pip install speechrecognition gtts pygame openai requests pyttsx3

2. Add Your API Keys:



Replace <Your Key Here> with your actual API keys for:

OpenAI

NewsAPI


3. Run the Assistant:



python main.py

4. Use Commands Like:



"Open YouTube"

"Play [song name]"

"Open file"

"News"

Or ask any question!



---

🔮 Future Plans

Add WhatsApp and email messaging

Android integration

Continuous background listening

GUI version of the assistant

Make it as powerful as Siri or Google Assistant!



---

🙋‍♂️ Creator

Built with ❤️ by Yash Raghuwanshi
A passionate CSE student building the future of AI.


---

📜 License

This project is open-source and free to use for educational purposes.