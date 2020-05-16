# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:46:48 2020

@author: Surya
"""
'''
1.1 Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()
'''

def myreduce(anyfunc, my_list):
    # Get first item in sequence and assign to result
    result = my_list[0]
    # iterate over remaining items in sequence and apply reduction function 
    for item in my_list[1:]:
        result = anyfunc(result, item)
    return result
 

#Function to test custom myreduce()
def sum(x,y):
    return x+y

ls=[1,2,3,4,5]

myreduce(sum,ls)
       
'''
1.2 Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()
'''

def myfilter(anyfunc, my_list):
    # Creating an empty list to append the result
    result = []
    # iterate over sequence of items in sequence and apply filter function
    for item in my_list:
        if anyfunc(item):
            result.append(item)
    # return funal output
    return result

#Function to test custom myfilter()
def even(x):
    if x%2==0:
        return True
    else:
        return False
    
myfilter(even,ls)


'''
2. Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
[4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
'''

name='ACADGILD'
result=[i for i in name]
print(result)

inputls=['x','y','z']
result=[letter*i for letter in inputls for i in range(1,5)]
print(result)

inputls=['x','y','z']
result=[letter*i for i in range(1,5) for letter in inputls]
print(result)

inputls=[2,3,4]
result=[[x+i] for x in inputls for i in range(0,3)]
print(result)

inputls=[2,3,4,5]
result=[[x+i for x in inputls] for i in range(0,4)]
print(result)

inputls=[1,2,3]
result=[(i,x) for x in inputls for i in inputls ]
print(result)
