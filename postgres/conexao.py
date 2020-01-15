import psycopg2

class Connection():

    def get_connection(self):
        connection = psycopg2.connect(user="postgres",
                                      password="1712",
                                      host="localhost",
                                      port="5432",
                                      database="python_postgres")
        return connection
