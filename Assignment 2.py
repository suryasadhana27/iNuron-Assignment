# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:27:08 2020

@author: Surya
"""
'''
1 . Create the below pattern using nested for loop in Python.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''

num=5
for i in range(1,num+1):
    for j in range(1,i+1):
        print('*',end='')
    print()
for a in range(1,num+1):
    for b in range(1,num+1-a):
        print('*', end='')
    print()


'''
2. Write a Python program to reverse a word after accepting 
the input from the user.
'''
data=input('Please enter a word : ')
print(data[::-1])