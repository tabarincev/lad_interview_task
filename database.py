import psycopg2

from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Database:
    def __init__(self, user, password, host, port, dbname):
        self.connection = self.get_connection(user, 
                                              password,
                                              host, 
                                              port,
                                              dbname)
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor()

    def get_connection(self, user, password, host, port, dbname):
        try:
            connection = psycopg2.connect(user=user,
                                          password=password,
                                          host=host,
                                          port=port,
                                          dbname=dbname)
            return connection
        except (Exception, Error) as error:
            print("Ошибка при подключении -", error)
    
    def insert_into_table(self, sql_query):
        try:
            self.cursor.execute(sql_query)
        except (Exception, Error) as error:
            print('Ошибка вставки -', error)
            