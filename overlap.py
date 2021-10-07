import numpy as np
from scipy.stats import hypergeom

def get_overlap(x,y):
    return np.isin(x,y).sum()

def get_pval(setA, setB, population):
    x = np.isin(setA,setB).sum() # number of successes
    M = len(population) # pop size
    k = len(setB) # successes in pop
    N = len(setA) # sample size
    pval = hypergeom.sf(x-1, M, k, N)
    return pval