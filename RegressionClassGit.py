'''
Created on Sep 1, 2017

@author: bob
'''
import numpy as np
from pylab import meshgrid
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random      
N=5 # number of different points for regression; I am only allowing values of -1 and 1
Xarray=10*rng.randn(N)
print("Xvalues ",Xarray,"\nshape of Xarray ",Xarray.shape)
Vlow=-10;Vhigh=10 #originally 0 and 2 to mimic perceptron 
V= rng.randint(size=N, low=Vlow, high=Vhigh)

V=2*V-1  #note that the constant 2 is broadcast through the array as it should in linear algebra
print("values taken on by V",V, "\nshape of V \n",V.shape)

if N==2 and Xarray[1]!= Xarray[0] :
    wans= (V[1]-V[0])/(Xarray[1]-Xarray[0])
    bans= V[0]-wans*Xarray[0]
slope, intercept, r_value, p_value, std_err = stats.linregress(Xarray,V)    
    
def cost(w,b):
    costArray=((w*Xarray+b)-V)**2 # taking square here to eventually take sum of squares
    return costArray.sum()
#print ("cost = \n",cost(1,1))

def costWrapper(Avar):# just a wrapper function for sciPy
    return cost(Avar[0],Avar[1]) # I think I can give it an ordered pair


#
#vcostWrapper= np.vectorize(costWrapper)  #did not work wanted to be able to work on array of pairs
    
#
#print("usingwrapper ", costWrapper([1,1]))
#find the minimum from sciPy ; sort of ridiculous for square as is normal regression you can solve analytically
res = minimize(costWrapper,[.5,.5],method='Nelder-Mead')# this method doesnt use derivatives
print("result is ",res)
print(" the  results from our minimizer of values of w, b  are ",res.x[0],res.x[1])
print("the minimum it reached is ",res.fun)
if N== 2 and Xarray[1]!= Xarray[0] :
    print("the actual answer which should give us 0 as a cost is \n ",wans,bans)
print("\n the answer from regression slope, intercept,error is \n",slope,intercept,cost(slope,intercept))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# !!!!!!!!!!!!!!!!! should change -.8 to 1 to really see more correct graph !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
w= np.arange(res.x[0]-2,res.x[0]+2,.05)  #change from 1 to -.8 to see arrays
b= np.arange(res.x[1]-2,res.x[1]+2,.05) 
W,B= meshgrid(w,b) #grid of points
print("\n W array\n",W,"\n and shape of W \n",W.shape)
print("\nB array\n",B,"\n and shape of B \n",B.shape)
#===============================================================================
# Ztemp= list(zip(np.ravel(W),np.ravel(B)))
# Ztemp= np.array(Ztemp)
# print ("just zipped arrays as list of pairs \n",Ztemp, "\n and length of list \n",len(Ztemp))
# ZtempA= vcostWrapper(Ztemp,1)
# 
# 
# ZtempA= ZtempA.reshape(W.shape)
# print("\n reshaped array of z values \n",ZtempA)
#===============================================================================

zs=np.array([cost(w,b)for w,b in zip(np.ravel(W),np.ravel(B))]) #note is iterator
Z = zs.reshape(W.shape)
print(" \n  the Z after applying function \n",Z,"\n and shape of Z \n",Z.shape)   

ax.plot_surface(W, B, Z)
    
ax.set_xlabel('W Label')
ax.set_ylabel('B Label')
ax.set_zlabel('Z Label')
    
plt.show()


    