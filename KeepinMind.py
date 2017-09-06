'''
Created on Sep 6, 2017

@author: bob
'''
import numpy as np

# difference between a list and a 1d array and a range
#class 3 material
ri = range(12)
print ("trying to print a range object \n", ri)# it is an iterator
li= list(ri) # converting to list
print(" \n after converting to a list \n",li)
Ai= np.array(ri)
print("\n after converting to an array (from iterator ould use list too) \n",Ai)

print("\nwhat is difference between one dim array and a list")
print("An array has a shape and can use math on it ", )
print (" \nshape of array\n", Ai.shape)
print("\n add two arrays ",Ai+Ai)
print(" multiply ", Ai*Ai)
print(" cube ",Ai**3)
print("\n you can also reshape arrays \n")
print("\n as a 3X4 \n", Ai.reshape((3,4))) # too many parenthisis should do in steps
print("\n as a 2X3X2 \n", Ai.reshape((2,3,2)))
print("\n you cant do these with lists or they have different meaning\n")

print (" the sum of two lists" ,li+li)
#print(" the difference of two lists" ,li-li) #nope
#print("the shape of a list",li.shape) #nope etc