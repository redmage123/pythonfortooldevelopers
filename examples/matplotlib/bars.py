#!/usr/bin/python3

import matplotlib.pyplot as plt

x = [2,4,5,6,8,10]
y = [6,7,8,2,4,1]

plt.bar (x,y,label = 'Bars1')


plt.xlabel('x')
plt.ylabel('y')

plt.title('First bar chart')
plt.legend()

plt.show()
