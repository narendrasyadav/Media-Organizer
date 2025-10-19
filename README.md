# Media Organizer

**Media Organizer** is a Python tool with a **Gradio web interface** that helps Windows users quickly move and organize **photos, music, and videos** from any drive to a designated folder. It’s safe, fast, and easy to use.

---

## Features

- Move **Photos, Music, Videos, or All Media** at once  
- **Custom destination folder** support  
- **Live output log** showing each file moved  
- Skips **system and program folders** for safety  
- Automatically **renames duplicates** to avoid overwriting  
- **Gradio UI** for a simple, interactive interface  

---

## Demo

### 1️⃣ Launch the App

Open the script, and the Gradio interface will appear in your browser.

 <img width="828" height="457" alt="cmd screenshot" src="https://github.com/user-attachments/assets/59c0922d-b7e7-483e-8ce7-e1c629c6badb" />


### 2️⃣ Select Options

- Enter the **drive path** (e.g., `D:\`)  
- Choose the **destination folder**  
- Select the **media type**  

 <img width="1918" height="1178" alt="gadio screenshoy" src="https://github.com/user-attachments/assets/1a1d14b8-1f8a-4432-8719-d3a7f065b1f1" />



### 3️⃣ Start Moving Files

Click **Start Moving Files** to begin. The output box will show a **live log** of files as they are moved.

 <img width="1918" height="1178" alt="after gadio screeenshot" src="https://github.com/user-attachments/assets/86297e1b-7437-425e-8199-ef6922b4a31d" />

 
---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/media-organizer.git
cd media-organizer
```

2. Install dependencies:
```bash
pip install gradio
```

3. Run the script:
```bash
python media_organizer.py
```

---

## Usage

1. Open the Gradio interface in your browser.  
2. Enter the **drive path** to scan.  
3. Choose the **destination folder**.  
4. Select the **media type** (Photos, Music, Videos, or All).  
5. Click **Start Moving Files**.  
6. Watch the **live output log** for progress.  

---

## Tech Stack

- Python  
- Gradio  
- Standard Libraries: `os`, `shutil`  

---

## License

MIT License © [Narendra Yadav]
