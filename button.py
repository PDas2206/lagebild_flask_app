# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:52:21 2022

@author: PRIYANKA
"""

from flask import Flask, jsonify, render_template, request
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/FunctionJob1Start')
def FunctionJob1Start():
    
    print('In SomeFunction')
    with open("data_file.txt", "w", encoding="utf-8") as f_in:
        now = datetime.now()
        print("Job 1 starts at:", now, file=f_in)
            
        
    return "Nothing"

@app.route('/FunctionJob1End')
def FunctionJob1End():
    with open("data_file.txt", "a", encoding="utf-8") as f_in:
        now = datetime.now()
        print("Job 1 ends at:", now, file=f_in)
    

@app.route('/FunctionRobot')
def FunctionRobot():
    print("You are using a Robot")
    return "Nothing"



if __name__ == '__main__':
   app.run(debug=True)