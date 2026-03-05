import logging
import requests

# 1. Logging 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("api_fetch.log"),
        logging.StreamHandler()
    ]
)

def fetch_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    try:
        response = requests.get(url, timeout=5)
        status = response.status_code
        
        if status == 200:
            try:
                # Handle JSON parsing
                data = response.json()
                # Defensive coding for NoneType slicing error
                title = data.get('title', 'No title')
                logging.info(f"Success: Post ID {post_id} - Title: {title[:20]}...")
            except ValueError:
                # Handle JSON parsing failure
                logging.error(f"Invalid JSON response for Post ID {post_id}")
        else:
            # Handle non-200 status codes
            logging.warning(f"Request failed (Status: {status}) for Post ID {post_id}")

    except Exception as e:
        # System/Network errors
        logging.error(f"System Error: {e}")

if __name__ == "__main__":
    print("--- API Fetching System ---")
    pid = input("Enter Post ID (1-100): ")
    
    if pid.isdigit():
        fetch_post(int(pid))
    else:
        # User input error is a warning, not a system error
        logging.warning(f"Invalid input: '{pid}' is not a number.")