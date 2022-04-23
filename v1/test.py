import seaborn as sns
import numpy as np
from numpy.random import randn
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

def ZscoreNormalization(x):
  """Z-score normaliaztion"""
  x = (x - np.mean(x)) / np.std(x)
  return x

#将读入的txt直接转化成list
exp_836=[]
with open('nSyb_836 Exp.txt') as f1:
    for line in f1:
        exp_836.extend([float(i) for i in line.split()])

print(exp_836)

naive_836=[]
with open('nSyb_836 Naive.txt') as f2:
    for line in f2:
        naive_836.extend([float(i) for i in line.split()])



sns.kdeplot(ZscoreNormalization(exp_836), shade=True,color='r',label='exp_836')
sns.kdeplot(ZscoreNormalization(naive_836), shade=True,color='g',label='naive_836')

