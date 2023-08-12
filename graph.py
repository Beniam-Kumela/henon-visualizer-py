#Import modules
import matplotlib.pyplot as plt
import numpy as np

x_val = []
a_val = []
n_iter = 100
x = 0.1
y = 0.1
a = 0.75
b = 0.3

fig, ax = plt.subplots()

while a <= 2:
    
    for i in range(n_iter):
        x = 1 - a * x ** 2 + y
        y = b * x
        
    for i in range(n_iter):
        x = 1 - a * x ** 2 + y
        y = b * x
        
        x_val.append(x)
        a_val.append(a)
        
    a += 0.001

z = np.arange(len(a_val))
cmap = plt.get_cmap('coolwarm')

ax.scatter(a_val, x_val, s = 0.1, c=z, cmap=cmap)
ax.set_xlabel('a')
ax.set_ylabel('x')
ax.set_title('Henon Bifurcation for a values (1-2) and b = 0.3 for 100 iterations')
plt.show()