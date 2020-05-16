# -*- coding: utf-8 -*-
"""
Created on Sat May 16 13:13:36 2020

@author: Surya
"""
'''
1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.
'''
class TraingelData:
    def __init__(self):
        self.a = float(input("Enter value of 'a' :" ))
        self.b = float(input("Enter value of 'b' :" ))
        self.c = float(input("Enter value of 'c' :" ))

class AreaOfTriangel:
    def area(tri):
        s=(tri.a+tri.b+tri.c)/2
        res=(s*(s-tri.a)*(s-tri.b)*(s-tri.c))** 0.5
        print('The area of triangle is:',res)
        
t=TraingelData()
AreaOfTriangel.area(t)

'''
1.2 Write a function filter_long_words() that takes a list of words and an integer n and 
returns the list of words that are longer than n.
'''

def filter_long_words(string,number):
    return [word for word in string if len(word) > number]
    
#wordlist=[]
#n=int(input('enter the no of words like to enter:'))
#for i in range(n):
#    word=input('Enter the word you like :')
#    wordlist.append(word)

wordlist=['surya','kumar','sadhana']
filter_long_words(wordlist,5)

'''
2.1 Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list
'''
wordlist=['surya','kumar','sadhana']

def Length(inputlist):
    output=[]
    for i in inputlist:
        x=len(i)
        output.append(x)
    print(output)

Length(wordlist)
    
'''
2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise.
'''
def VowelorNot():
    x=input('please enter a character: ')
    y=['a','e','i','o','u']
    if x in y:
        print('True')
    else:
        print('False')

VowelorNot()    
