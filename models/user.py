import psycopg2
import bcrypt
from models import common,short

# def get_user_if_valid1(email,original_password):
#     results=common.sql_read(f"SELECT * FROM users WHERE email=%s;",[email])
#     if len(results):
#         user=results[0]
#         user_formatted={"id":user[0],"email":user[1],"name":user[2],"password_hash":user[3]}
#         #return user only if password match
#         if bcrypt.checkpw(original_password.encode(),user_formatted["password_hash"].encode()):
#             return user_formatted
#         return None
#     return None


# def add_user(email,name,original_password):
#     password_hash=bcrypt.hashpw(original_password.encode(),bcrypt.gensalt()).decode()
#     common.sql_write("INSERT INTO users (email,name,password_hash)VALUES(%s,%s,%s);",[email,name,password_hash])




class Users:
    def __init__(self,name=None,email=None,weddingDate=None,guestNum=0,budget=0,plain_password=None):
        self.name=name
        self.email=email
        self.plain_password=plain_password
        self.weddingDate=weddingDate
        self.guestNum=guestNum
        self.budget=budget
    


    def get_user_if_valid(self):
        results=common.sql_read("SELECT * FROM users WHERE email=%s;",[self.email])
        if len(results):
            user=results[0]
            user_formatted={"id":user[0],"email":user[1],"name":user[2],"weddingDate":user[3],"guestNum":user[4],"budget":user[5] ,"password_hash":user[6]}
            
            #return user only if password match
            #if bcrypt.checkpw(self.plain_password.encode(),user_formatted['password_hash'].encode()):
            print(self.plain_password)
            print(user_formatted)
            print(user_formatted['password_hash'])
            password_check=bcrypt.checkpw(self.plain_password.encode(),user_formatted['password_hash'].encode())     
            if password_check == True:
                return user_formatted
            return None

        return None


    def add_user(self):
        password_hash=bcrypt.hashpw(self.plain_password.encode(),bcrypt.gensalt()).decode()
        common.sql_write("INSERT INTO users (email,name,weddingDate,guestNum,budget,password_hash)VALUES(%s,%s,%s,%s,%s,%s);",[self.email,self.name, self.weddingDate,self.guestNum,self.budget,password_hash])

