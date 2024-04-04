# plottask.py
# This programs displays a histogram of 1000 values with a mean of 5 and standard deviation of 2
# and a plot of the function h(x)=x^3 in the range 0 to 10 on the one set of axes.
# Author: Louise Ryan


import matplotlib.pyplot as plt      #matplotlib-->library for creating plots in python.pyplot-->module within matplotlib
import numpy as np                   #numpy library used to store and manipulate numerical data

xpoints = np.array(range(0,11))      #numpy array created with integers 0-10. 11 to ensure 10 is included in the plot      
ypoints = xpoints*xpoints*xpoints    #the cubed value of the xpoints array.
plt.plot(xpoints, ypoints, label = '$h(x)=x^3$', color='red')

np.random.seed(1)      #to ensure that the same sequence of numbers are generated each time.

mean = 5
std_dev = 2
data = np.random.normal(mean, std_dev, size = 1000)
plt.hist(data, label = 'Normal Distribution', color='lightgrey', edgecolor='black')

plt.legend()
plt.title('Random distribution histogram with function plot', fontsize=10, fontweight='bold', color='darkblue')
plt.xlabel('x-axis', fontweight='bold')
plt.ylabel('y-axis', fontweight='bold')
plt.grid(alpha=0.3)
plt.savefig('plottask')



# References:
# https://s3-us-west-2.amazonaws.com/python-notes/a-whirlwind-tour-of-python-2.pdf
# https://www.w3schools.com/python/matplotlib_intro.asp
# https://python-charts.com/distribution/histogram-matplotlib/
# https://python-charts.com/matplotlib/
# https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm