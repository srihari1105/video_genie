#2

import os
import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile
import keyboard
import numpy as np
import time
import json
from deep_translator import GoogleTranslator
from pydub import AudioSegment

def speech_to_text(mode,choose_model,file_name=None):
    # === 🔧 CONFIGURATION ===
    input_folder = "D:/video_genie/data/audio/input/"
    output_wav = "D:/video_genie/data/audio/output/converted.wav"
    transcript_file = "D:/video_genie/data/transcripts/transcript.txt"
    translated_file = "D:/video_genie/data/transcripts/translated.txt"
    json_output_file = "D:/video_genie/data/transcripts/transcript.json"

    # === 🎛️ Choose mode ===
    mode = mode
    choose_model = choose_model

    # === 📦 Load Whisper model and Translator ===
    model = whisper.load_model(choose_model)
    translator = GoogleTranslator(source="auto", target="en")

    # === 📁 Handle file input ===
    if mode == "file":
        file_name = file_name
        input_path = os.path.join(input_folder, file_name)

        if not os.path.exists(input_path):
            print("❌ File not found:", input_path)
            exit()

        ext = file_name.split(".")[-1].lower()
        print(f"🔄 Converting '{file_name}' ({ext}) to WAV...")

        audio = AudioSegment.from_file(input_path, format=ext)
        audio = audio.set_frame_rate(16000).set_channels(1)
        audio.export(output_wav, format="wav")
        print("✅ Conversion complete.")

        print("🧠 Transcribing file audio...")
        result = model.transcribe(output_wav, task="transcribe", fp16=False)

    # === 🎤 Handle mic input ===
    elif mode == "mic":
        fs = 16000
        print("🎤 Press 'S' to START recording and 'R' to STOP recording.")

        while not keyboard.is_pressed('s'):
            pass

        print("🔴 Recording started... Press 'R' to stop.")
        frames = []

        try:
            while True:
                if keyboard.is_pressed('r'):
                    print("⏹️ Recording stopped.")
                    break

                block = sd.rec(int(0.5 * fs), samplerate=fs, channels=1, dtype='int16')
                sd.wait()
                frames.append(block)
        except KeyboardInterrupt:
            print("⏹️ Recording interrupted.")

        audio_data = np.concatenate(frames, axis=0)

        temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        write(temp_file.name, fs, audio_data)
        temp_file.close()

        print("🧠 Transcribing mic input...")
        result = model.transcribe(temp_file.name, task="transcribe", fp16=False)

        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)
            print(f"🧹 Temporary mic file deleted: {temp_file.name}")

    else:
        print("❌ Invalid mode. Use 'file' or 'mic'.")
        exit()

    # === 💾 SAVE OUTPUTS: TEXT + JSON ===
    json_segments = []

    with open(transcript_file, "w", encoding="utf-8") as f_orig, \
        open(translated_file, "w", encoding="utf-8") as f_trans:

        for segment in result.get("segments", []):
            start = round(segment['start'], 2)
            end = round(segment['end'], 2)
            original_text = segment['text'].strip()

            # Translate using deep_translator
            try:
                translated_text = GoogleTranslator(source="auto", target="en").translate(original_text)
            except Exception:
                translated_text = original_text

            # Write to TXT files
            f_orig.write(f"[{start:.2f}s - {end:.2f}s] {original_text}\n")
            f_trans.write(f"[{start:.2f}s - {end:.2f}s] {translated_text}\n")

            # Append to JSON structure
            json_segments.append({
                "start": start,
                "end": end,
                "original": original_text,
                "translated": translated_text
            })

    # Save to JSON
    with open(json_output_file, "w", encoding="utf-8") as f_json:
        json.dump(json_segments, f_json, ensure_ascii=False, indent=2)

    # === ✅ DONE ===
    print(f"\n💾 Transcript saved to: {transcript_file}")
    print(f"🌐 Translated version saved to: {translated_file}")
    print(f"📦 JSON format saved to: {json_output_file}")