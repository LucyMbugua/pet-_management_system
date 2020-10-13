import psycopg2

# connect to a database
conn = psycopg2.connect(dbname="pet_system_db", user="postgres", password="ADMIN")

