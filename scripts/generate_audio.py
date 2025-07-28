from scripts import save_story
from gtts import gTTS
import os

def generate_audio():
    # 📖 Prompt user to input story and save it
    save_story.save_story()

    # 📄 Path to story file
    text_path = "D:/video_genie/data/story/story.txt"

    # 📥 Read the contents of the story
    with open(text_path, "r", encoding="utf-8") as f:
        story_text = f.read()

    # 🎙️ Convert text to speech
    tts = gTTS(text=story_text, lang='en', slow=False)

    # 💾 Save the audio file
    output_path = "D:/video_genie/data/audio/input/creative.mp3"
    tts.save(output_path)

    print(f"✅ Audio saved to: {output_path}")
