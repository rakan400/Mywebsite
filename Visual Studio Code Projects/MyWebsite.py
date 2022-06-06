from flask import Flask, render_template, url_for, flash, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from numpy import RankWarning
import pymongo
from pymongo import MongoClient
from datetime import date
import time
from flask_login import LoginManager, login_user

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://rakan00:12345@mywebsitedb.\
eg9nka5.mongodb.net/?retryWrites=true&w=majority")
db = client.MyWebsiteDB

app.config['SECRET_KEY'] = "qa12qa"

login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/")
@app.route("/home")
def home(methods=["GET", "POST"]):
    collection = db.UserAccounts
    username = ''
    balance = ''

    return render_template('Home Page.html', username = username, balance = balance)

#@app.route("/about")
#def about():
#   return render_template('about.html', title = 'about')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    collection = db.UserAccounts
    errorlabel = ''

    if request.method.upper() == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        cpassword = request.form.get("cpassword")

        if username.strip() == "" or email.strip()=="" or password.strip()=="" or cpassword.strip()=="":
            errorlabel = "Missing Information!"
            return render_template('Sign up page.html', errorlabel = errorlabel)

        elif password != cpassword:
            errorlabel = "Passwords don't match!"
            return render_template('Sign up page.html', errorlabel = errorlabel)

        else:
            data = {'username':username,
                'email':email,
                'password': password,
                'balance':0
                }
            try:
                collection.insert_one(data)
            except Exception as e:
                errorlabel = e.args
            else:
                return redirect(url_for("home"))

    return render_template('Sign up page.html', errorlabel = errorlabel)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    collection = db.UserAccounts
    errorlabel = ''

    if request.method.upper() == "POST":
        email = request.form.get("email")
        password = request.form.get("password").split()

        email_found = collection.find_one({"email": email})
        if email_found:
            passwordcheck = (email_found['password']).split()
            
            if password == passwordcheck: 
                login_user(email)
                return redirect(url_for("home"))
            else:
                errorlabel = "Wrong password!"
                return render_template('login page.html', errorlabel = errorlabel)
        else:
            errorlabel = 'Email not found'
            return render_template('login page.html', errorlabel = errorlabel)

    return render_template('login page.html', errorlabel = errorlabel)

@app.route('/contact_us', methods=["GET", "POST"]) 
def contact_us():
    return render_template('Contact us.html')

@app.route('/News', methods=["GET", "POST"]) 
def News():
    return render_template('News.html')

@app.route('/shotlinks', methods=["GET", "POST"]) 
def Shortlinks():
    return render_template('Shortlinks.html')

@app.route('/Ads', methods=["GET", "POST"]) 
def Ads():
    return render_template('Watch Ads.html')

@app.route('/Withdraw', methods=["GET", "POST"]) 
def Withdraw():
    return render_template('Withdraw.html')


#@app.route('/create', methods=["GET", "POST"]) 
#def create_post():
#    if request.method.upper() == "POST":
#        medicine = request.form.get("medicine")
        
#        if medicine == None or medicine.strip() == "":
#            flash("Please fill all the fields")
#            return render_template("create_post.html")

#        db = client.firstdb
#        collection = db.Med_posts

#        today = date.today()
#        todays = str(today)

#        data = {'title': medicine,
#                'date': todays}

#        collection.insert_one(data)

#        return redirect(url_for("home")) # redirect user
#    return render_template("create_post.html")

if __name__ == '__main__':
    app.run(debug=True)