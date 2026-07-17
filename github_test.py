import requests

url = "https://api.github.com/search/repositories?q=data-engineering"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(data["items"][0]["full_name"])
