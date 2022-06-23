from requests import get

response = get("https://swapi.dev/api/people/1")
print(response)
print(response.status_code)
print(response.text)
c = 0


