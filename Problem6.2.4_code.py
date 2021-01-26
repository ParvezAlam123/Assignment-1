import numpy as np
import matplotlib.pyplot as plt
v=np.linspace(0,1,100)
P=2*np.pi*v*(v+np.pi)
plt.plot(v,P)
plt.xlabel('v')
plt.ylabel('Pdf of v')
plt.show()