import requests
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="githubdb",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

url = "https://api.github.com/search/repositories?q=data-engineering"

data = requests.get(url).json()

for repo in data["items"][:10]:

    cursor.execute(
        """
        INSERT INTO repositories
        (repo_name, stars, forks, language)
        VALUES (%s,%s,%s,%s)
        """,
        (
            repo["full_name"],
            repo["stargazers_count"],
            repo["forks_count"],
            repo["language"]
        )
    )

conn.commit()

cursor.close()
conn.close()

print("Dados inseridos")
