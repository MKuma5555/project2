import psycopg2
import os
db_password=os.getenv('DATABASE_PASSWORD')

def sql_read(query,parameters=[]):
    connection=psycopg2.connect(dbname="venue",user="postgres" ,host="127.0.0.1" ,password=db_password)
    cursor=connection.cursor()
    cursor.execute(query,parameters)
    results = cursor.fetchall()
    connection.close()
    return results


def sql_read2(query):
    connection=psycopg2.connect(dbname="venue",user="postgres" ,host="127.0.0.1" ,password=db_password)
    cursor=connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results



def sql_write(query,parameters=[]):
    connection=psycopg2.connect(dbname="venue",user="postgres" ,host="127.0.0.1" ,password=db_password)
    cursor=connection.cursor()
    cursor.execute(query,parameters)
    connection.commit()
    connection.close()
    