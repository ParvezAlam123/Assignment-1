import numpy as np
import matplotlib.pyplot as plt
R=1
theta=np.linspace(0,2*np.pi,100)
P=R**3/3+(R**2/2)*theta
plt.plot(theta,P)
plt.xlabel('Theta')
plt.ylabel('Pdf of theta')
plt.show()