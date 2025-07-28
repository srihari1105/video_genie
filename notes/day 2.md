## 📘 Day 2 Notes – Speech-to-Text System (Mic & File Mode)

### ✅ Completed Goals:

* Implemented a Python-based speech-to-text system that supports both mic input and audio file input.
* Transcriptions saved in a clean text format.
* Handled multiple audio formats (mp3, m4a, wav).

---

### 📂 Folder Structure Setup:

```
project/
├── data/
│   ├── audio/
│   │   ├── input/         # User audio input (mp3, m4a)
│   │   └── output/        # Converted wav files (output)
│   └── transcripts/       # Final transcript files
├── scripts/
│   └── speech_to_text.py  # Main transcription script
├── notes/                 # Notes and daily logs
└── .venv/                 # Virtual environment (Python)
```

---

### 🧠 Core Concepts Learned:

#### 🎤 Mic vs File Mode:

* Mic: Uses `speech_recognition.Microphone()`
* File: Asks user for file name + format → converts to `.wav` using `pydub`

#### 🔁 Dynamic Mode Selection:

```python
mode = input("Choose input mode - type 'mic' or 'file': ")
```

#### 🛠️ Audio Conversion:

* Used `pydub.AudioSegment.from_file()` to handle mp3/m4a
* Exported as `.wav` with 16kHz sample rate for better accuracy

#### 📝 Transcription Output:

* Used `recognize_google()` for transcription
* Supported `language="te-IN"` for Telugu
* Saved final text output in `transcript.txt`

---

### ✅ Features Implemented:

* [x] File input (user chooses file)
* [x] Mic input (records speech directly)
* [x] Handles mp3, m4a, wav files
* [x] Transcript saved with UTF-8 encoding
* [x] Git commits completed for changes
* [x] LinkedIn post made for Day 2

---

### ⚙️ Next Steps:

* Add support for long audio chunking
* Improve transcription readability (timestamps, punctuation)
* Continue documenting and pushing to GitHub

---

### 💡 Notes:

* Mic recordings are auto-converted to `.wav`
* For file inputs, format must be known (prompted from user)
* Output was in a single line initially → fixed by inserting `\n` every few words
* Google Speech API has limits, so short chunks work better

---

⚠️ *This project is part of a learning journey. Please don’t clone or replicate until the final version is released.*
