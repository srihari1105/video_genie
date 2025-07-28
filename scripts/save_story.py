import sys
import os

def save_story(folder="D:/video_genie/data/story", filename="story.txt"):
    # Make sure the folder exists
    os.makedirs(folder, exist_ok=True)

    # Full path to the story file
    file_path = os.path.join(folder, filename)

    # Ask user to paste their story
    print("📖 Paste your story below. Press Ctrl+Z (Windows) or Ctrl+D (Linux/macOS) in the next line when you're done:\n")

    # Read multi-line input from stdin
    story = sys.stdin.read()

    # Remove the old file if it exists
    if os.path.exists(file_path):
        os.remove(file_path)

    # Write new story
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(story)

    print(f"\n✅ Story saved to {file_path}")