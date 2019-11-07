#This is the Sine-Cpsine graph viewer which allows the user to view two graphs, one each for sine and cosine where there 
#is a 180-degree difference between any two points 

import matplotlib.pyplot as plt
import numpy as np

Fs = 8000
f = 5
sample = 8000
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)
plt.plot(x, y)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()
