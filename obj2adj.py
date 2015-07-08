import glob
import os
import math
import numpy as np
import operator
import sys
#import ThreeDObject

print "syst.arv => %s" % sys.argv


class ThreeDObject:

    def __init__(self, name, filepath):
        self.name = name
        self.filepath = filepath
        self.list = []
        self.setList(filepath)

    def setList(self, filepath):
        self.list.append(self.extractOBJ(filepath))

    def extractOBJ(self, filepath):

        with open(filepath) as f:
            content = f.readlines()

        #print "content => %s" %content
        
        con1 = [ii.rstrip() for ii in content if len(ii) > 1]
        print "con1 => %s" %con1[0]
        con2 = [each[2:] for each in con1 if each[0] == 'v']
        print "con2 => %s" %con2[0]
        con7 = [each.split() for each in con2]
        print "con7 => %s" %con7[0]
        con8 = [[float(X) for X in each] for each in con7]
        print "con8 => %s" %con8[0]
        
        l = np.asarray(con8)
        return l

    def getName(self): return self.name

    def getList(self): return self.list


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
#f = glob.glob('data/p2_c56_BenH.obj_R20/*')
var = ThreeDObject('cell', 'cellbody.obj')
var.setList('cellbody.obj')

print "var.getName() => %s" %var.getName()

"""k = f[0]
h = f[1]



with open(h) as f:
    content1 = f.readlines()
con3 = [ii.rstrip() for ii in content1 if len(ii) > 1]
con4 = [each[2:] for each in con3 if each[0] == 'v']
con5 = [each.split() for each in con4]
con6 = [[float(X) for X in each] for each in con5]
dend = np.asarray(con6)

answer = nnsearch(cell, dend)
print answer"""
