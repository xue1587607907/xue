import pymysql

class Utilsaa:
    @classmethod
    def get_conn(cls):
        conn= pymysql.connect(host="localhost",port=3306,user="root",password="123456",charset="utf8",database="test")
        return conn
    @classmethod
    def get_cursor(cls,conn):
       return conn.cursor()

    @classmethod
    def close(cls,cursor,conn):
        if cursor:
            cursor.close()
        if conn:
            conn.close()

