# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:52:21 2022

@author: PRIYANKA
"""

from flask import Flask, render_template, request
#from datetime import datetime


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
"""
@app.route('/FunctionJob1Start')
def FunctionJob1Start():
    
    #print('In SomeFunction')
    #with open("data_file.txt", "w", encoding="utf-8") as f_in:
        #now = datetime.now()
        #print("Job 1 starts at:", now, file=f_in)
            
        
    return "Nothing"

@app.route('/FunctionJob1End')
def FunctionJob1End():
    #with open("data_file.txt", "a", encoding="utf-8") as f_in:
        #now = datetime.now()
        #print("Job 1 ends at:", now, file=f_in)
    return "Nothing"
    

@app.route('/FunctionRobot')
def FunctionRobot():
    #print("You are using a Robot")
    return "Nothing"
    
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
    



if __name__ == '__main__':
   app.run(debug=True)
