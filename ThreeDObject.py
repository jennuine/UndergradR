import glob
import numpy as np

class ThreeDObject:

    def __init__(self, name, filepath):
        self.name = name
        self.filepath = filepath
        self.list = []

    def setList(self, x):
        self.list.append(self.readOBJ(x))

    def readOBJ(self, filepath):

        with open(filepath) as f:
            content = f.readlines()
        con1 = [ii.rstrip() for ii in content if len(ii) > 1]
        print con1[0]
        con2 = [each[2:] for each in con1 if each[0] == 'v']
        print con2[0]
        con7 = [each.split() for each in con2]
        print con7[0]
        con8 = [[float(X) for X in each] for each in con7]
        print con8[0]
        
        l = np.asarray(con8)
        return l

    def name():
        return self.name