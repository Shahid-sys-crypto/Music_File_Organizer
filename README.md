# 🎵 Music File Organizer (Python)

A simple **Music File Organizer** built using **Python** that scans a directory for music files, extracts metadata, organizes them by **Artist → Album**, and saves a summary in a JSON file.

---

## ✨ Features

- 🎶 Scans directories for music files
- 🏷️ Extracts metadata (Title, Artist, Album, Genre)
- 📂 Organizes music into folders by **Artist / Album**
- 💾 Moves files automatically to the organized structure
- 📄 Saves a metadata summary as `music_summary.json`
- 🧑‍💻 Command-line based and beginner-friendly

---

## 📁 Project Structure

Music_File_Organizer.py
music_summary.json
README.md


---

## 🛠️ Requirements

- Python **3.x**
- `mutagen` library (for reading audio metadata)

Install the required library using:
pip install mutagen


---

## ▶️ How to Run

1. Download or clone the project
2. Open terminal / command prompt
3. Navigate to the project directory
4. Run the program:

python Music_File_Organizer.py


5. Enter:
   - Path to the directory containing music files
   - Path where organized music should be stored

---

## 🧠 How It Works

### Music Scanning

- Recursively scans directories for:
  - `.mp3`
  - `.flac`
  - `.wav`

### Metadata Extraction

- Uses the `mutagen` library to extract:
  - Title
  - Artist
  - Album
  - Genre
- Unknown fields are labeled as `"unknown"`

### File Organization

Files are organized in the following structure:

Output_Directory/
├── Artist Name/
│ ├── Album Name/
│ │ ├── song1.mp3
│ │ ├── song2.mp3


### Metadata Summary

- A JSON file (`music_summary.json`) is generated containing metadata of all detected music files

---

## 📄 Sample `music_summary.json`

```json
[
    {
        "title": "Song Name",
        "album": "Album Name",
        "genre": "Pop",
        "artist": "Artist Name"
    }
]
🧩 Technologies Used
Python

os and shutil modules

mutagen library

json module

🚀 Future Enhancements
Support for more audio formats

GUI version using Tkinter

Option to copy instead of move files

Album artwork extraction

Playlist generation

👤 Author
Shahid Farhan
Python automation mini-project for music organization.


If you want, I can:
- Combine **all your projects into one GitHub portfolio README**
- Write a **college mini-project report**
- Add **logging and error handling**
- Build a **GUI music organizer**
