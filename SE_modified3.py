import requests
import json

# Define API endpoint to retrieve data
API_ENDPOINT = "https://jsonplaceholder.typicode.com/posts"

def get_data(endpoint):
    """
    Retrieves data from a public domain using API call.
    Returns a dictionary containing the response data.
    """
    response = requests.get(endpoint)
    data = json.loads(response.content)
    return data

def display_data(data):
    """
    Returns data retrieved from the public domain.
    """
    return data

def test_get_data():
    """
    Tests the get_data() function with a test API endpoint.
    """
    test_endpoint = "https://jsonplaceholder.typicode.com/comments"
    expected_result = [{'postId': 1, 'id': 1, 'name': 'id labore ex et quam laborum', 'email': 'Eliseo@gardner.biz', 'body': 'laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium'}, {'postId': 1, 'id': 2, 'name': 'quo vero reiciendis velit similique earum', 'email': 'Jayne_Kuhic@sydney.com', 'body': 'est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et'}, {'postId': 1, 'id': 3, 'name': 'odio adipisci rerum aut animi', 'email': 'Nikita@garfield.biz', 'body': 'quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione'}, {'postId': 1, 'id': 4, 'name': 'alias odio sit', 'email': 'Lew@alysha.tv', 'body': '
