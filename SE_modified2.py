import requests
import json

# Define API endpoint to retrieve data
API_ENDPOINT = "https://jsonplaceholder.typicode.com/posts"

def get_data():
    """
    Retrieves data from a public domain using API call.
    Returns a dictionary containing the response data.
    """
    response = requests.get(API_ENDPOINT)
    data = json.loads(response.content)
    return data

def display_data(data):
    """
    Displays data retrieved from the public domain.
    """
    for d in data:
        print(f"ID: {d['id']}")
        print(f"Title: {d['title']}")
        print(f"Body: {d['body']}")
        print("---------------")

def main():
    # Retrieve data from public domain
    data = get_data()

    # Display data
    display_data(data)

if __name__ == '__main__':
    main()
