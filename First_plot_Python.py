# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 19:40:34 2020

@author: Alejandro Hurtado
"""
'''Make a program that prints a main plot with 3 functions.
And then one subplot for each fuction.'''
# Emmanuel Alejandro Hurtado Alejandre Data 2A 

# Importing numpay and change its indicator to np
import numpy as np 
# Importing matplotlib.pyplot and change its indicator to plt
import matplotlib.pyplot as plt 

x = np.arange(0,11) # Defining the domain showed in the plot and subplots
y1 = np.cos(x)-1    # Initializing fuction 1 
y2 = 2*np.sin(x/3.) # Initializing fuction 2 
y3 = (x**2)/20.-2   # Initializing fuction 3 

plt.plot(x, y1)             # Adding function 1 to plot
plt.plot(x, y2)             # Adding function 2 to plot
plt.plot(x, y3)             # Adding function 3 to plot
plt.xlabel("X axis")        # Defaining the name of x axis 
plt.ylabel("Y axis")        # Defaining the name of y axis 
plt.title("Original Graph") # Defaining the title of the plot  
plt.legend(["cos(x-1)", "2sin(x/3)", "(x^2)/20-2"]) # Defining legends
plt.show()                  # Showing plot on screen

plt.subplot(3,1,1)          # Creting subplot
plt.plot(x,y1)              # Adding function 1 to subplot
plt.xlabel("X axis")        # Defaining the name of x axis 
plt.ylabel("Y axis")        # Defaining the name of y axis 
plt.title("Function 1")     # Defaining the title of the subplot
plt.legend(["cos(x-1)"])    # Defining legends
plt.show()                  # Showing subplot on screen

plt.subplot(3,1,2)          # Creting subplot
plt.plot(x,y2)              # Adding function 2 to subplot
plt.xlabel("X axis")        # Defaining the name of x axis 
plt.ylabel("Y axis")        # Defaining the name of y axis 
plt.title("Function 2")     # Defaining the title of the subplot
plt.legend(["2sin(x/3)"])   # Defining legends
plt.show()                  # Showing subplot on screen

plt.subplot(3,1,3)          # Creting subplot
plt.plot(x,y3)              # Adding function 3 to subplot
plt.xlabel("X axis")        # Defaining the name of x axis 
plt.ylabel("Y axis")        # Defaining the name of y axis 
plt.title("Function 3")     # Defaining the title of the subplot
plt.legend(["(x^2)/20-2"])  # Defining legends
plt.show()                  # Showing subplot on screen

'''
References:
    https://cs231n.github.io/python-numpy-tutorial/
    https://www.machinelearningplus.com/python/101-numpy-exercises-python/
'''