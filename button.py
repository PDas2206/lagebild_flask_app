# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:52:21 2022

@author: PRIYANKA
"""
import sqlite3
from flask import Flask, jsonify, render_template, request, session, g, flash
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = "AAAAfghjkti22222888888"
app.config["SESSION_COOKIE_NAME"] = "myCOOKIE_monSTERRRRRRRRRR"

connection = sqlite3.connect("db_record.db")
cursor = connection.cursor()

result=""

@app.route('/thank')
def thank():
    connection = sqlite3.connect("db_record.db")
    cursor = connection.cursor()
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    cursor.execute("INSERT INTO record VALUES (?,?)", ("ALLENDTHANK", now))
   
    connection.commit()
    return render_template("thank.html")



@app.route('/')
def home():
    #flash("Enter your name/alias")
    return render_template("home.html")


"""
@app.route("/", methods=["POST", "GET"])
def login():
    
    

    return render_template("login.html")
"""


"""    
@app.route('/sample', methods=["POST", "GET"])
def sample():
    
   return render_template("sample.html")
"""


@app.route('/index', methods=["POST", "GET"])
def index():
   connection = sqlite3.connect("db_record.db")
   cursor = connection.cursor()
   now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
   cursor.execute("INSERT INTO record VALUES (?,?)", ("STARTEXPERIMENT", now))
   
   connection.commit()
    
   return render_template("index.html")


 
''' function to store the user name '''


"""
@app.route('/storeName', methods=['GET','POST'])
def storeName():
    form=formABC()
    if form.is_submitted():
        result=request.form["text_box"]
        app.logger.info(result)
   
    #userName = request.values.get("text_box")
    return render_template("home.html")
"""
    
    

@app.route('/FunctionJob1Start')
def FunctionJob1Start():
    """old
    print('In SomeFunction')
    with open("data_file.txt", "w", encoding="utf-8") as f_in:
        now = datetime.now()
        print("Job 1 starts at:", now, file=f_in)
            
        
    #return "Nothing"
    """
    
    
    
    connection = sqlite3.connect("db_record.db")
    cursor = connection.cursor()
    
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    #session["all_items"].append("Job1Start",now)
    
    
    
    cursor.execute("INSERT INTO record VALUES (?,?)", ("Job1Start", now))
    
    
    print(cursor.fetchall())
    connection.commit()
    #connection.close()
    #session.modified = True
    
    return render_template("index.html")

@app.route('/FunctionJob1End')
def FunctionJob1End():
    """old
    with open("data_file.txt", "a", encoding="utf-8") as f_in:
        now = datetime.now()
        print("Job 1 ends at:", now, file=f_in)
    """
    connection = sqlite3.connect("db_record.db")
    cursor = connection.cursor()
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    cursor.execute("INSERT INTO record VALUES (?,?)", ("Job1End", now))
    #print(cursor.fetchall())
    connection.commit()
    
    return render_template("index.html")
    

@app.route('/FunctionJob2Start')
def FunctionJob2Start():
   
    
    connection = sqlite3.connect("db_record.db")
    cursor = connection.cursor()
    
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    cursor.execute("INSERT INTO record VALUES (?,?)", ("Job2Start", now))
    
    connection.commit()
    
    
    return render_template("index.html")

@app.route('/FunctionJob2End')
def FunctionJob2End():
    
    connection = sqlite3.connect("db_record.db")
    cursor = connection.cursor()
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    cursor.execute("INSERT INTO record VALUES (?,?)", ("Job2End", now))
   
    connection.commit()
    
    return render_template("index.html")
    

@app.route('/FunctionRobot')
def FunctionRobot():
    print("You are using a Robot")
    return render_template("index.html")




@app.route('/FinishExperiment')
def FinishExperiment():
    
    connection = sqlite3.connect("db_record.db")
    cursor = connection.cursor()
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    cursor.execute("INSERT INTO record VALUES (?,?)", ("ALLEND", now))
   
    connection.commit()
    
    return render_template("thank.html")
    

"""
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('db_record.db')
        cursor = db.cursor()
        #cursor.execute("select name from groceries")
        #all_data = cursor.fetchall()
        #all_data = [str(val[0]) for val in all_data]

        #shopping_list = all_data.copy()
        #random.shuffle(shopping_list)
        #shopping_list = shopping_list[:5]
    #return all_data
    return cursor
"""

if __name__ == '__main__':
   app.run(debug=True)