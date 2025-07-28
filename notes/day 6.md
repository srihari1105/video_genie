# 🎬 AI Video Editor – Day 6 Notes  
**📅 Date:** 1st July 2025  
**🔍 Focus:** Image Generation from Prompts (Audio → Text → Translated Prompt → Image)

---

## ✅ What I Learned & Did Today

### 1️⃣ Explored Image Generation Models
- Researched free AI image tools:
  - Hugging Face Inference API (✅ Chosen)
  - OpenArt, Leonardo AI, Playground AI
- Understood:
  - **Hosted API** (easy to use, limited credits)
  - **Local setup** (not feasible on low-end GPUs)

---

### 2️⃣ Hugging Face Setup
- Selected model: `stabilityai/stable-diffusion-3.5-large`
- Generated a personal Hugging Face **Access Token**
- Used `.env` file to securely load API key into scripts

---

### 3️⃣ Integrated Image Generation
- Finalized `generate_image.py` script:
  - Reads prompts from `data/prompts/image_prompts.json`
  - Sends them to Hugging Face API
  - Saves each image to `data/images/`

---

### 4️⃣ Faced & Solved Issues
| Issue | Solution |
|-------|----------|
| 404 error | Corrected model name and API endpoint |
| API token not loading | Used `dotenv` to load `.env` correctly |
| 402 (Quota Exceeded) | Switched to Google Colab with GPU |

---

### 5️⃣ Switched to Google Colab
- Setup:
  - Whisper for transcription
  - Google Translator for English output
  - Diffusers + Stable Diffusion for image generation
- Built `main.ipynb` notebook:
  - Full end-to-end pipeline (Audio → Image)
  - Easy to run on GPU for free with Google Colab

---

## 🧪 Test Results

- Used creative Telugu-English audio
- Generated cinematic prompts with strong visuals
- Output images were visually rich (until API quota hit)
- Google Colab version works well with larger pipelines

---

## 🗂️ Files Updated Today

| File Name             | Purpose                                       |
|----------------------|-----------------------------------------------|
| `.env`               | Holds Hugging Face API token securely         |
| `generate_image.py`  | Generates images from translated prompts      |
| `main.ipynb`         | Colab-friendly notebook with full UI pipeline|

---

## 🚀 Tomorrow's Plan (Day 7)

- Build a Gradio web app in Colab
  - Upload audio
  - Show transcripts and translated prompts
  - Display generated images
- Add **style** and **genre** selections to enhance prompt control
- Start preparing **UI for final demo**

---

⚠️ Note: This is a learning journey. Please don’t clone or replicate this until I finish the complete version. I’ll open-source the final build after completion.
