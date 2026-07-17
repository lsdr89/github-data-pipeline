import requests

url = "https://api.github.com/search/repositories?q=data-engineering"

response = requests.get(url)

data = response.json()

for repo in data["items"][:10]:

    print(repo["full_name"])
    print(repo["stargazers_count"])
    print(repo["forks_count"])
    print(repo["language"])

    print("------")
