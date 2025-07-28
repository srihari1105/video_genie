import zipfile
import os
import shutil

def unzip():
    # Path to the downloaded ZIP file
    zip_path = r"C:\Users\dell\Downloads\generated_images.zip"

    # Folder to extract to
    extract_to = r"D:\video_genie\data\images"

    # Step 1: Clean the existing images folder
    if os.path.exists(extract_to):
        # Remove all files inside the folder
        for filename in os.listdir(extract_to):
            file_path = os.path.join(extract_to, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        print(f"🧹 Cleaned existing folder: {extract_to}/")
    else:
        os.makedirs(extract_to)
        print(f"📁 Created new folder: {extract_to}/")

    # Step 2: Extract ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"✅ Extracted all images to: {extract_to}/")

    # Step 3: Delete ZIP after extraction
    if os.path.exists(zip_path):
        os.remove(zip_path)
        print(f"🗑️ Deleted ZIP file: {zip_path}")
