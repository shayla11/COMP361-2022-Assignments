#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 11:02:42 2022

@author: shayla
"""

"""
1 (2.5 pts.) Write Python code that prompts for a word until the user enters an empty word (i.e.,
gives a carriage return immediately at the prompt). Then the code outputs a string containing all
the words entered, in the order in which they were entered, separated by spaces. (It will make
things easy if you have a space before the first word as well.) The following is an example
execution.

"""


word = "."
word_list = []
while word != "":
    word = input("Enter a word: ")
    word_list.append(word)
      
word_list = word_list[:-1]
for i in word_list:
    print(i, end =" ")

      
      
"""
2 (4.5 pts.) Write Python code that prompts for and inputs (and evaluates) a list of at least five
numbers. (You needn’t verify that what is entered is indeed a list of at least five numbers; just
assume it is.) It then prints out the first half and then the second half of the list. (If the list has odd
length, make the second half have one more number than the first.). Next, if the first element is
bigger than the last, swap them. Otherwise, if the first is smaller than the last, increment both by
1. Otherwise (the first element is neither bigger nor smaller than the last, i.e., they’re equal), set
both to 0. Finally, output the altered list. The following is an example execution where the first
element is bigger than the last and the length of the list is odd.
"""


num_list = eval(input("Enter a list of numbers with atleast 5 numbers: "))
first_half = len(num_list)//2

print("The first half is", end=" ")
print(num_list[:first_half])

print("The second half is", end=" ")
print(num_list[first_half:])

if num_list[0] == num_list[len(num_list)-1]: # x = y
    num_list[0] = 0
    num_list[len(num_list)-1] = 0
elif num_list[0] > num_list[len(num_list)-1]: # x > y
    x = num_list[0]
    y = num_list[len(num_list)-1]
    num_list[0] = y
    num_list[len(num_list)-1] = x
elif num_list[0] < num_list[len(num_list)-1]: # x < y
    num_list[0] = num_list[0]+1
    num_list[len(num_list)-1] = num_list[len(num_list)-1]+1
 
print("The updated list is", end=" ")
print(num_list)


    
'''
3 (3 pts.) Produce Python code that prompts for and inputs two lists of numbers. (You needn’t
verify that they are indeed lists of numbers.) It prints out a list where the element at any index i is
the sum of the elements at index i of the two input lists. If the input lists are of different lengths,
have the length of the output list be the length of the shorter of the two. Use a for loop. Note that,
where x and y are numbers, min(x,y) is the smaller of those two numbers. For example, if the
two input lists are [2, 4, 3] and [1, 7, 2, 5], then the resulting list will be [3, 11, 5]. 
'''

first_num_list = eval(input("Enter a list of numbers: "))
second_num_list = eval(input("Enter another list of numbers: "))

min_val = min(len(first_num_list), len(second_num_list))
if len(first_num_list) == min_val:
    shorter_list = first_num_list
else:
    shorter_list = second_num_list
   
updated_list = []
for x in range(len(shorter_list)):
    num = first_num_list[x] + second_num_list[x]
    updated_list.append(num)
 
print("The updated list is", end=" ")
print(updated_list)




