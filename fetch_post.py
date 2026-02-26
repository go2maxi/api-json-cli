import requests

def fetch_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.get(url, timeout=5)
        print(f"\n[Status Code]: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success: {data.get('title')}")
        else:
            print("⚠️ Error: Resource not found. (404 Not Found)")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("--- API Fetching Test Start ---")
    pid = input("Enter Post ID to fetch (1-100): ")
    if pid.isdigit():
        fetch_post(pid)
    else:
        print("❌ Please enter a number.")