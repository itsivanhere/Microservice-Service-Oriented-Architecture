from nameko.extensions import DependencyProvider
import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
#import mysql.connector.pooling

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        self.connection = connection

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())

    ### CRUD TEMPLATE ###
    ### Feel free to remove or make changes ###

    def get_all_benefit(self): # get all benefit (pengecekan ketersediaan data benefit)
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = """SELECT * FROM benefit"""
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'name': row['name'],
                'description': row['description'],
                'point_required': row['point_required'],
                'discount': row['discount'],
                'start_date': row['start_date'],
                'end_date': row['end_date']
            })
        cursor.close()
        hasil={
            'status': 'success',
            'data': result
        }
        return hasil

    def get_benefit_by_id(self, id):  #get benefit by id
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = """
            SELECT * FROM benefit WHERE id = '{}'""".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        if result!=[]:
            hasil={
            'status': 'success',
            'data': result
        }
        else:
            hasil={
                'status': 'Error',
                'data': 'Benefit not found!'
            }
        return hasil

    # def get_room_type_by_name(self, name):
    #     cursor = self.connection.cursor(dictionary=True)
    #     result = []
    #     sql = """
    #         SELECT * FROM room_type WHERE name = '{}'
    #     """.format(name)
    #     cursor.execute(sql)
    #     result = cursor.fetchone()
    #     cursor.close()
    #     return result

    def benefit_data_entry(self, name, description, point_required,discount,start_date,end_date): # data entry benefit
        cursor = self.connection.cursor(dictionary=True)
        result=[]
        sql = """INSERT INTO benefit (id, name, description, point_required, discount, start_date, end_date)
            VALUES (DEFAULT,'{}', '{}', '{}', '{}', '{}', '{}')""".format(
            name, description, point_required,discount,start_date,end_date)
        cursor.execute(sql)
        self.connection.commit()
        result=cursor.fetchone()
        cursor.close()
        return result

    def edit_benefit_data(self, id, name, description, point_required, discount,start_date,end_date):
        cursor = self.connection.cursor(dictionary=True)
        result=[]
        sql = """
            UPDATE benefit
            SET name = '{}',
            description = '{}',
            point_required = '{}',
            discount = '{}',
            start_date = '{}',
            end_date = '{}'
            WHERE id = {}""".format(
            name, description, point_required, discount,start_date,end_date, id)
        cursor.execute(sql)
        self.connection.commit()
        result=cursor.fetchone()
        cursor.close()
        if result==[]:
            hasil={
            'status': 'success',
            'data': result
        }
        else:
            hasil={
                'status': 'Error',
                'data': 'Benefit not found!'
            }
        return hasil

    # def delete_room_type(self, id):
    #     cursor = self.connection.cursor(dictionary=True)
    #     sql = """
    #         DELETE FROM room_type
    #         WHERE id = {}""".format(id)
    #     cursor.execute(sql)
    #     self.connection.commit()
    #     cursor.close()
    
    ### START YOUR CODE HERE ###
    
    ### ...
    
    ### END YOUR CODE HERE ###

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
                database='catea_benefit',
                user='root',
                password=''
            )
        except Error as e:
            print("Error while connecting to MySQL using Connection pool ", e)

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())