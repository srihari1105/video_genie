# 🎬 Day 7: Image to Video Generation (with Audio + Text Overlay)

## ✅ Tasks Completed Today

1. **Debugged and fixed MoviePy setup**:

   * Resolved `moviepy.editor` import issues
   * Installed proper version compatible with Python 3.12
   * Installed and configured **ImageMagick** (with correct binary path for `TextClip`)

2. **Implemented `generate_video.py` script**:

   * Converts static images into a video
   * Allows user to choose whether to show **text overlays** (subtitles)
   * Adds **background audio** with duration matching
   * Auto exports final video using `libx264` and `aac` codecs

3. **Handled Audio Issues**:

   * Converted `.wav` to `.mp3` using Pydub
   * Ensured compatibility with MoviePy’s audio system

---

## 🧪 How to Run

### 1. Convert Audio (if needed)

```python
from pydub import AudioSegment
sound = AudioSegment.from_wav("../data/audio/output/converted.wav")
sound.export("../data/audio/output/converted.mp3", format="mp3")
```

### 2. Run the video generator

```bash
python scripts/generate_video.py
```

You’ll be prompted to choose:

```
Do you want to add text overlay on each image? (yes/no)
```

---

## 📂 Output

* Final video: `data/final_video.mp4`
* Audio: `converted.mp3`
* Text overlays: Optional, user-defined

---

## 🔧 Requirements

* Python 3.12
* MoviePy
* Pydub
* ImageMagick 7.1 (added to PATH and verified)
* FFmpeg (installed and in PATH)

---

## 🚀 Next Step (Day 8)

* Add transition effects between clips
* Add logo watermark
* Add intro/outro title screen support

---

## ⚠️ Disclaimer

This is a learning journey. Please don’t clone or replicate this until I finish the complete version. I’ll open-source the final build after completion.
