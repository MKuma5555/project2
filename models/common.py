import psycopg2
import os
db_password=os.getenv('DATABASE_PASSWORD')

print(dict(name=os.getenv('DBNAME'),user=os.getenv('DBUSER') ,host=os.getenv('DBHOST') ,password=db_password,port=os.getenv('DBPORT')))

def sql_read(query,parameters=[]):
    connection=psycopg2.connect(dbname=os.getenv('DBNAME'),user=os.getenv('DBUSER') ,host=os.getenv('DBHOST') ,password=db_password,port=os.getenv('DBPORT'))
    cursor=connection.cursor()
    cursor.execute(query,parameters)
    results = cursor.fetchall()
    connection.close()
    return results


def sql_read2(query):
    connection=psycopg2.connect(dbname=os.getenv('DBNAME'),user=os.getenv('DBUSER') ,host=os.getenv('DBHOST') ,password=db_password,port=os.getenv('DBPORT'))
    cursor=connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results



def sql_write(query,parameters=[]):
    connection=psycopg2.connect(dbname=os.getenv('DBNAME'),user=os.getenv('DBUSER') ,host=os.getenv('DBHOST') ,password=db_password,port=os.getenv('DBPORT'))
    cursor=connection.cursor()
    try:

        cursor.execute(query,parameters)
        connection.commit()
        connection.close()
        return "success"
    except Exception as e:
        error_type = type(e).__name__
        error_msg = str(e)
        error_detail = f"{error_type}: {error_msg}"
        connection.rollback()
        return f"Error inserting data into database: {error_detail}"
    
   


def simple(query):
    connection=psycopg2.connect(dbname=os.getenv('DBNAME'),user=os.getenv('DBUSER') ,host=os.getenv('DBHOST') ,password=db_password,port=os.getenv('DBPORT'))
    cursor=connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()