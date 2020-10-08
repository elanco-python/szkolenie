import psycopg2

#############################################
def connect_db():
    connection = psycopg2.connect(
        user="", password="",
        host="", database="", port="5432"
    )
    connection.set_session(autocommit=False, readonly=False)
    cursor = connection.cursor()
    return connection, cursor
#############################################