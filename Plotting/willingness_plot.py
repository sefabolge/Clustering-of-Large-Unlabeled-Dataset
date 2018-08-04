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
#file = open('willingness_analysis.csv', 'r')
file = open('willingness_analysis_mllib.csv', 'r')
for line in file:
    l = line.split(',')
    cluster = int(l[2])
    #userId = int(l[1])
    reputation = int(l[0])
    totalScore = int(l[1])
    data.append([reputation, totalScore, cluster])

import matplotlib.patches as mpatches
patch0 = mpatches.Patch(color=colorDict[0], label='Cluster 0')
patch1 = mpatches.Patch(color=colorDict[1], label='Cluster 1')
patch2 = mpatches.Patch(color=colorDict[2], label='Cluster 2')
patch3 = mpatches.Patch(color=colorDict[3], label='Cluster 3')

#tData = list(zip(*data))

#colourList = return_colour(tData[2])

fig, ax = plt.subplots()
#ax.scatter(tData[1], tData[0],s=1, color=colourList )
ax.set_xlabel('Reputation')
ax.set_ylabel('Answer Count')

fig.suptitle('Willingness analysis in StackOverFlow')
fig.subplots_adjust(wspace=0.09)    
fig.legend( [patch0, patch1, patch2, patch3],['Cluster 0', 'Cluster 1','Cluster 2', 'Cluster 3'], loc = 'lower right', ncol=2, labelspacing=0. )
plt.ylim(-10, 23000)
plt.xlim(-10, 800000)
#plt.show()
c0 = filter(lambda l: l[2] == 0,data)
c1 = filter(lambda l: l[2] == 1,data)
c2 = filter(lambda l: l[2] == 2,data)
c3 = filter(lambda l: l[2] == 3,data)
total = data.__len__()

print('Cluster 0 Size: '+ str(c0.__len__()) + '('+ str(c0.__len__()*100.00/total) +'%)')
print('Cluster 1 Size: '+ str(c1.__len__()) + '('+ str(c1.__len__()*100.00/total) +'%)')
print('Cluster 2 Size: '+ str(c2.__len__()) + '('+ str(c2.__len__()*100.00/total) +'%)')
print('Cluster 3 Size: '+ str(c3.__len__()) + '('+ str(c3.__len__()*100.00/total) +'%)')
print('Total Size: '+ str(total))
