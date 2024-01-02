import requests

endpoint1 = "http://localhost:8000/api/01/"
endpoint2 = "http://localhost:8000/api/02/"


get_response= requests.get(endpoint1)
print(get_response.text[:200])
print(get_response.json()['message'])
print(get_response.status_code)

get_response= requests.get(endpoint2, params={"abc": 123}, 
                           json={"query": "Hello World"})
# print(get_response.text[:200])
# print(get_response.status_code)
print(get_response.json())
