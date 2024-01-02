import requests

endpoint1 = "https://httpbin.org/"
endpoint2 = "https://httpbin.org/anything"
endpoint3 = "https://httpbin.org/status/200"


#HTML
get_response= requests.get(endpoint1)
print(get_response.text[:200])

print("\n========\n")

#JSON
get_response= requests.get(endpoint2)
print(get_response.json())

print("\n========\n")

#JSON
get_response= requests.get(endpoint2, 
                           json={"query": "Hello World"})
print(get_response.json())

print("\n========\n")

#JSON
get_response= requests.get(endpoint2)
print(get_response.status_code)

print("\n========\n")

#JSON
get_response= requests.get(endpoint3)
print(get_response)
