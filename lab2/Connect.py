import psycopg2

#Function that returns connection to DB
def makeConnect():
    return psycopg2.connect(
        user="postgres",
        password="oleg1998kira",
        host="127.0.0.1",
        port="5432",
        database="systemOperator",
    )
#Function that closes connection to DB
def closeConnect(connection):
    connection.commit()
    connection.close()
