from flask import Flask,render_template,request,session,redirect

import psycopg2
import bcrypt
from models import short,common,add_edit_venue,user




import os
db_password=os.getenv('DATABASE_PASSWORD')



app=Flask(__name__)
app.config["SECRET_KEY"] = db_password



@app.route('/home')
def home():
    # results=short.main_short("SELECT * FROM venue_category;")
    results=short.main_short()
    venue_cate=[]
    for r in results:
        venue_cate.append(r)
    return render_template('home_page.html',venue_cate=venue_cate)


@app.route('/Winery')
def winery_page():
    each_venue_list=short.each_list("winery_list_table")
    category_name='Winery'
    winery_list=[]
    for each in each_venue_list:
        winery_list.append(each)
    return render_template("venue_list.html",list=winery_list,category_name=category_name)


@app.route('/City')
def city_page():
    each_venue_list=short.each_list("city_venue_list_table")
    category_name='City'
    city_list=[]
    for each in each_venue_list:
        city_list.append(each)
    return render_template("venue_list.html",list=city_list,category_name=category_name)

@app.route('/Waterfront')
def waterfront_page():
    each_venue_list=short.each_list('waterfront_list_table')
    category_name='Waterfront'
    waterfront_list=[]
    for each in each_venue_list:
        waterfront_list.append(each)
    return render_template("venue_list.html",list=waterfront_list,category_name=category_name)

@app.route('/Historic')
def historic_list():
    each_venue_list=short.each_list('historic_list_table')
    category_name='Historic'
    historic_list=[]
    for each in each_venue_list:
        historic_list.append(each)
    return render_template("venue_list.html",list=historic_list,category_name=category_name)

@app.route('/Unique')
def unique_list():
    each_venue_list=short.each_list('unique_list_table')
    category_name='Unique'
    unique_list=[]
    for each in each_venue_list:
        unique_list.append(each)
    return render_template("venue_list.html",list=unique_list,category_name=category_name)

# @app.route('/each/venue/category/list<category_name>')
# def each_list():
#     table_name=
#     each_venue_list=short.each_list(table_name)
#     category_name='Historic'
#     historic_list=[]
#     for each in each_venue_list:
#         historic_list.append(each)
#     return render_template("venue_list.html",list=historic_list,category_name=category_name)




@app.route('/authorizer_login')
def authorizer_form():
    return render_template('authorizer_login.html')

@app.route('/authorizer_login_check',methods=["POST"])
def authorizer_check():
    input_name=request.form.get('name')
    input_password=request.form.get('password')

    # authorizer_password=short.authorizer_login("WHERE password=%s",[float(input_password)])
    authorizer_name=short.authorizer_login('WHERE name=%s',[input_name])
   

    if  authorizer_name:
        session["user_id"]=authorizer_name['id']
        name=authorizer_name['name']
        password=authorizer_name['password']

        return render_template('authorizer_page.html',name=name)
    else:
        return "I don't recognize you. You can't login this page"



@app.route('/authorizer_logout')
def admin_logout():
    session['user_id you']=None
    return redirect ('/home')


@app.route('/forms/add/venue_list')
def add_venue_list_form():
    return render_template('add_venue_list.html')


@app.route('/api/add/venue_list',methods=['POST'])
def api_add_venue_list():
    form=request.form
    new_venue=add_edit_venue.Venue_adj(
        table_name=request.form.get('category_name'),
        name=request.form.get('venue_name'),
        img_pic=request.form.get('venue_img'),
        location=request.form.get('location'),
        overview=request.form.get('overview'),
        avg_price=request.form.get('avg_price'),
        avg_ppl=request.form.get('avg_guest'),
    )
    new_venue.add_venue_list()
    ###Blow code is not using class ADD_venue ver#####
    # category=request.form.get('category_name')
    # venue_name=request.form.get('venue_name')
    # venue_img=request.form.get('venue_img')
    # location=request.form.get('location')
    # overview=request.form.get('overview')
    # avg_price=request.form.get('avg_price')
    # avg_guest=request.form.get('avg_guest')

    # # venue_list=common.sql_write(f"INSERT INTO {category}(name, img_pic,location,overview,avg_price,avg_ppl) VALUES (%s,%s,%s,%s,%s,%s)", [venue_name, venue_img,location,overview,int(avg_price),int(avg_guest) ])
    # venue_list=short.add_venue_list([venue_name, venue_img,location,overview,int(avg_price),int(avg_guest) ])
    return redirect("/home")


@app.route('/check/venue/category')
def check_venue_category():
    return render_template('check_category.html')


@app.route('/forms/edit/venue_list',methods=["POST"])
def edit_venue_list_form():
    table_name=request.form.get('category_name')
    id_input=request.form.get('id')
    is_valid=common.sql_read(f"SELECT * FROM {table_name}")
    if int(id_input) <= int(len(is_valid)):
        item=common.sql_read(f"SELECT * FROM {table_name} WHERE id={id_input}")
        return render_template("edit_venue_list.html",table_name=table_name,item=item,id=id_input)
    else:
        return """<h2>The id is not valid</h2><br>
                <a href="/check/venue/category">back to select category/id</a> """




@app.route('/api/edit/venue_list',methods=["POST"])
def api_venue_list():
    table_name=request.form.get('postName')
    id=request.form.get('postId')
    form=request.form
    edit_venue=add_edit_venue.Venue_adj(table_name,id)
    edit_venue.update_venue_list(form.get('venue_name'),form.get('venue_img'),form.get('location'),form.get('overview'),form.get('avg_price'),form.get('avg_guest'),)
    return redirect('/home')

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
    return render_template('delete_choose.html')

@app.route('/delete/check',methods=["POST"])
def delete_check():
    category_name=request.form.get('category_name')
    id=request.form.get('id')
    item_name=common.sql_read(f'SELECT * FROM {category_name} WHERE id={id}')
    return render_template('delete_confirm.html',category_name=category_name,id=id,item=item_name)


@app.route('/api/delete/venue',methods=["POST"])
def delete_confirm():
    form=request.form
    delete_submit=add_edit_venue.Venue_adj(
            form.get('postName'),
            form.get("postId")[0],      
    )
    check=delete_submit.delete_venue()
######blow code without using class code#####
    # table_name=request.form.get('postName'),
    # id=request.form.get("postId"), 
    # results=common.simple(f"DELETE FROM {table_name[0]} WHERE id={id[0]} ")
    return redirect('/home')
    



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
        # return render_template('user_page.html',user=user_info)
    else:
        return f"Wrong email or password . You input email :{email}, password:{plain_text_password}"



@app.route('/my_page',methods=["post","Get"])
def goto_user_page():
    
    # who_is_user=common.sql_read(f'SELECT * FROM users WHERE id={session["user_id"]}')
    # if who_is_user==False:
    #     return "We don't know you"
    # else:
        who_is_user=common.sql_read(f'SELECT * FROM users WHERE id={session["user_id"]}')
        print(who_is_user)
        like_btn=request.form.get('like_btn')
        print(like_btn)
        return render_template('user_page.html',user=who_is_user,like=like_btn)


@app.route('/user_logout')
def user_logout():
    session['user_id']=None
    return redirect ('/home')



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
    #return f"{isValidPassword}"
    common.sql_write("INSERT INTO users (email,name,weddingDate,guestNum,budget,password_hash)VALUES(%s,%s,%s,%s,%s,%s);",[email,name,date,guests,budget,hashed_password])
    results=common.sql_read("SELECT * FROM users WHERE email=%s;",[email])
    
    return  f"""
    <p> Hi {results[0][2]}. Your email :{results[0][1]} Your password:{results[0][6]}</p><br>
    <p>enjoy food truck<a href="/home">menu</a></p>
     <p>Is this valid password? {isValidPassword}</p> """

if __name__ =="__main__":
    app.run(debug=True)