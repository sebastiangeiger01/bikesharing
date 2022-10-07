import psycopg2
from flask import Flask

app = Flask(__name__)

def get_users():
    """ query data from the users table """
    conn = None
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='db' password='example'")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        result = "The number of users: " + str(cur.rowcount) + "\n"
        row = cur.fetchone()

        while row is not None:
            result += str(row) + "\n"
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return result

@app.route('/')
def hello():
    users = get_users()
    return 'Hello World! I have the following users in my database: ' + users