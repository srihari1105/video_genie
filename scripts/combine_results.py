import json
import os

def combine_results():
    # === 🔧 File paths ===
    TRANSCRIPT_FILE = "D:/video_genie/data/transcripts/transcript.json"
    IMAGE_FOLDER = "D:/video_genie/data/images/content/ai_video_editor/generated_images/"
    OUTPUT_FILE = "D:/video_genie/data/final/final_output.json"

    # === 📥 Load transcript ===
    with open(TRANSCRIPT_FILE, "r", encoding="utf-8") as f:
        transcript_data = json.load(f)

    # === 🖼️ List and sort image files ===
    image_files = sorted([
        file for file in os.listdir(IMAGE_FOLDER)
        if file.endswith(".png")
    ])

    # === 🧩 Combine ===
    combined = []

    for idx, segment in enumerate(transcript_data):
        if idx >= len(image_files):
            print(f"⚠️ Skipping segment {idx+1} - No image found.")
            continue

        image_path = os.path.abspath(os.path.join(IMAGE_FOLDER, image_files[idx]))
        image_path = image_path.replace("\\", "/")  # 🔁 Ensures forward slashes

        combined.append({
            "segment_id": idx + 1,
            "start": segment.get("start"),
            "end": segment.get("end"),
            "original_text": segment.get("original"),
            "translated_text": segment.get("translated"),
            "image_path": image_path
        })

    # === 💾 Save final output ===
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)

    print(f"✅ Final combined output saved to: {OUTPUT_FILE}")
