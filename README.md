# Smart File Organizer 📂

A Python-based command-line application that automatically organizes files into categorized folders based on their file extensions.

Instead of manually sorting files in a cluttered directory, Smart File Organizer scans the selected folder, identifies each file type, creates the required category folders, and moves the files automatically.

---

## ✨ Features

- 📁 Organize files from a user-selected folder
- 🔍 Detect file extensions automatically
- 🗂️ Categorize files into different folders
- 📦 Support archive files
- 💻 Support programming and coding files
- 🎵 Organize music files
- 🎬 Organize video files
- 🖼️ Organize image files
- 📄 Organize document files
- ❓ Move unsupported file types to `Others`
- 🔁 Handle duplicate filenames automatically
- 🛡️ Validate folder paths
- 📊 Display organization statistics
- 📋 Display supported file types
- 🧭 Interactive command-line menu

---

## 🛠️ Technologies Used

- **Python 3**
- `os`
- `shutil`

### Python concepts practiced

- Functions
- Loops
- Conditional statements
- Dictionaries
- Lists
- String manipulation
- Exception handling
- File and directory operations
- Path handling
- Return values
- Basic program architecture

---

## 📂 Supported File Types

|   Category   |                 Extensions                        |
|--------------|---------------------------------------------------|
| Images       | `.jpg`, `.png`, `.jpeg`, `.gif`, `.webp`, `.svg`  |
| Documents    | `.pdf`, `.txt`, `.docx`, `.doc`, `.xlsx`, `.pptx` |
| Music        | `.mp3`, `.wav`, `.flac`                           |
| Videos       | `.mp4`, `.mkv`, `.avi`, `.mov`                    |
| Coding Files | `.py`, `.c`, `.js`, `.cpp`, `.r`, `.html`         |
| Archives     | `.zip`, `.rar`, `.7z`                             |
| Others       | Unsupported extensions                            |

---

## 🚀 How It Works

The application follows a simple workflow:

```text
User selects a folder
        ↓
Program scans the folder
        ↓
File extension is detected
        ↓
Extension is matched to a category
        ↓
Category folder is created if needed
        ↓
Duplicate filename is checked
        ↓
File is moved to its category folder
        ↓
Statistics are updated