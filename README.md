# Melbourne wedding venue web 

This is the link for [RENDER](https://project2-fnip.onrender.com/home) 

The app in this repo is deployed at [https://flask.onrender.com](https://flask.onrender.com).

## For project2
_______
I created wedding venue website. The web has some category, each category has some different venue list and like button to save the "favorite list" into user page.

## What user can do
________

* sign up as an user and save some list into "my_page"
* once click "like" button from each venue list 

## What admin can do.
____
* Able to adjust category list (ADD,Edit,Delete)

## My steps
__________
1. create category database table.
2. create each category's database table (5 categories for now) 
3. Admin login page/check Name & password to match
4. Admin member be able to adjust category list(Add venue,edit venue data and delete venue list) 
5. Create User login/check if the password is vialed and match with user database.
6. If user existing member, able to save the venue list.
7. Create sign up page 

## Struggle point
_____

* I struggled to trigger "like button" list create User like list table to get data and push into "my_page" to show.
  
## NEED to fix and 
_____
This is "user MY_page"
Need to create each value has each delete button with like_table id to trigger delete button for DELETE specific data from table.
However, i couldn't fix "button"'s for loop that looping same as first loop amount of value. instead each button for each list... each list has multiple delete buttons.

```````js

    <div class="liked_container">
 
      {% for  u in liked_venues %}
      
      <div class="liked_block">
        <div class="venue_name" name="">{{u[0][1]}}</div>
        <div class="card_image">
            <img src='{{u[0][2]}}' class="img">
        </div>
        
        <form  action="/delete_liked" method="POST"  >
          {% for  liked in user_like_list %}
        
            
            <button  name="delete_liked_btn" value="{{liked[0]}}">DELETE</button>
      
            {% endfor%}     
        </form> 
      </div> 
      {% endfor%} 
    </div>  

`````````
## ADD more structure
_____
* more nice style css
* user page showing match budget list and guest number list.
* Venue list has "previous" and "Next" button, need to add more photos for each venue.
  