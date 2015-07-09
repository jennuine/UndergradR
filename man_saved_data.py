import numpy as np
import pickle
from termcolor import cprint
#data = np.load("data.npy")
#cprint(data.tolist(), 'cyan')#data.tolist()

data = pickle.load(open("saved_data"))
cprint(data, 'cyan')