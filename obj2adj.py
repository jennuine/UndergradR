import glob
import os
import math
import numpy as np
import operator


def euclidianD(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)


def nnsearch(a, b):
    g = []
    for ii in a:
        l = []
        for number, jj in enumerate(b):
            l.append(euclidianD(ii, jj))
        (m, i) = min((v, i) for i, v in enumerate(l))
        g.append((m, i))
    return g
l = []
f = glob.glob('data/p2_c56_BenH.obj_R20/*')

k = f[0]
h = f[1]

with open(k) as f:
    content = f.readlines()

con1 = [ii.rstrip() for ii in content if len(ii) > 1]
con2 = [each[2:] for each in con1 if each[0] == 'v']
con7 = [each.split() for each in con2]
con8 = [[float(X) for X in each] for each in con7]
cell = np.asarray(con8)

with open(h) as f:
    content1 = f.readlines()
con3 = [ii.rstrip() for ii in content1 if len(ii) > 1]
con4 = [each[2:] for each in con3 if each[0] == 'v']
con5 = [each.split() for each in con4]
con6 = [[float(X) for X in each] for each in con5]
dend = np.asarray(con6)

answer = nnsearch(cell, dend)
print answer
