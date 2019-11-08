#This is the Sine-Cosine graph viewer which allows the user to view two graphs, one each for sine and cosine where there 
#is a 180-degree difference between any two points 

import matplotlib.pyplot as plt
import numpy as np

Fs = 8000
f = 5

sample = 8000
x = np.arange(0, sample, 1)

y = np.sin(2 * np.pi * f * x / Fs)
y1 = np.cos(2 * np.pi * f * x / Fs)

plt.plot(x, y, x, y1)
plt.xlabel('x')
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin(x) and cos(x) from 0 and 2pi')
plt.legend(['sin(x)', 'cos(x)'])
plt.show()




