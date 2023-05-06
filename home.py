from flask import Flask,render_template,request,session,redirect
import requests
import psycopg2
from models import short,common

import os


SECRET_KEY = os.getenv('SECRET_KEY')

app=Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY



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
    # each_venue_list=short.each_list("SELECT * FROM winery_list_table")
    each_venue_list=short.each_list("winery_list_table")
    category_name='Winery'
    winery_list=[]
    for each in each_venue_list:
        winery_list.append(each)
    return render_template("venue_list.html",list=winery_list,category_name=category_name)


@app.route('/City')
def city_page():
    # each_venue_list=short.each_list("SELECT * FROM city_venue_list_table")
    each_venue_list=short.each_list("city_venue_list_table")
    category_name='City'
    city_list=[]
    for each in each_venue_list:
        city_list.append(each)
    return render_template("venue_list.html",list=city_list,category_name=category_name)


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
def autho_logout():
    session['user_id you']=None
    return redirect ('/home')


@app.route('/add_venue_list')
def add_form():
    return render_template('add_venue_list.html')
app.run(debug=True)