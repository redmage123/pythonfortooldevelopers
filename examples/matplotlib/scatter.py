#!/usr/bin/python3

import matplotlib.pyplot as plt


x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label = 'Scatter plot example',color = 'red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Age distribution histogram')
plt.legend()
plt.show()

plt.xlabel('x')
plt.ylabel('y')
plt.title('Age distribution histogram')
plt.scatter(x,y,label = 'Scatter plot example 2', color = 'black',marker = '*')
plt.show()

plt.xlabel('x')
plt.ylabel('y')
plt.title('Age distribution histogram')
plt.scatter(x,y,label = 'Scatter plot example 2', color = 'black',marker = '*',s=100)
plt.show()
