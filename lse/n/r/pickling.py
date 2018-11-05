import pickle
from pathlib import Path

def pickle_var(var, filename):
    #with open(Path(filename), 'wb') as p:
    with open(filename, 'wb') as p:
        pickle.dump(var, p)
    return

def depickle(filename):
    with open(Path(filename), 'rb') as p:
        v = pickle.load(p)
    return v
