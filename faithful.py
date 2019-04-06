#old faithful data set 
# 6th April 2019

#calculate mean each column

import numpy
data = numpy.genfromtxt('data1/faithful.csv',delimiter=',')
firstcol = data[:,0]
meanfirstcol = numpy.mean(data[:,0])
meansecondcol = numpy.mean(data[:,1])
