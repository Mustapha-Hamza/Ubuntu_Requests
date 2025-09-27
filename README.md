# Ubuntu_Requests

# Ubuntu-Inspired Image Fetcher 🖼️

> *"I am because we are"* — Ubuntu Philosophy  

This project is a simple Python tool that demonstrates the spirit of Ubuntu by connecting to the global web community, respectfully fetching shared images, and organizing them for later appreciation.  

---

## 🌍 Project Overview
The script prompts the user for an **image URL**, downloads it using the `requests` library, and saves it into a directory called **`Fetched_Images`**.  

It follows four Ubuntu-inspired principles:
- **Community**: Connects to the wider web community by fetching resources.  
- **Respect**: Handles errors gracefully instead of crashing.  
- **Sharing**: Organizes images neatly in a folder for reuse.  
- **Practicality**: Provides a real, usable tool.  

---

## ⚡ Features
- Prompt user for an image URL  
- Download image using `requests`  
- Auto-create `Fetched_Images` directory if it doesn’t exist  
- Extract filename from URL (or auto-generate one)  
- Save image in binary mode  
- Handle errors gracefully (HTTP errors, connection errors, etc.)  

---

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Ubuntu_Requests.git
   cd Ubuntu_Requests
