# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 07:05:51 2020

@author: Surya
"""
'''
1. Write a program which will find all such numbers which are divisible 
by 7 but are not a multiple of 5, between 2000 and 3200 (both included). 
The numbers obtained should be printed in acomma-separated sequence 
on a single line.
'''
output=[]
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        output.append(i)
print(output)

'''
2.Write a Python program to accept the user's first and last name and then 
getting them printed in the the reverse order with a space between first name 
and last name.
'''
fname=input('Enter yout First name: ')
lname=input('Enter your Last name: ')
print('{} {}'.format(lname,fname))
fullNmae= '{} {}' .format(fname,lname)
fullNmae[::-1]

'''
3.Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r**3
'''
def sphere():
    pi= 3.14156
    r=float(input('enter the diameter of the sphere: '))
    v=4/3 *pi*(r/2)**3
    print('The volume of the sphere is: ', v)

'''    
4. write a program which accepts a sequence of comma separated numbers 
from console and generate list
'''
emp_list=[]
n=int(input('Enter the length of the sequence you like to enter : '))
for i in range (n):
    value=input('Enter a number: ')
    emp_list.append(value)
emp_list
    
'''
5 . Create the below pattern using nested for loop in Python.

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
6. Write a Python program to reverse a word after accepting 
the input from the user.
'''
data=input('Please enter a word : ')
print(data[::-1])

'''
7. Write a Python Program to print the given string in the format specified in the sample output.
WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, ! SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
its citizens

Sample Output:
WE, THE PEOPLE OF INDIA,
having solemnly resolved to constitute India into a SOVEREIGN, !
SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
and to secure to all its citizens

'''
sentence='''
WE, THE PEOPLE OF INDIA,
having solemnly resolved to constitute India into a SOVEREIGN, !
SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
and to secure to all its citizens
'''
sentence.splitlines()


