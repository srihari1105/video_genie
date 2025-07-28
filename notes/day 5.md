# 🎮 AI-Powered Video Editor – Voice to Visuals (Telugu + English)

This project is part of my 100-day learning journey, where I'm building an AI-powered editor that takes Telugu (or mixed language) audio input and transforms it into meaningful AI-generated visual stories.

---

## ✅ Project Goals

* Convert voiceover (mic or audio file) to text using OpenAI Whisper
* Translate Telugu segments into English
* Generate image prompts per segment
* Create AI-generated images and assemble them into short videos

---

## 📅 Progress Log

### 🔹 Day 1–2: Audio Input Setup

* ✅ Integrated OpenAI Whisper for transcription
* ✅ Handled both file and mic input
* ✅ Converted `.mp3/.m4a` to `.wav` using `pydub`
* ✅ Dynamic mic recording with keypress detection

### 🔹 Day 3: Transcription with Timestamped Segments

* ✅ Whisper transcribes with timestamps
* ✅ Transcripts saved to `transcript.txt` and `transcript.json`
* ✅ Output organized per segment: `[start - end] text`

### 🔹 Day 4: Auto Translation

* ✅ Detected Telugu segments using `googletrans`
* ✅ Translated Telugu to English
* ✅ Created `translated.txt` and embedded translations in `transcript.json`

### 🔹 Day 5: Prompt Generator (Current Day)

* ✅ Created `generate_image_prompts.py`
* ✅ User can choose:

  * 🎨 **Visual style** (cinematic, watercolor, anime, etc.)
  * 🎬 **Genre** (romance, mythology, action, etc.)
* ✅ Prompt is generated per translated segment
* ✅ Output: `image_prompts.json` containing:

  ```json
  {
    "segment_id": 3,
    "start": 12.0,
    "end": 15.0,
    "translated": "You are my life",
    "prompt": "Watercolor artwork illustrating: 'You are my life' in the tone of a romance story...",
    "style": "watercolor",
    "genre": "romance"
  }
  ```

---

## 📁 Directory Structure

```
/data
  └── /audio
      └── /input            # Input audio files (mp3, m4a, etc.)
      └── /output           # Converted .wav and mic recordings
  └── /transcripts
      └── transcript.txt    # Original transcript with timestamps
      └── translated.txt    # Translated (Telugu → English)
      └── transcript.json   # Structured segment data
  └── /prompts
      └── image_prompts.json # Final prompts per segment

/scripts
  └── speech_to_text.py     # Mic/file audio to transcript
  └── generate_image_prompts.py  # Segment-wise prompt generator
```

---

## ⚠️ Disclaimer

> ⚠️ Note: This is a learning journey. Please don’t clone or replicate this until I finish the complete version. I’ll open-source the final build after completion.

---

## 🚀 Next Up (Day 6 Preview)

* 🧠 Use `image_prompts.json` to generate AI images per segment
* ⚙️ Allow batch export using DALL·E / Sora / Midjourney

---

## 📌 Tech Stack

* Python 3.10+
* OpenAI Whisper
* Google Translate API (`googletrans`)
* Pydub + SoundDevice
* JSON & file handling

---

## 🙌 Connect

Follow my progress on [LinkedIn](#)
Let’s build in public and grow together!

\#AI #OpenAI #SpeechToText #TeluguAI #PromptEngineering #BuildInPublic #100DaysOfAI
