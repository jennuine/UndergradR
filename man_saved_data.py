import numpy as np
import pickle
from termcolor import cprint
import math

sprint = lambda x : cprint('\t' + x, 'magenta')#, attrs=['bold'])
rprint = lambda x : cprint('\t\t' + x, 'red')
cyan = lambda x: cprint(x, 'cyan')


data = pickle.load(open("saved_data"))
"""
data <type 'list'>
data[0] <type 'tuple'>
	(data[0])[0] <type 'float'>
	(data[0])[1] <type 'int'>
		(float distance, int index)
"""

cyan(pickle.load(open("input7_vs_input7")))

"""
#cprint(data, 'cyan')
#cyan(type((data[0])[1]))
(x, y) = data[0]
cyan(x)
print y

def radix_sort(arr):
    max = -1
    for (row, row2) in arr:
        num = int(math.log10(row)) + 1
        if num > max:
            max = num

    buckets = [[] for i in range(0, 10)] #buckets for each digit
    for digit in range(0, max):
        for (number, row2) in arr:
        	x = int(number)
        	buckets[x / 10**digit % 10].append(number)
        	del arr[:]
        for bucket in buckets:
            arr.extend(bucket)
            del bucket[:]
    return arr

cyan(radix_sort(data))
"""