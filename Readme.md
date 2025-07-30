# VIDEO_GEINE
# 🎮 AI Video Editor - Turn Audio or Text into AI Videos!

This is a command-line based AI video editor that converts your **voice or story text** into a full **AI-generated video**, complete with translated captions, artwork-style visuals, and music. It combines the power of **Whisper**, **Deep Translator**, **Stable Diffusion**, and **MoviePy** into one streamlined pipeline.

> ⚡ First version built as a resume project — future versions will include frontend UI!

---

## 🌟 Features

* 🎤 Accept audio (mic or file) or user-pasted story text
* 🧠 Transcribe using OpenAI Whisper and translate to English
* 🎨 Generate image prompts using custom styles + genres
* 🖼️ Use Google Colab to generate AI images (Stable Diffusion XL)
* 🎮 Automatically generate a final video with:

  * Image transitions (fade, crossfade, zoom, etc.)
  * Text overlays (optional, top/bottom)
  * Background audio synced to timing

---

## 🧱 Tech Stack

| Area              | Tools Used                                                   |
| ----------------- | ------------------------------------------------------------ |
| Speech to Text    | [Whisper](https://github.com/openai/whisper)                 |
| Translation       | [Deep Translator](https://pypi.org/project/deep-translator/) |
| Prompt Generation | Python (custom logic + formatting)                           |
| Image Generation  | Stable Diffusion via Google Colab                            |
| Video Creation    | [MoviePy](https://zulko.github.io/moviepy/)                  |
| Text on Images    | Pillow (instead of ImageMagick)                              |
| Interface         | Python CLI (`main.py`)                                       |

---

## 📁 Folder Structure

```
project/
├── main.py
├── scripts/            # was locked in gihub and under development 
│   ├── generate_audio.py                       
│   ├── speech_to_text.py
│   ├── save_story.py
│   ├── text_to_image_prompt.py
│   ├── combine_results.py
│   ├── generate_video.py
│   └── unzip.py
├── data/
│   ├── story/
│   ├── audio/
│   │   ├── input/
│   │   └── output/
│   ├── transcripts/
│   ├── prompts/
│   ├── images/
│   ├── final/
│   └── colab notebook/
│       └── generate_images.ipynb
```

---

## 🚀 How to Use

1. Clone the repo:

   ```
   git clone https://github.com/srihari1105/ai-video-editor.git
   cd ai-video-editor
   ```

2. Set up the virtual environment:

   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the project:

   ```
   python main.py
   ```

4. Follow the guided CLI. Choose whether you want to:

   * Use mic/file for audio
   * Select styles and genre
   * Add captions, transition type
   * Upload to Colab and generate AI images
   * Get a final video in `/data/final_video.mp4`

---

## 🤯 Lessons & Struggles

| Challenge                               | Solution                                                |
| --------------------------------------- | ------------------------------------------------------- |
| Whisper errors due to Python version    | Switched to Python 3.10.11 for compatibility            |
| ImageMagick blocked text rendering      | Replaced with Pillow-based overlay                      |
| Terminal screen looked messy            | Added spacing, emoji icons, and `time.sleep()`          |
| Image generation without GPU            | Used Colab backend with `.ipynb` upload                 |
| Script-to-script integration in Python  | Refactored everything to use **function-based modules** |
| Need to test stories of different types | Built action, horror, mythology stories for demo        |

---

## 🧪 Example Output

* 📖 Input: Mythological Story (typed or spoken)
* 🎤 Audio: Converted using gTTS or user input
* 🖼️ Images: Created via Stable Diffusion prompts
* 🎞️ Final Output: Smooth slideshow video with text overlay + sound

> Final video path: `data/final_video.mp4`

---

## 🛠️ Future Plans

* 🔌 Add a **Gradio** or **Lovable AI** frontend
* 💡 Add support for background music selection
* ☁️ Move image generation from Colab to local GPU (or cloud API)
* 🔗 Deploy as a web app for public use

---

## 🤝 Acknowledgements

Thanks to:

* [OpenAI Whisper](https://github.com/openai/whisper)
* [Deep Translator](https://pypi.org/project/deep-translator/)
* [MoviePy](https://zulko.github.io/moviepy/)
* [Google Colab](https://colab.research.google.com)

---

## 🔗 Connect

This was my **first end-to-end AI project** — built with passion, learning, and a lot of debugging 💥

📬 Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/srihari-singupurapu)
🎥 Demo video, docs, and UI will come in the next version!

---


🚫 Note: Core project logic (e.g., image generation, audio processing, etc.) has been removed from public access to prevent plagiarism.

This project is shared only for **portfolio demonstration** purposes. Please do not clone and claim as your own.
