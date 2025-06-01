# 🧹 Password Dictionary Filter GUI

A simple Python GUI tool to filter and sort password dictionaries (wordlists) based on length and character rules. Useful for cleaning up `.txt` wordlists used in security research, penetration testing, or personal use.

---

## 📦 Features

- 🗂 Choose a `.txt` file as input
- 🎯 Filter by:
  - Minimum and maximum password length
  - Only alphabetic / numeric / alphanumeric
  - Remove passwords with special characters
  - Remove duplicates
- 🔤 Sort by:
  - Alphabetical order
  - Password length
- 💾 Choose where to save the filtered file (with original filename)
- 📊 See how many passwords were filtered and kept

---

## 🖼️ Screenshot

![Alt text](https://github.com/user-attachments/assets/62495585-409c-430f-89ab-50a5d6315d3c)

---

## 🚀 Getting Started

### 1. Requirements

- Python 3.x
- `tkinter` (usually pre-installed)

To install `tkinter` on Ubuntu:

```bash
sudo apt update
sudo apt install python3-tk

```
### 2. How to run

```bash
python3 index.py
