import json
import os

def text_to_image_prompt(style, genre, width, height):
    # === 🔧 File Paths ===
    input_file = "D:/video_genie/data/transcripts/transcript.json"
    output_file = "D:/video_genie/data/prompts/image_prompts.json"

    # === 🧠 Prompt Builder ===
    def generate_prompt(translated_text, style, genre, width, height):
        resolution = f"{width}x{height}"
        if not translated_text.strip():
            return f"Abstract visual art in {style} style, genre: {genre}, {resolution} resolution"
        return (
            f"{style.capitalize()} artwork illustrating: \"{translated_text}\" "
            f"in the tone of a {genre} story, expressive lighting, deep colors, {resolution} resolution"
        )

    # === 🗂️ Load Transcript ===
    if not os.path.exists(input_file):
        print(f"❌ transcript.json not found at: {input_file}")
        exit()

    with open(input_file, "r", encoding="utf-8") as f:
        transcript = json.load(f)

    # === 🎯 Generate Prompts ===
    image_prompts = []
    for idx, segment in enumerate(transcript):
        start = segment["start"]
        end = segment["end"]
        translated = segment.get("translated", "").strip()
        prompt = generate_prompt(translated, style, genre, width, height)

        image_prompts.append({
            "id": idx + 1,
            "start": start,
            "end": end,
            "translated": translated,
            "prompt": prompt,
            "style": style,
            "genre": genre,
            "width": width,
            "height": height
        })

    # === 💾 Save Output ===
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(image_prompts, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Image prompts generated for {width}x{height} with style '{style}' and genre '{genre}'")
    print(f"📁 Saved to: {output_file}")
