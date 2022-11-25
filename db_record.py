# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 16:21:03 2022

@author: PRIYANKA
"""

import sqlite3


connection = sqlite3.connect("db_record.db")
cursor = connection.cursor()

cursor.execute("create table record (job TEXT, timestamp INTEGER)")
#cursor.execute("INSERT INTO record VALUES (?,?)", ("Job1Start", 123))
"""
for i in range(len(record)):
	cursor.execute("insert into record (job) values (?)",[record[i]])
	print("added ", record[i])
"""
cursor.execute("SELECT * FROM record")
print(cursor.fetchall())
connection.commit()
connection.close()
