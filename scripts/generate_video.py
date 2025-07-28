import os
import json
from moviepy.editor import (
    ImageClip, concatenate_videoclips, AudioFileClip, CompositeVideoClip
)
from PIL import Image, ImageDraw, ImageFont

def generate_video(add_text, transition_type, transition_duration, text_position=None):

    # 🩹 Fix for Pillow >=10 (ANTIALIAS removed)
    if not hasattr(Image, 'ANTIALIAS'):
        Image.ANTIALIAS = Image.Resampling.LANCZOS

    # === 🛠️ Configuration ===
    DATA_FILE = "D:/video_genie/data/final/final_output.json"
    AUDIO_FILE = "D:/video_genie/data/audio/output/converted.wav"
    OUTPUT_VIDEO = "D:/video_genie/data/final_video.mp4"
    TEMP_CLIP_FOLDER = "D:/video_genie/data/temp_clips"
    FONT_PATH = "C:/Windows/Fonts/arial.ttf"  # ✅ Change if you want another font

    os.makedirs(TEMP_CLIP_FOLDER, exist_ok=True)

    # === ✅ Text Overlay Helper (Pillow-based) ===
    def overlay_text_on_image(image_path, text, position="bottom", save_path=None):
        image = Image.open(image_path).convert("RGB")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(FONT_PATH, size=24)

        # Get text size (using textbbox for Pillow >=10)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Padding and background
        padding = 10
        bg_height = text_height + 2 * padding
        bg = Image.new("RGB", (image.width, bg_height), (0, 0, 0))

        # Combine image + text background
        if position == "top":
            combined = Image.new("RGB", (image.width, image.height + bg_height))
            combined.paste(bg, (0, 0))
            combined.paste(image, (0, bg_height))
            text_y = padding
        else:
            combined = Image.new("RGB", (image.width, image.height + bg_height))
            combined.paste(image, (0, 0))
            combined.paste(bg, (0, image.height))
            text_y = image.height + padding

        text_x = (image.width - text_width) // 2
        draw = ImageDraw.Draw(combined)
        draw.text((text_x, text_y), text, font=font, fill="white")

        if save_path:
            combined.save(save_path)
            return save_path
        else:
            return combined

    # === 🧠 User Input ===
    # add_text = add_text
    # if add_text=="yes":
    #     text_position = text_position
    # transition_type = transition_type
    # transition_duration =transition_duration

    # === 📄 Load Data ===
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        segments = json.load(f)

    clips = []

    print("\n🎨 Generating video clipsD:/video_genie.")
    for i, segment in enumerate(segments):
        start = segment["start"]
        end = segment["end"]
        duration = end - start
        image_path = segment["image_path"]
        text = segment.get("translated_text", "")

        # === 📝 Apply text if enabled
        if add_text=="yes" and text:
            try:
                overlayed_image_path = os.path.join(TEMP_CLIP_FOLDER, f"frame_{i:03d}.jpg")
                overlay_text_on_image(image_path, text, text_position, overlayed_image_path)
                image_path = overlayed_image_path
            except Exception as e:
                print(f"⚠️ Text overlay failed: {e}. Skipping text.")

        img_clip = ImageClip(image_path).set_duration(duration).resize(height=480)

        # === 🔁 Transitions ===
        if transition_type == "fade":
            img_clip = img_clip.fadein(transition_duration).fadeout(transition_duration)
        elif transition_type == "crossfade" and i != 0:
            img_clip = img_clip.crossfadein(transition_duration)
        elif transition_type == "slide":
            img_clip = img_clip.set_start(i * (duration - transition_duration))
            img_clip = img_clip.set_position(lambda t: ('center', int(50 * (1 - t / transition_duration))) if t < transition_duration else 'center')
        elif transition_type == "zoom":
            img_clip = img_clip.resize(lambda t: 1 + 0.1 * (t / transition_duration) if t < transition_duration else 1)

        clips.append(img_clip)

    # === 🎬 Merge Clips ===
    print("\n📰 Concatenating clipsD:/video_genie.")
    if transition_type == "crossfade":
        final_video = concatenate_videoclips(clips, method="compose", padding=-transition_duration)
    else:
        final_video = concatenate_videoclips(clips, method="compose")

    # === 🔊 Add Audio ===
    print("\n🎷 Adding background audioD:/video_genie.")
    try:
        audio = AudioFileClip(AUDIO_FILE)
        final_video = final_video.set_audio(audio)
    except Exception as e:
        print(f"⚠️ Warning: Audio not added due to error: {e}")

    # === 💾 Export Final Video ===
    print("\n💾 Exporting final videoD:/video_genie.")
    final_video.write_videofile(OUTPUT_VIDEO, codec="libx264", audio_codec="aac", fps=24)

    print("\n✅ Video created successfully at:", OUTPUT_VIDEO)