import psycopg2
import requests
from models import common




def main_short():
    results=common.sql_read("SELECT * FROM venue_category;") #get common.py sql_read function and use this for home() function.
    return results


####this code move to common.py = sql_read function
# def each_list(query):
#     connection=psycopg2.connect(dbname="venue",user="postgres" ,host="127.0.0.1" ,password="Misa5310101")
#     cursor=connection.cursor()
#     cursor.execute(query)
#     each_venue_list = cursor.fetchall()
#     connection.commit()
#     connection.close()
#     return each_venue_list

def each_list(table_name):
    each_venue_list=common.sql_read2("SELECT * FROM {}".format(table_name))
    return each_venue_list

# def authorizer_login(para):
#     results=common.sql_read("SELECT * FROM authorizer_table  WHERE  name={};".format(para))
#     if len(results):
#         authorizer=results[0]
#         return {"id":authorizer[0], "name":authorizer[1],"password":authorizer[2] }
#     return None
#
 
def authorizer_login(filter_clause,para):
    results=common.sql_read(f"SELECT *FROM authorizer_table {filter_clause};",para)
    if len(results):
        authorizer=results[0]
        return {"id":authorizer[0], "name":authorizer[1],"password":authorizer[2]}
    return None



