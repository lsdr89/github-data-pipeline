import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="githubdb",
    user="postgres",
    password="postgres"
)

print("Conectado!")

conn.close()
