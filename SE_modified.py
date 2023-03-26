import requests
import json
import random

# Define API endpoint for public data
API_ENDPOINT = "https://jsonplaceholder.typicode.com/todos"

# Define function to retrieve data from the API endpoint
def get_data():
    response = requests.get(API_ENDPOINT)
    data = json.loads(response.text)
    return data

# Define function to generate a random program for a given category
def generate_program(category):
    program = f"{category} program:\n"
    if category == "Theater":
        program += "Title: "
        program += " ".join([random.choice(["The", "A"]) + " " + random.choice(["Amazing", "Spectacular", "Incredible"]) + " " + random.choice(["Play", "Musical", "Performance"])])
        program += "\nDirector: "
        program += random.choice(["John", "Jane", "James"]) + " " + random.choice(["Smith", "Doe", "Johnson"])
        program += "\nDescription: "
        program += random.choice(["A heartwarming tale of love and loss", "A thrilling mystery set in ancient India", "A comedic romp through the streets of Mumbai"])
    elif
