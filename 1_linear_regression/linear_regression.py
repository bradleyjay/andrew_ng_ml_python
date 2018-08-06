'''

Linear Regression, Andrew Ng - Python, Numpy Implimentation

'''

import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline # juypter notebook syntax

# read in dataset

np.seterr(divide='ignore', invalid='ignore')
data = np.genfromtxt('./ex1data1.txt', delimiter=',')

x = data[:,0]
y = data[:,1]
m = len(y)

# plot raw data

fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(x,y, marker = 'x', c='r')
ax.set_title('Food Truck - Estimated Revenue per City')
ax.set_xlabel('Population of City (10,000s)')
ax.set_ylabel('Profit ($10,000s)')

#plt.show() # wouldn't need in Juypter Notebook

# prepare matricies for parameters (theta) and X (features)

X = np.matrix([])
col1 = np.ones((m,1))

X[:,0] = x