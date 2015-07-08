import glob
import os
import math
import numpy as np
import operator
import sys
from termcolor import cprint
import scipy.spatial.distance as scipy
#import ThreeDObject

sprint = lambda x : cprint('\t' + x, 'magenta')#, attrs=['bold'])
rprint = lambda x : cprint('\t\t' + x, 'red')
cyan = lambda x: cprint(x, 'cyan')

class ThreeDObject:

    def __init__(self, name, filepath):
        """
        Constructor: creates new ThreeDObject
        """
        self.name = name
        self.filepath = filepath
        self.list = self.extractOBJ(filepath)

    def __str__(self): return self.name
    def __repr__(self): return str(self.list)

    def extractOBJ(self, filepath):
        """
        Returns an array containing (x, y, z) coordinates for the .obj vertices
        """
        with open(filepath) as f:
            content = f.readlines()
        
        #cyan(content)

        con1 = [ii.rstrip() for ii in content if len(ii) > 1]
        sprint("con1 => %s" %con1[0])
        con2 = [each[2:] for each in con1 if each[0] == 'v']
        sprint("con2 => %s" %con2[0])
        con7 = [each.split() for each in con2]
        sprint("con7 => %s" %con7[0])
        con8 = [[float(X) for X in each] for each in con7]
        sprint("con8 => %s" %con8[0])
        
        l = np.asarray(con8)
        #cyan(l)
        return l

    def getName(self): return self.name
    def getList(self): return self.list


def euclidianD(p1, p2):
    """
    Returns the euclidian distance between p1 and p2 points
    """
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)


def nnsearch(a, b):
    """
    Returns an matrix of shortest paths from a and b
    """
    g = []
    for ii in a:
        l = []
        for number, jj in enumerate(b):
            l.append(euclidianD(ii, jj))
        (m, i) = min((v, i) for i, v in enumerate(l))
        g.append((m, i))
    return g

def store(args):
    """
    Returns an array of ThreeDObjects based on filepath contained in args
    """
    objs = []

    for path in args[1:]:
        obj = ThreeDObject(path.rstrip('.obj'), path)
        objs.append(obj)
        rprint("obj => %s" %obj)
    return np.asarray(objs)

objs = store(sys.argv)

#cyan(objs)

obj1 = objs[0].getList()
obj2 = objs[1].getList()

answer = obj1.
print answer
cyan(answer)

