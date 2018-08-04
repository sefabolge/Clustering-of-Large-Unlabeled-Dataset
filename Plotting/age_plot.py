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
file = open('dataAge_our_kmeans.csv', 'r')
for line in file:
    l = line.split(',')
    age = int(l[1])
    reputation = int(l[2])
    answer_count = int(l[3])
    cluster = int(l[0])
    data.append([age,reputation, answer_count, cluster])

import matplotlib.patches as mpatches
patch0 = mpatches.Patch(color=colorDict[0], label='Cluster 0')
patch1 = mpatches.Patch(color=colorDict[1], label='Cluster 1')
patch2 = mpatches.Patch(color=colorDict[2], label='Cluster 2')
patch3 = mpatches.Patch(color=colorDict[3], label='Cluster 3')

tData = list(zip(*data))

colourList = return_colour(tData[3])

fig, ax = plt.subplots(ncols=2, sharey=True)
ax[0].barh(tData[0], tData[1], 1, align='center', color=colourList)
ax[1].barh(tData[0], tData[2], 1, align='center', color=colourList)

ax[0].invert_xaxis()
ax[0].yaxis.tick_right()
ax[0].set(yticks=range(15,100,5))
ax[0].set_title('Reputation')
ax[1].set_title('Amount of Answers')

fig.suptitle('Age analysis in StackOverFlow')
fig.subplots_adjust(wspace=0.09)
fig.legend( [patch0, patch1, patch2, patch3],['Cluster 0', 'Cluster 1','Cluster 2', 'Cluster 3'], loc = 'lower right', ncol=2, labelspacing=0. )

plt.ylim(15, 100)
plt.show()
