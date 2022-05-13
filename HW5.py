#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:29:22 2022

@author: shayla
"""

import unittest
from HW4 import ForSaleBook, ExaminationCopy, Box

box = None

class TestForSaleBook(unittest.TestCase):
    def test_init_ForSaleBook(self):
        testBook = ForSaleBook("MobyDick", 3.5, 12.50)
        self.assertEqual(testBook.title, "MobyDick" )
        self.assertEqual(testBook.weight, 3.5)
        self.assertEqual(testBook.price, 12.50)
        
    def test_str_ForSaleBook(self):
        testBook = ForSaleBook("MobyDick", 3.5, 12.50)
        self.assertEqual(testBook.__str__(), 'MobyDick ($12.50)')
        
class TestExaminationCopy(unittest.TestCase):
    def test_init_ExaminationCopy(self):
        testBook = ExaminationCopy("Little Women", 2.7, "Fred")
        self.assertEqual(testBook.title, "Little Women")
        self.assertEqual(testBook.weight, 2.7)
        self.assertEqual(testBook.receiver, "Fred")
        
    def test_str_ExaminationCopy(self):
        testBook = ExaminationCopy("Little Women", 2.7, "Fred")
        self.assertEqual(testBook.__str__(), "Little Women (Fred)")
        
        
class TestBox(unittest.TestCase):
    def setUp(self):
        self.bx = Box(12, 7)
        self. bx.add_book(ForSaleBook('Catch 22', 3.2, 10.75))
        self.bx.add_book(ForSaleBook('Catch 21', 3.5, 15.99))
        
    def tearDown(self):
        self.bx = None
    
    def test_total_weight(self):
        self.assertEqual(self.bx.total_weight(), 6.7)
    
    @unittest.expectedFailure
    def test_add_book(self):
        self.box.add_book(ForSaleBook("The Hunger Games", 12.3, 16.99))
        raise ValueError
        
        

if __name__ == "__main__":
    unittest.main()
        