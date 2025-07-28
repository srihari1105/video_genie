from scripts.generate_audio import generate_audio
from scripts.speech_to_text import speech_to_text
from scripts.combine_results import combine_results
# from scripts.generate_images import generate_images
from scripts.generate_video import generate_video
from scripts.unzip import unzip
from scripts.text_to_image_prompt import text_to_image_prompt
from scripts.save_story import save_story
import time

def main():
    #================================step:1 generate audio=======================================
    print("=" * 60)
    print("👋 hey DUDE!😍\nLet's make a kick start 🚀")
    print("=" * 60)
    time.sleep(0.4)

    print('''\n🤨 Let me know...
Do you have the audio, or do you want to create it from a story?''')
    time.sleep(0.4)
    x = int(input("👉 Enter 1 to create audio from text, or 0 if you already have it: "))

    if x == 1:
        print("\n🎜️ Let's create audio from your story...")
        generate_audio()
    else:
        print("\n🧵‍♂️ Ok then, let's start the process with your audio 🚒")

    #==================================================================================================

    #===============================variables========================================================

    #======================variables for speech_to_text.py===============================================
    print("\n" + "=" * 60)
    print("🔊 STEP 1: Speech to Text")
    print("=" * 60)
    time.sleep(0.4)
    mode = input("🎧 Choose input mode - type 'file' or 'mic': ").strip().lower()
    choose_model = input("🧠 Enter Whisper model (tiny, base, medium, large): ").strip()
    if mode == "file":
        file_name = input("📁 Enter audio filename (e.g., audio.mp3): ").strip()
    else:
        file_name = None
    #======================================================================================================

    #====================variables for text_to_image_prompt.py=============================================
    print("\n" + "=" * 60)
    time.sleep(0.4)
    print("🎨 STEP 2: Style & Genre Selection")
    print("=" * 60)

    STYLE_CHOICES = ['cinematic', 'watercolor', 'digital painting', 'anime', '3D render', 'sketch']
    GENRE_CHOICES = ['romance', 'mythology', 'drama', 'action', 'comedy', 'horror', 'inspirational']

    def choose_option(label, choices):
        print(f"\n🎧 Choose {label} from the list below:")
        for i, option in enumerate(choices, 1):
            print(f"{i}. {option}")
        while True:
            try:
                selected = int(input(f"Enter the number for {label}: "))
                if 1 <= selected <= len(choices):
                    return choices[selected - 1]
                else:
                    print("❌ Invalid choice. Try again.")
            except ValueError:
                print("❌ Please enter a number.")

    style = choose_option("visual style", STYLE_CHOICES)
    genre = choose_option("video genre", GENRE_CHOICES)

    aspect_ratios = {
        "1": (1280, 720),
        "2": (1080, 1080),
        "3": (720, 1280),
        "4": None
    }

    print("\n" + "=" * 60)
    print("📀 Select Image Aspect Ratio")
    print("=" * 60)
    print("1. YouTube (1280x720)")
    print("2. Instagram Post (1080x1080)")
    print("3. Reels / Shorts (720x1280)")
    print("4. Custom")
    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == "4":
        width = int(input("Enter custom width: "))
        height = int(input("Enter custom height: "))
    elif choice in aspect_ratios:
        width, height = aspect_ratios[choice]
    else:
        print("⚠️ Invalid choice. Using default 1280x720.")
        width, height = (1280, 720)
    #=====================================================================================================

    #==============================variables for generate video==============================================
    print("\n" + "=" * 60)
    time.sleep(0.4)
    print("📝 STEP 3: Text Overlay & Transitions")
    print("=" * 60)

    add_text = input("Do you want to add text overlay on each image? (yes/no): ").strip().lower()
    text_position = None
    if add_text == "yes":
        text_position = input("Where do you want the text overlay? (top/bottom): ").strip().lower()

    transition_type = input("Select transition type (none/fade/crossfade/slide/zoom): ").strip().lower()
    transition_duration = 0.0
    if transition_type in ["fade", "crossfade", "slide", "zoom"]:
        try:
            transition_duration = float(input("Enter transition duration in seconds (e.g., 0.5): ").strip())
        except ValueError:
            print("⚠️ Invalid duration, using default 0.5s.")
            transition_duration = 0.5
    #==========================================================================================================

    #==============================step:2 speech_to_text.py================================================
    speech_to_text(mode, choose_model, file_name)
    #========================================================================================================

    #======================step:3 text_to_image_prompt====================================================
    text_to_image_prompt(style, genre, width, height)
    #======================================================================================================

    #==========================step:4 generate_images {colab/code file}=====================================
    print("\n" + "=" * 60)
    time.sleep(0.4)
    print("💻 STEP 4: GPU or Colab Image Generation")
    print("=" * 60)
    print("\n🤨 Does your system have a GPU for local image generation?")
    gpu = int(input("👉 Enter 1 for YES, or 0 to use Colab: "))

    if gpu == 1:
        pass  # integrate generate_images.py here
    else:
        print("\n🚀 Using Google Colab for Image Generation")
        print("=" * 60)
        print("1️⃣  Open this Colab file path:\n    👉 D:/video_genie/data/colab notebook/generate_images.ipynb")
        time.sleep(0.2)
        print("2️⃣  Open with → Google Colab (or upload manually at https://colab.research.google.com)")
        time.sleep(0.2)
        print("3️⃣  Set Runtime > Change runtime type → ⚡ GPU")
        time.sleep(0.2)
        print("4️⃣  Run all cells (Shift+Enter or Runtime > Run All)")
        time.sleep(0.2)
        print("5️⃣  Download the generated ZIP images\n")
        time.sleep(0.2)
        input("📦 Press Enter after you finish and place the ZIP file in the folder...\n")
        unzip()
        print("✅ Images downloaded into your video_genie folder")
        time.sleep(0.2)
    #=======================================================================================================

    #================================step:6 combine results================================================
    combine_results()
    #======================================================================================================

    #======================================step:7 generate video==============================================
    generate_video(add_text, transition_type, transition_duration, text_position)
    #=========================================================================================================

    print("\n🎉🎉🎉 All Done! Your AI video is ready! 🥳")
    time.sleep(0.4)
    print("📍 Output Video: D:/video_genie/data/final_video.mp4")
    time.sleep(0.2)
    print("=" * 60)

main()
