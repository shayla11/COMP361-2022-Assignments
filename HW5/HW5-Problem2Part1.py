#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 15:48:04 2022

@author: shayla
"""

import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

horse_table = """ CREATE TABLE IF NOT EXISTS horse_table 
                (horse text, age int);"""

with open("data.txt") as file:
    file_lines = []
    for file_line in file:
        file_lines.append(tuple(file_line.strip().split()))
        
cursor.execute(horse_table)
connection.commit()

add_to_horse_table = """ INSERT INTO horse_table (horse, age) 
                    VALUES ("{horse_name}", "{horse_age}");"""
                    
for l in file_lines:
    sql_command = add_to_horse_table.format(horse_name=l[0], horse_age=l[1])
    cursor.execute(sql_command)
    
connection.commit()
connection.close()