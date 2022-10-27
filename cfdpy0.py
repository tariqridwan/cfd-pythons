# <-- comments in python are denoted by the pound sign, like this one

import numpy                 # we import the array library
from matplotlib import pyplot    # import plotting library
myarray = numpy.linspace(0, 5, 10)
myarray
a = 5        #a is an integer 5
b = 'five'   #b is a string of the word 'five'
c = 5.0      #c is a floating point 5  
type(a)
type(b)
type(c)
for i in range(5):
    print("Hi \n")
    for i in range(3):
    for j in range(3):
        print(i, j)
    
    print("This statement is within the i-loop, but not the j-loop")
    myvals = numpy.array([1, 2, 3, 4, 5])
myvals
myvals[0], myvals[4]
myvals[5]
