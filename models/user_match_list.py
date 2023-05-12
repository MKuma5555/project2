import psycopg2
import bcrypt
from models import common,short


class Match:
 def __init__(self,name=None,email=None,weddingDate=None,guestNum=0,budget=0,plain_password=None):
        self.name=name
        self.email=email
        self.plain_password=plain_password
        self.weddingDate=weddingDate
        self.guestNum=guestNum
        self.budget=budget

def user_match_list(self):
    table_name_list=["winery_list_table","city_venue_list_table","waterfront_list_table","historic_list_table","unique_list_table"]
    for table_name in table_name_list:
        print(table_name)
    check_match=common.sql_read(f"SELECT * FROM {table_name} ")

    user=common.sql_read("SELECT * FROM users WHERE id=%s",session["user_id"])

    if check_match['avg_price'] <= user['budget']:
        return f"{check_match['avg_price']}"
    if check_match['']:
        return None 




class Like_btn_list:
        def __init__(self,table_name=None,id=0,name=None,img_pic=None):
            self.table_name=table_name
            self.id=id
            self.name=name
            self.img_pic=img_pic
        
           

        def liked_venue_list(self):
            
            common.sql_write("""
            INSERT INTO like_list (name, img_pic) VALUES (%s,%s)""",[self.name,self.img_pic])
            
            