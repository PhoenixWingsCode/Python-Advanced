import requests
import json

# Fetch data from the API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    posts = response.json()
    print(json.dumps(posts[:5], indent=4))  # Show first 5 posts nicely formatted
else:
    print("Failed to retrieve data:", response.status_code)