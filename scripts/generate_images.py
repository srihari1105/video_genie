import os
import json
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

def generate_images():

    PROMPT_FILE = "D:/video_genie/data/prompts/image_prompts.json"
    IMAGE_FOLDER = "D:/video_genie/data/images/"
    FINAL_JSON = "D:/video_genie/data/final/final_output.json"
    os.makedirs(IMAGE_FOLDER, exist_ok=True)
    os.makedirs(os.path.dirname(FINAL_JSON), exist_ok=True)

    # === 🔁 Ask if images are already generated ===
    skip_generation = input("Have you already generated the images? (yes/no): ").strip().lower() == "yes"

    # === 🧠 Create final_output.json based on existing images ===
    def create_final_output_json(folder, json_path, duration=3):
        print("📦 Creating final_output.json...")
        image_files = sorted([f for f in os.listdir(folder) if f.endswith(".png")])
        data = []
        for idx, filename in enumerate(image_files):
            data.append({
                "start": idx * duration,
                "end": (idx + 1) * duration,
                "image_path": os.path.join(folder, filename),
                "translated_text": ""  # You can update this if needed
            })
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"✅ Saved: {json_path}")

    # === 🖼️ Image Generation ===
    def generate_images():
        # 🧹 Clear existing images
        for file in os.listdir(IMAGE_FOLDER):
            if file.endswith(".png"):
                os.remove(os.path.join(IMAGE_FOLDER, file))
        print(f"🧼 Cleared old images from: {IMAGE_FOLDER}")

        # 🖼️ Ask for aspect ratio
        aspect_ratios = {
            "1": (1280, 720),
            "2": (1080, 1080),
            "3": (720, 1280),
            "4": None
        }

        print("Select image aspect ratio:")
        print("1. YouTube (16:9)")
        print("2. Instagram Post (1:1)")
        print("3. Reels / Shorts (9:16)")
        print("4. Custom")
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "4":
            width = int(input("Enter custom width: "))
            height = int(input("Enter custom height: "))
        elif choice in aspect_ratios:
            width, height = aspect_ratios[choice]
        else:
            print("Invalid choice. Using default 1280x720.")
            width, height = (1280, 720)

        try:
            steps = int(input("Enter number of inference steps (default 50): ").strip())
        except:
            steps = 50

        print("\n🔁 Loading Stable Diffusion...")
        pipeline = StableDiffusionPipeline.from_pretrained(
            "CompVis/stable-diffusion-v1-4",
            torch_dtype=torch.float32
        )
        pipeline = pipeline.to("cpu")

        with open(PROMPT_FILE, "r", encoding="utf-8") as f:
            prompts = json.load(f)

        for idx, item in enumerate(prompts, 1):
            prompt_text = item.get("prompt") or item.get("translated_text")
            if not prompt_text:
                print(f"⚠️ Skipping item {idx} due to missing prompt.")
                continue

            print(f"🎨 Generating image {idx}/{len(prompts)}: {prompt_text[:60]}...")
            try:
                image = pipeline(prompt_text, height=height, width=width, num_inference_steps=steps).images[0]
                image_path = os.path.join(IMAGE_FOLDER, f"image_{idx:03}.png")
                image.save(image_path)
                print(f"✅ Saved: {image_path}")
            except Exception as e:
                print(f"❌ Failed to generate image {idx}: {e}")

        print("✅ All images generated.")

    # === 🚀 Main Control ===
    if skip_generation:
        create_final_output_json(IMAGE_FOLDER, FINAL_JSON)
    else:
        generate_images()
        create_final_output_json(IMAGE_FOLDER, FINAL_JSON)