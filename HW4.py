#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 21:08:23 2022

@author: shayla
"""

class Book:
    def __init__(self, title, weight):
        self.title = title
        self.weight = weight
    def __str__(self):
        return self.title

class ForSaleBook(Book):
    def __init__(self, title, weight, price):
        self.title = title
        self.weight = weight
        self.price = price
    def __str__(self):
        return self.title + " ($" + "{:.2f}".format(self.price) + ")"
    
class ExaminationCopy(Book):
    def __init__(self, title, weight, receiver):
        self.title = title
        self.weight = weight
        self.receiver = receiver
    def __str__(self):
        return self.title + " (" + self.receiver + ")"
    
class Box():
    def __init__(self, id, capacity):
        self.content = []
        self.id = id
        self.capacity = capacity
    def add_book(self,bk):
        try:
            if bk.weight > self.capacity:
                raise ValueError("Capacity of box " + str(self.id) + " exceeded.")
            self.content.append(bk)
            self.capacity -= bk.weight
            
        except ValueError as e:
            print(e)
        
    def total_weight(self):
        total = 0
        for b in self.content:
            total += b.weight
        return total
    
    def print_content(self):
        for b in self.content:
            print(b)

    
    
    
if __name__ == '__main__':
    fs_bk = ForSaleBook('MobyDick', 3.5, 12.50)
    print(str(fs_bk) + ' has weight ' + str(fs_bk.weight) + ' pounds.') 
    ex_cp = ExaminationCopy('Little Women', 2.7, 'Fred') 
    print(str(ex_cp) + ' has weight ' + str(ex_cp.weight) + ' pounds.') 
    print('-' * 40)
    bx = Box(12, 10.0)
    bx.add_book(fs_bk)
    bx.add_book(ex_cp)
    bx.add_book(ForSaleBook('Catch 22', 3.2, 10.75))
    bx.print_content()
    try:
        bx.add_book(ExaminationCopy('Networks: An Introduction', 3.7, 'Al')) 
    except ValueError as detail:
        print(detail)