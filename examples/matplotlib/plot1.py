#!/usr/bin/python3
import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,4,7]

x2 = [1,2,3]
y2 = [10,14,12]


plt.xlabel('Plot Number')
plt.ylabel('Important variable')

plt.title("My first graph\nIt's teh awesome!")
plt.plot(x,y,label = 'First Line')
plt.plot(x2,y2,label = 'Second Line')
plt.legend()
plt.show()
