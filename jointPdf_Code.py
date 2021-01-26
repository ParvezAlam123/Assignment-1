from mpl_toolkits import mplot3d 
import numpy as np 
import matplotlib.pyplot as plt 
  
fig = plt.figure() 
  
# syntax for 3-D projection 
ax = plt.axes(projection ='3d') 
  
# defining all 3 axes 
v = np.linspace(0, 1, 100) 
theta = np.linspace(0,2*np.pi,100)
z = v**2+v*theta
  
# plotting 
ax.plot3D(v, theta, z, 'green') 
ax.set_title('3D line plot geeks for geeks') 
plt.show() 