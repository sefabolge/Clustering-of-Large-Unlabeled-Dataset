# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mtl
data = [];
colorDict = {0: 'blue', 1: 'red', 2: 'green', 3: 'orange' }
activity = 0
lang = 0
cluster = 0

def return_colour( cluster ):	
    ret = []
    for i in cluster:
        ret.append(str(colorDict[i]))
    return ret
#File should be your analysis file.. 
file = open('language_analysis.csv', 'r')
try:
	for line in file:
	    l = line.split(',')
	    cluster = int(l[0])
	    #userId = int(l[1])
	    language = int(l[1])
	    activity = int(l[2])
	    data.append([language, activity, cluster])
except:
	n = None

tData = list(zip(*data))

fig, ax = plt.subplots()
ax.scatter(tData[1], tData[0],s=1, c=tData[2] )
ax.set_xlabel('Language')
ax.set_ylabel('Activity')

fig.suptitle('Language analysis in StackOverFlow')
fig.subplots_adjust(wspace=0.09)
plt.show()
