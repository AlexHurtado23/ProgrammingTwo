# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 20:17:35 2020

@author: Alejandro Hurtado
"""
'''Make a program that preforms all the posible array operations
 with 2 given vectors by the user'''
# Emmanuel Alejandro Hurtado Alejandre Data 2A 

import numpy as np    # Importing numpay and change its indicator to np
import sys            # Importing system library 

size_x = int(input("Length of array x: ")) # Aksing for the length of array x
size_y = int(input("Lenght of array y: ")) # Aksing for the length of array y
print("\n")
x = np.zeros((1,size_x)) # Creating array x filling it with zeros
y = np.zeros((1,size_y)) # Creating array y filling it with zeros

if (size_x != size_y): # Condition to acomplish to preform operations
    print("Sorry we cannot preform the operations. Watch your sizes!")
    sys.exit()
else:
    # Asking for the value of each element of array x 
    print("Give values for array x: ") 
    for i in range(0,size_x):
        x[0,i]= input("Element [0,"+str(i+1)+"]: ")
    print("\n")

    # Asking for the value of each element of array y 
    print("Give values for array y: ")
    for i in range(0,size_y):
        y[0,i]= input("Element [0,"+str(i+1)+"]: ")
    print("\n")
    
    # Showing the given arrays    
    print("Given arrays")
    print("array x: ",x)
    print("array y: ",y)
    print("\n")

    # Making addition of both arrays
    print("Addition of the given arrays is: ",np.add(x,y))
    
    # Making substraction of both arrays
    print("Subtraction of the given arrays is: ",np.subtract(x,y))
    
    # Making multiplication of both arrays
    print("Multiplication of the given arrays is: ",np.multiply(x,y))
    
    # Making division of both arrays
    print("Division of the given arrays is: ",np.divide(x,y))
    
    # Making the square root of array x
    print("Square root of the given array x is: ",np.sqrt(x))
    
    # Making the square root of array y
    print("Square root of the given array y is:",np.sqrt(y))

'''
References:
    https://cs231n.github.io/python-numpy-tutorial/
    https://www.machinelearningplus.com/python/101-numpy-exercises-python/
'''