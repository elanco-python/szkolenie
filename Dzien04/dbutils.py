
import psycopg2


#############################################
def connect_db():
    connection = psycopg2.connect(
        user="elanco_user", password="elanco_pass",
        host="51.91.120.89", database="elanco", port="5432"
    )
    connection.set_session(autocommit=False, readonly=False)
    cursor = connection.cursor()
    return connection, cursor
#############################################