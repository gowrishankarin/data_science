
# coding: utf-8

# In[1]:


from sklearn import preprocessing
from sklearn.metrics import mean_squared_error, classification_report
import numpy as np
import matplotlib.pylab as plt
import datetime as dt
import time
import numpy as np


# In[2]:


def load_snp_returns():
    f = open("../datasets/snp/table.csv", "r").readlines()[1:]
    raw_data = []
    raw_dates = []
    i = 0
    for line in f:
       # if i == 0 or i % 500000 == 0: 
       #     print(line)
        try:
            splits = line.split(',')
            open_price = float(splits[1])
            close_price = float(splits[4])
            raw_data.append(close_price - open_price)
            raw_dates.append(splits[0])
        except:
            continue
    
    return raw_data[::-1], raw_dates[::-1]


# In[4]:


import pandas as pd

def load_snp_returns_pd():
    return pd.read_csv("../datasets/snp/table.csv")


# In[7]:


def load_snp_close():
    f = open('../datasets/snp/table.csv', 'r').readlines()[1:]
    raw_data = []
    raw_dates = []
    for line in f:
        try:
            splits = line.split(',')
            close_price = float(splits[4])
            raw_data.append(close_price)
            raw_dates.append(splits[0])
        except:
            continue
            
    return raw_data, raw_dates
            


# In[9]:


def split_into_chunks(data, train, predict, step, binary=True, scale=True):
    X, Y = [], []
    for i in range(0, len(data), step):
        try:
            
            x_i = data[i:i+train]
            y_i = data[i+train+predict]
            
            if binary:
                if y_i > 0:
                    y_i = [1., 0.]
                else:
                    y_i = [0., 1.]
                    
                if scale: 
                    x_i = preprocessing.scale(x_i)
            
            else:
                timeseries = np.array(data[i:i+train+predict])
                if scale: 
                    timeseries = preprocessing.scale(timeseries)
                x_i = timeseries[:-1]
                y_i = timeseries[-1]
                    
        except:
            break
            
        X.append(x_i)
        Y.append(y_i)
        
    return X, Y
                
        


# In[10]:


def shuffle_in_unison(a, b):
    # courtsey http://stackoverflow.com/users/190280/josh-bleecher-snyder
    
    assert len(a) == len(b)
    shuffled_a = np.empty(a.shape, dtype=a.dtype)
    shuffled_b = np.empty(b.shape, dtype=b.dtype)
    permutation = np.random.permutation(len(a))
    for old_index, new_index in enumerate(permutation):
        shuffled_a[new_index] = a[old_index]
        shuffled_b[new_index] = b[old_index]
    
    return shuffled_a, shuffled_b


# In[11]:


def create_Xt_Yt(X, y, percentage=0.8):
    split = int(np.floor(len(X) * percentage))
    X_train = X[0:split]
    Y_train = y[0:split]
    
    X_train, Y_train = shuffle_in_unison(X_train, Y_train)
    
    X_test = X[split:]
    Y_test = y[split:]
    
    return X_train, X_test, Y_train, Y_test


# In[12]:


# Great


# In[13]:


#get_ipython().system('jupyter nbconvert --to python 001_Preprocessing.ipynb')
#get_ipython().system('mv 001_Preprocessing.py preprocessing.py')
































