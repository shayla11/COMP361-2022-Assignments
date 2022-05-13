#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 22:07:06 2022

@author: shayla
"""

import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()


homework_sql_query = """ SELECT DISTINCT * FROM horse_table 
                    WHERE age > ? and age < ? """

cursor.execute(homework_sql_query, (7, 13))
results = cursor.fetchall()
for result in results:
    print(result[0])
    
connection.commit()
connection.close()