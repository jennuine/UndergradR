import numpy as np
from termcolor import cprint

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