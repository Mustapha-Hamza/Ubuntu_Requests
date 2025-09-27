import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Prompt the user for an image URL
    url = input("Enter the URL of an image: ").strip()

    # Create directory if it doesn't exist
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Send HTTP GET request
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)

        # Try to extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename found, generate a unique one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Save path
        filepath = os.path.join(folder, filename)

        # Save the image in binary mode
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✅ Image successfully fetched and saved as: {filepath}")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"❌ Connection error: {req_err}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    fetch_image()
