from nameko.extensions import DependencyProvider
import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling


class DatabaseWrapper:
    connection = None

    def __init__(self, connection):
        self.connection = connection

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
    
    def get_id(self,email,password):
        cursor = self.connection.cursor(dictionary=True)
        result=[]
        sql="SELECT * FROM student_data where email='%s' and password='%s'", (email,password)
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'session_id':'',
                'id': row['id'],
                'email': row['email']
            })
        self.connection.commit()
        # result=cursor.fetchone()
        cursor.close()
        return result

    def upload_file(self, id, file):
        # check if user already exist
        cursor = self.connection.cursor(dictionary=True)

        cursor.execute("""
        INSERT INTO student_file (id,file)
        VALUES (%s, %s);
        """, (id,file))
        cursor.close()
        self.connection.commit()
        return "File berhasil di upload!"

    def __del__(self):
        self.connection.close()


class DatabaseProvider(DependencyProvider):

    connection_pool = None

    def setup(self):
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="database_pool",
                pool_size=32,
                pool_reset_session=True,
                host='127.0.0.1',
                database='student',
                user='root',
                password=''
            )
        except Error as e:
            print("Error while connecting to MySQL using Connection pool ", e)

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())