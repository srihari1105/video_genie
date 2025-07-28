## 🧠 Day 3 Notes – Whisper File & Mic Transcription System

### ✅ Completed Tasks:

#### 🎤 1. Mic Input Transcription

* Implemented real-time microphone recording using:

  * `sounddevice` to capture live audio
  * `keyboard` module to start/stop recording by holding the `r` key
* Saved mic input to a temporary WAV file using `tempfile`
* Used OpenAI Whisper to transcribe recorded audio
* **Auto language detection** handled by `language=None`

#### 📁 2. File Input Transcription

* Allowed the user to load MP3/M4A/other formats
* Converted all audio to mono 16kHz WAV using `pydub`
* Transcribed the full audio file directly without chunking
* Saved timestamped transcripts to `transcripts/transcript.txt`

#### 🧹 3. Cleanup System

* Automatically deleted:

  * Temporary mic files (`tempfile`)
  * Converted files and chunk folders if used
* Prevented file permission issues by **explicitly closing temp files** (`temp_file.close()`)

---

### ⚖️ Code Enhancements:

* Added full inline comments for better learning and readability
* Reorganized import structure: `pydub` imported only in file mode to optimize dependencies
* Converted recorded audio (list of NumPy arrays) properly using `np.array()` before saving
* Verified and updated `write()` logic to prevent `AttributeError`

---

### 🔪 Testing Done:

* ✅ Tested mic input: Held down 'r', recorded sample, and verified correct transcription
* ✅ Tested file input with `leo.mp3`, `test123.mp3`, and a 2-minute sample
* 📄 Transcript format verified with timestamps

---

### ❌ Issues Encountered:

* GitHub Actions CI failure due to an unconfigured `.github/workflows/ci.yml` file

  * Resolved with advice to either delete or fix the file
* Mic recording initially failed due to improper data type passed to `write()`

  * Fixed using `np.array(frames, dtype='int16')`
* `PermissionError` from not closing temp files

  * Fixed by using `temp_file.close()`

---

### 💾 Files Modified Today:

* `scripts/speech_to_text.py`: Main logic implemented
* Added `data/audio/input/` test files: `leo.mp3`, `test123.mp3`
* Created transcript output at: `data/transcripts/transcript.txt`

---

### ✅ Git Commit for Today:

```bash
git add .
git commit -m "🧠 Day 3: Added Whisper support with file & mic input, transcription + cleanup"
git push
```

---

## 🔮 What’s Next (Day 4 Plan):

1. **Refactor Code to Functions**:

   * Create `transcribe_file()`, `transcribe_mic()`, and `save_transcript()` functions

2. **Create CLI Arguments (optional)**:

   * Allow user to run with `--mode mic` or `--mode file`

3. **Audio Chunking Mode (Optional)**:

   * Add optional 30s chunking support (for longer files)

4. **Start UI Planning (HTML/CSS or Streamlit)**:

   * Brainstorm a basic GUI or web interface to trigger file/mic transcription
