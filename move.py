import os
import shutil
import gradio as gr

# === File extensions ===
photo_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff')
music_extensions = ('.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma')
video_extensions = ('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm')

# === Folders to skip ===
exclude_dirs = [
    'Program Files', 'Program Files (x86)', 'Windows', 'captcha',
    '$Recycle.Bin', 'System Volume Information', 'Games',
    'DeliveryOptimization', 'Programs', 'WindowsApps',
    'WpSystem', 'WUDownloadCache', 'ALL_Photos', 'ALL_Music', 'ALL_Videos', 'ALL_Files'
]

def move_media(drive_to_scan, dest_folder, media_type):
    drive_to_scan = drive_to_scan.strip()
    dest_folder = dest_folder.strip()

    if not os.path.exists(drive_to_scan):
        return f"❌ Drive not found: {drive_to_scan}"

    if not dest_folder:
        return "❌ Please provide a destination folder path."

    os.makedirs(dest_folder, exist_ok=True)

    # === Choose target file types ===
    if media_type == "Photos":
        target_extensions = photo_extensions
    elif media_type == "Music":
        target_extensions = music_extensions
    elif media_type == "Videos":
        target_extensions = video_extensions
    else:
        target_extensions = photo_extensions + music_extensions + video_extensions

    moved_count = 0
    output_log = []

    # === Start scanning ===
    output_log.append(f"🚀 Scanning {drive_to_scan} for {media_type.lower()}...\n")

    for root, dirs, files in os.walk(drive_to_scan):
        if any(excluded.lower() in root.lower() for excluded in exclude_dirs):
            continue

        for file in files:
            if file.lower().endswith(target_extensions):
                src = os.path.join(root, file)
                dst = os.path.join(dest_folder, file)

                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(dst):
                    dst = os.path.join(dest_folder, f"{base}_{counter}{ext}")
                    counter += 1

                try:
                    shutil.move(src, dst)
                    moved_count += 1
                    output_log.append(f"✅ Moved: {src} → {dst}")
                except Exception as e:
                    output_log.append(f"❌ Failed: {src} ({e})")

    output_log.append(f"\n🎉 Done! Total files moved: {moved_count}")
    output_log.append(f"📂 Saved in: {dest_folder}")

    return "\n".join(output_log)


# === Build Gradio UI ===
with gr.Blocks(title="Media Organizer for Windows") as demo:
    gr.Markdown(
        "## 🎶📷🎬 Media Organizer\n"
        "Move photos, music, and videos from any drive to a chosen folder easily."
    )

    drive_path = gr.Textbox(label="Enter Drive Path (Example: C:\\user)", value="")
    dest_folder = gr.Textbox(label="Destination Folder (Example: D:\\Sorted_Media)")
    media_type = gr.Radio(["Photos", "Music", "Videos", "All Media"], label="Select Media Type", value="Photos")

    run_button = gr.Button("🚀 Start Moving Files")
    result_box = gr.Textbox(label="Output Log", lines=20)

    run_button.click(fn=move_media, inputs=[drive_path, dest_folder, media_type], outputs=result_box)

demo.launch()
