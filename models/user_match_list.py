import psycopg2
import bcrypt
from models import common,short



# class Users:
#     def __init__(self,name=None,img_pic=None,
#                     location=None,
#                     overview=None,
#                     avg_price=0,
#                     avg_ppl=0):
#         self.name=name
#         self.img_pic=img_pic
#         self.location=location
#         self.overview=overview
#         self.avg_price=avg_price
#         self.avg_ppl=avg_ppl


def budget_match(self):
    table_name_list=["winery_list_table","city_venue_list_table","waterfront_list_table","historic_list_table","unique_list_table"]
    for table_name in table_name_list:
        print(table_name)
    match_budget=common.sql_read(f"SELECT * FROM {table_name} ")