from flask import Flask,render_template,request,session,redirect

import psycopg2
import bcrypt
from models import short,common,add_edit_venue,user,user_match_list


import os
db_password=os.getenv('DATABASE_PASSWORD')



app=Flask(__name__)
app.config["SECRET_KEY"] = db_password



@app.route('/')
def home():
    results=short.main_short()
    venue_cate=[]
    for r in results:
        venue_cate.append(r)

    return render_template('home_page.html',venue_cate=venue_cate)

@app.route('/venue_list')
def venue_list():
    category = request.args.get('category')  # Access the value of the "category" query parameter

    results = common.sql_read("SELECT category_name FROM category_list")
    for category_name in results:
        for c_name in category_name:
            if c_name == category:

                each_venue_list = common.sql_read(f"SELECT * FROM category_list WHERE category_name='{c_name}'")

                category_name = c_name
                venue_list = []
                for each in each_venue_list:
                    venue_list.append(each)
                return render_template("venue_list.html", list=venue_list, category_name=category_name, table_name=category)
            



# @app.route('/Winery')
# def winery_page():
#     table_name="winery_list_table"
#     each_venue_list=short.each_list("winery_list_table")
#     category_name='Winery'
#     winery_list=[]
#     for each in each_venue_list:
#         winery_list.append(each)
#     return render_template("venue_list.html",list=winery_list,category_name=category_name,table_name=table_name)


# @app.route('/City')
# def city_page():
#     table_name='city_venue_list_table'
#     each_venue_list=short.each_list("city_venue_list_table")
#     category_name='City'
#     city_list=[]
#     for each in each_venue_list:
#         city_list.append(each)
#     return render_template("venue_list.html",list=city_list,category_name=category_name,table_name=table_name)

# @app.route('/Waterfront')
# def waterfront_page():
#     table_name='waterfront_list_table'
#     each_venue_list=short.each_list('waterfront_list_table')
#     category_name='Waterfront'
#     waterfront_list=[]
#     for each in each_venue_list:
#         waterfront_list.append(each)
#     return render_template("venue_list.html",list=waterfront_list,category_name=category_name,table_name=table_name)

# @app.route('/Historic')
# def historic_list():
#     table_name='historic_list_table'
#     each_venue_list=short.each_list('historic_list_table')
#     category_name='Historic'
#     historic_list=[]
#     for each in each_venue_list:
#         historic_list.append(each)
#     return render_template("venue_list.html",list=historic_list,category_name=category_name,table_name=table_name)

# @app.route('/Unique')
# def unique_list():
#     table_name='unique_list_table'
#     each_venue_list=short.each_list('unique_list_table')
#     category_name='Unique'
#     unique_list=[]
#     for each in each_venue_list:
#         unique_list.append(each)
#     return render_template("venue_list.html",list=unique_list,category_name=category_name,table_name=table_name)


@app.route('/authorizer_login')
def authorizer_form():
    return render_template('authorizer_login.html')

@app.route('/authorizer_login_check',methods=["POST"])
def authorizer_check():
    input_name=request.form.get('name')
    input_password=request.form.get('password')
    authorizer_name=short.authorizer_login('WHERE name=%s',[input_name])
    authorizer_password=short.authorizer_login('WHERE password=%s',[input_password])
    if  authorizer_name and authorizer_password:
        session["user_id"]=authorizer_name['id']
        name=authorizer_name['name']
        password=authorizer_name['password']

        return render_template('authorizer_page.html',name=name)
    else:
        return "I don't recognize you. You can't login this page"



@app.route('/authorizer_logout')
def admin_logout():
    session['user_id']=None
    return redirect ('/')


@app.route('/forms/add/venue_list')
def add_venue_list_form():
    return render_template('add_venue_list.html')


@app.route('/api/add/venue_list',methods=['POST'])
def api_add_venue_list():
    form=request.form
    new_venue=add_edit_venue.Venue_adj(
        category_name=request.form.get('category_name'),
        name=request.form.get('venue_name'),
        img_pic=request.form.get('venue_img'),
        location=request.form.get('location'),
        overview=request.form.get('overview'),
        avg_price=request.form.get('avg_price'),
        avg_ppl=request.form.get('avg_guest'),
    )
    new_venue.add_venue_list()
    return redirect("/")


@app.route('/check/venue/category')
def check_venue_category():
    results = common.sql_read("SELECT name FROM category_list")
  
    venue_name = [element[0] for element in results]
    return render_template('check_category.html',show_category=venue_name)


@app.route('/forms/edit/venue_list',methods=["POST"])
def edit_venue_list_form():
    # category_name=request.form.get('category_name')
    id_input=request.form.get('id')
    venue_name_select=request.form.get('venue_name')

    # is_valid=common.sql_read(f"SELECT * FROM {table_name}")
    # if int(id_input) <= int(len(is_valid)):
    #     item=common.sql_read(f"SELECT * FROM {table_name} WHERE id={id_input}")
    #     return render_template("edit_venue_list.html",table_name=table_name,item=item,id=id_input)
    # else:
    #     return """<h2>The id is not valid</h2><br>
    #             <a href="/check/venue/category">back to select category/id</a> """
    item=common.sql_read(f"SELECT * FROM category_list WHERE name='{venue_name_select}'")
    return render_template("edit_venue_list.html",item=item,venue_name_select= venue_name_select)


@app.route('/api/edit/venue_list',methods=["POST"])
def api_venue_list():
    category_name=request.form.get('postName')
    id=request.form.get('postId')
    form=request.form
    print(id,category_name)
    edit_venue=add_edit_venue.Venue_adj(id)
    edit_venue.update_venue_list(form.get('venue_category') ,form.get('venue_name'),form.get('venue_img'),form.get('location'),form.get('overview'),form.get('avg_price'),form.get('avg_guest'),)
    return redirect('/')

 #####this is code without using class venue_adj #####
    # connection=psycopg2.connect(dbname="venue",user="postgres" ,host="127.0.0.1" ,password=db_password)
    # cursor=connection.cursor()
    
    # table_name=request.form.get('postName')
    # id=request.form.get('postId')

    # new_name=request.form.get('venue_name')
    # new_img_pic=request.form.get('venue_img')
    # new_location=request.form.get('location')
    # new_overview=request.form.get('overview')
    # new_avg_price=request.form.get('avg_price')
    # new_avg_ppl=request.form.get('avg_guest')
    # check=cursor.execute(f"SELECT * FROM {table_name} Where id=9")
    # # edit_list=cursor.execute("""
    # # UPDATE winery_list_table SET name=%s,img_pic=%s,location=%s,overview=%s,avg_price=%s,avg_ppl=%s WHERE id=%s""",
    # # (new_name,new_img_pic,new_location,new_overview,new_avg_price,new_avg_ppl,id))
    # connection.commit()
    # connection.close()
    # #return redirect('/home')
    

@app.route('/delete/venue')
def delete_venue():
    results = common.sql_read("SELECT name FROM category_list")
    venue_name = [element[0] for element in results]
    return render_template('delete_choose.html',venue_name=venue_name)

@app.route('/delete/check',methods=["POST"])
def delete_check():
    venue_name=request.form.get('venue_name')
    id=common.sql_read(f"SELECT id FROM category_list WHERE name='{venue_name}'")

    # item_name=common.sql_read(f'SELECT * FROM {category_name} WHERE id={id}')
    item_name=common.sql_read(f'SELECT * FROM category_list WHERE id={id[0][0]}')
    return render_template('delete_confirm.html',category_name=venue_name,id=id[0][0],item=item_name)


@app.route('/api/delete/venue',methods=["POST"])
def delete_confirm():
    form=request.form
    delete_submit=add_edit_venue.Venue_adj(
            # form.get('postName'),
            form.get("postId"),      
    )
    check=delete_submit.delete_venue()
######blow code without using class code#####
    # table_name=request.form.get('postName'),
    # id=request.form.get("postId"), 
    # results=common.simple(f"DELETE FROM {table_name[0]} WHERE id={id[0]} ")
    return redirect('/')
    



@app.route('/login')
def user_login_form():
    return render_template('user_login.html')


@app.route('/login', methods=["POST","GET"])
def login_action():
    email = request.form.get('user_email')
    plain_text_password = request.form.get('user_password')

    curr_user = user.Users(email=email, plain_password=plain_text_password)
    user_info = curr_user.get_user_if_valid()

    if user_info:
        session["user_id"] = user_info['id']
        session['user_name'] = user_info['name']
        return redirect('/my_page')
    else:
        return f"Wrong email or password . You input email :{email}, password:{plain_text_password}"



@app.route('/user_logout')
def user_logout():
    session['user_id']=None
    return redirect ('/')



@app.route('/sign_up')
def form_sign_up():
    return render_template('sign_up_form.html')


@app.route('/sign_up',methods=["POST"])
def create_user(): 
    name=request.form.get('user_name')
    email=request.form.get('user_email')
    date=request.form.get('wedding_date')
    guests=request.form.get('user_guest')
    budget=request.form.get('user_budget')
    password=request.form.get('user_password')

    
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    isValidPassword = bcrypt.checkpw(password.encode(), hashed_password.encode())
    common.sql_write("INSERT INTO users (email,name,weddingDate,guestNum,budget,password_hash)VALUES(%s,%s,%s,%s,%s,%s);",[email,name,date,guests,budget,hashed_password])
    results=common.sql_read("SELECT * FROM users WHERE email=%s;",[email])
    
    return  f"""
    <p> Hi {results[0][2]}. Your email :{results[0][1]} Your password:{password}</p><br>
    <p>Check more<a href="/">menu</a></p>
     <p>Is this valid password? {isValidPassword}</p> """



@app.route('/my_page', methods=["POST", "GET"])
def goto_user_page():
 
    who_is_user = common.sql_read(f'SELECT * FROM users WHERE id={session["user_id"]}')
    user_like_list = common.sql_read(f'SELECT * FROM like_table WHERE user_id={session["user_id"]}')
    print(f'This is user_like_listP{user_like_list}')
    
   
    ###This is before adjust code
    # liked_venues = []
    # for  liked in user_like_list :
    #     table_name=liked[2]
    #     venue_id=liked[3]
    #     venue = common.sql_read(f'SELECT * FROM {table_name} WHERE id={venue_id}')
    #     venue.append(table_name)
    #     liked_venues.append(venue)
   
    liked_venues = []
    for  liked in user_like_list :
        print(liked)
        category_name=liked[2]
        venue_name=liked[3]
        print(f"how come not insert?{venue_name}")
        venue = common.sql_read(f"SELECT * FROM category_list WHERE name='{venue_name}'")
        print(venue)
        venue.append(category_name)
        liked_venues.append(venue)

    return render_template('user_page.html',user=who_is_user, liked_venues=liked_venues,user_like_list=user_like_list)



    
# This is before adjust 
# @app.route('/like',methods=["POST"])
# def like_page():
#     venue_id=request.form.get('like_btn')
#     table_name=request.form.get('postName')
#     session['venue_id']=venue_id
#     session['table_name']=table_name
    
#     results=common.sql_write("INSERT INTO like_table ( user_id, like_table_name,like_table_venue_id) VALUES(%s,%s,%s);",[session["user_id"],session['table_name'],session['venue_id']])  
#     return redirect('/my_page')
   

@app.route('/like',methods=["POST"])
def like_page():
    venue_name=request.form.get('like_btn')
    
    category_name=request.form.get('postName')
  
    session['venue_name']=venue_name
    print(f"This is venue name:{session['venue_name']}")
    session['category_name']=category_name
    print(f"This is category name:{session['category_name']}")

    results=common.sql_write("INSERT INTO like_table ( user_id, like_category_name,likeUnique_name) VALUES(%s,%s,%s);",[session["user_id"],session['category_name'],session['venue_name']])  
    print(f'return like{results}')
    return redirect('/my_page')
   




@app.route('/delete_liked',methods=["POST"])
def delete_liked_list():
    delete_btn=request.form.get("delete_liked_btn")
    print(f'this is id: {delete_btn}')
    #delete_venue=common.simple(f'SELECT * FROM like_table WHERE user_id={session["user_id"]}')
    bye=common.simple(f"DELETE FROM like_table WHERE  id={delete_btn}")
    return redirect('/my_page')
# @app.route('/like', methods=["POST"])
# def like_page():
#     venue_id = request.form.get('like_btn')
#     table_name = request.form.get('postName')
#     session['venue_id']=venue_id
    
#     if table_name == "winery_list_table":
#         session['table_name']=table_name
#         results = common.sql_write("INSERT INTO likes (user_id, winery_id) VALUES (%s, %s);", [session["user_id"], venue_id])
        
#     elif table_name == "city_venue_list_table":
#         session['table_name']=table_name
#         results = common.sql_write("INSERT INTO likes (user_id, city_id) VALUES (%s, %s);", [session["user_id"], venue_id])
        
#     elif table_name == "waterfront_list_table":
#         session['table_name']=table_name
#         results = common.sql_write("INSERT INTO likes (user_id, waterfront_id) VALUES (%s, %s);", [session["user_id"], venue_id])
        
#     elif table_name == "historic_list_table":
#         session['table_name']=table_name
#         results = common.sql_write("INSERT INTO likes (user_id, historic_id) VALUES (%s, %s);", [session["user_id"], venue_id])
        
#     elif table_name == "unique_list_table":
#         session['table_name']=table_name
#         results = common.sql_write("INSERT INTO likes (user_id, unique_id) VALUES (%s, %s);", [session["user_id"], venue_id])

#     return redirect('/my_page')




if __name__ =="__main__":
    app.run(debug=True,port=os.getenv("PORT", default=5000))