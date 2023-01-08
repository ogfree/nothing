import matplotlib.pyplot as plt
import numpy as np
x1 = np.linspace(-5,5,100)

y = np.sin(x1)
y1= np.cos(x1)

plt.plot(x1,y,'-.g',label='sinx')
plt.plot(x1,y1,'-.r', label='cosx inverted to sinx')
# the function, which is y = sin(x) here

plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()