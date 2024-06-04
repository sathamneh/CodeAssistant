import psycopg2

try:
    conn = psycopg2.connect(
        dbname="qa_pilot_chatsession_db",
        user="postgres",
        password="Password",
        host="172.16.100.214"
    )
    print("Connection successful")
    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    print(f"Database version: {db_version}")
    cur.close()
    conn.close()
except psycopg2.Error as e:
    print(f"Error: {e}")
