#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

def get_inds(ped_fi):
    inds = []
    with open(ped_fi) as pf:
        for l in pf:
            pop, ind, gt = l.split(' ',2)
            inds.append([pop, ind])
    return inds

def get_colors(n):
    if n < 10:
        return plt.cm.Set1(np.linspace(0, 1, 10))
    elif n < 12:
        return plt.cm.Set1(np.linspace(0, 1, 12))
    else:
        return plt.cm.Set3(np.linspace(0, 1, n))

def get_pop_xcoords(inds):
    currpop = ''
    vlines=[]
    pop_labels=[]
    pop_coords=[]

    for ind in inds:
        if currpop == '':
            currpop = ind[0]
            pop_labels.append(ind[0])
            curr_inds = 1
            xcoord = 0

        elif ind[0] == currpop:
            curr_inds+=1
            xcoord+=1

        elif ind[0] != currpop:
            currpop = ind[0]
            pop_labels.append(ind[0])
            pop_coords.append(xcoord-(curr_inds/2.))
            xcoord+=1
            vlines.append(xcoord)
            curr_inds=0

    pop_coords.append(xcoord-(curr_inds/2.))

    return vlines, pop_labels, pop_coords

def plot_Q(inds, Q, k):
    colors = get_colors(k)
    width=1
    xcoord = np.arange(len(inds)*width, step=width)
    bars=[]
    plt.figure(figsize=(20,6))
    for ki in range(k):
        for i, ind in enumerate(inds):
            h = np.sum(Q[i,0:ki+1])
            b = np.sum(Q[i,0:ki])
            bars.append( plt.bar(left=xcoord[i], height=h, bottom=b, width=width, color=colors[ki], edgecolor='none') )

    plt.title('Admixture Plot, K='+str(k))
    plt.grid(False)
    plt.xlim([0,xcoord[-1]+width])
    plt.ylim([0,1])
    vlines, pop_labels, pop_coords = get_pop_xcoords(inds)
    plt.vlines(vlines, 0, 1, colors='k', linestyles='solid', linewidth=1)
    plt.xticks(pop_coords, pop_labels, rotation=60, fontsize=12, ha='right')
    plt.tick_params(axis='x', which='both', bottom='on', top='off', direction='out')
    plt.tick_params(axis='y', which='both', left='off', right='off', labelleft='off')
    plt.tight_layout()
    plt.show()

ped_file = sys.argv[1]
q_file = sys.argv[2]

inds = get_inds(ped_file)
df = pd.read_table(q_file, sep=' ', header=None)
Q = np.array(df)
K=int(Q.shape[1])

plot_Q(inds, Q, K)
