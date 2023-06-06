import psycopg2

from models import common
import os
db_password=os.getenv('DATABASE_PASSWORD')

class Venue_adj:
     
    def __init__(self,id=0,category_name=None, name=None,img_pic=None,location=None,overview=None,avg_price=0,avg_ppl=0):
       
        self.id=id
        self.category_name=category_name
        self.name=name
        self.img_pic=img_pic
        self.location=location
        self.overview=overview
        self.avg_price=avg_price
        self.avg_ppl=avg_ppl

    def add_venue_list(self):
        common.sql_write("""
        INSERT INTO category_list(category_name,name, img_pic,location,overview,avg_price,avg_ppl) VALUES (%s,%s,%s,%s,%s,%s,%s)""",
        [self.category_name,self.name,self.img_pic,self.location,self.overview,self.avg_price,self.avg_ppl])
        

    #    def add_venue_list(self):
    #     common.sql_write("""
    #     INSERT INTO {}(name, img_pic,location,overview,avg_price,avg_ppl) VALUES (%s,%s,%s,%s,%s,%s,%s)""".format(self.table_name),
    #     [self.name,self.img_pic,self.location,self.overview,self.avg_price,self.avg_ppl])
        
    #####blow code is not using commit.sql_write ver
    # def add_venue_list(self):
    #     connection=psycopg2.connect(dbname="venue",user="postgres" ,host="127.0.0.1" ,password=db_password)
    #     cursor=connection.cursor()
    #     cursor.execute("""
    #     INSERT INTO {}(name, img_pic,location,overview,avg_price,avg_ppl) VALUES (%s,%s,%s,%s,%s,%s)""".format(self.table_name),
    #     [self.name,self.img_pic,self.location,self.overview,self.avg_price,self.avg_ppl])
    #     connection.commit()
    #     cursor.close()
    #     connection.close()

    

    # def update_venue_list(self,new_name,new_img_pic,new_location,new_overview,new_avg_price,new_avg_ppl):
    #     update_list=common.sql_write(f"""
    #     UPDATE {self.table_name} SET name=%s,img_pic=%s,location=%s,overview=%s,avg_price=%s,avg_ppl=%s WHERE id={self.id}""",
    #     (new_name,new_img_pic,new_location,new_overview,new_avg_price,new_avg_ppl))
     

    def update_venue_list(self,new_category_name,new_name,new_img_pic,new_location,new_overview,new_avg_price,new_avg_ppl):
        # UPDATE {self.table_name} SET category_name=%s,name=%s,img_pic=%s,location=%s,overview=%s,avg_price=%s,avg_ppl=%s WHERE id={self.id}""",
        update_list=common.sql_write(f"""
        
        UPDATE category_list SET category_name=%s,name=%s,img_pic=%s,location=%s,overview=%s,avg_price=%s,avg_ppl=%s WHERE id={self.id}""",
        [new_category_name,new_name,new_img_pic,new_location,new_overview,new_avg_price,new_avg_ppl])
     

    def delete_venue(self):
        common.simple(f"DELETE FROM category_list WHERE id={self.id}")
        
       