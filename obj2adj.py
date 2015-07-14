import os
import math
import numpy as np
import operator
import sys
from termcolor import cprint, colored
from ThreeDObject import ThreeDObject
import pickle

sprint = lambda x : cprint('\t' + x, 'magenta')#, attrs=['bold'])
rprint = lambda x : cprint('\t\t' + x, 'red')
cyan = lambda x: cprint(x, 'cyan')

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

    for index, ii in enumerate(a):
        l = []
        for number, jj in enumerate(b):
            l.append(euclidianD(ii, jj))
        (m, i) = min((v, i) for i, v in enumerate(l))
        g.append((m, i))
        #rprint(str(index))
        show_progress(index, len(a), 20)
    return g

def store(args):
    """
    Returns an array of ThreeDObjects based on filepath contained in args
    """
    objs = []

    for path in args[1:]:
        obj = ThreeDObject(path.rstrip('.obj'), path)
        objs.append(obj)
        #rprint("obj => %s" %obj)
    return np.asarray(objs)

def show_progress(index, end_val, bar_length):
    """
    Displays the progress of the process running
    """
    percent = float(index) / end_val
    hashes = '#' * int(round(percent * bar_length))
    spaces = ' ' * (bar_length - len(hashes))
    text = "\b\tProcess: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100)))
    sys.stdout.write("\r {:<70}".format(text))
    sys.stdout.flush()

def radix_sort(arr):
    max = -1
    for row in arr[0:]:
        num = int(math.log10(row)) + 1
        if num > max:
            max = num

    buckets = [[] for i in range(0, 10)] #buckets for each digit
    for digit in range(0, max):
        for number in arr[0:]:
            buckets[number / 10**digit % 10].append(number)
            del arr[:]
            for buckets in buckets:
                array.extend(buckets)
                del bucket[:]
    return arr

global minDistList
minDistList = []

def compareAll(objs):
    """
    Compares all elements using nnsearch stored in objs & saves it's compared data file
    """
    for i1, element in enumerate(objs):
        if (i1 + 1) < len(objs):
            count = 0
            for i2, element2 in enumerate(objs[i1 + 1:]):
                sprint('Comparing %s vs %s' %(str(element), str(element2)))
                count = count + 1
                answer = nnsearch(element.getList(), element2.getList())
                print "\n"
                minDistList.append(answer)
                a = element
                b = element2
        
        text = "%s_vs_%s" %(str(a), str(b))
        pickle.dump(answer, open(text, "w"))



"""******************************************************************"""


objs = store(sys.argv)

compareAll(objs)

"""
#cyan(objs)

obj1 = objs[0].getList()
obj2 = objs[1].getList()

answer = nnsearch(obj1, obj2)

#np.save("data.npy", answer)

pickle.dump(answer, open("saved_data", "w"))


cyan(answer)

rprint(radix_sort(answer))
"""
