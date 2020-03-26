import numpy as np
import pandas as pd

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


def split_train_test_in_unison(X, y, percentage=0.8):
    split = int(np.floor(len(X) * percentage))
    
    X_train = X[0:split]
    Y_train = y[0:split]
    
    X_train, Y_train = shuffle_in_unison(X_train, Y_train)
    
    X_test = X[split:]
    Y_test = y[split:]
    
    return X_train, X_test, Y_train, Y_test

def data_2_percentage_change(data):
    change = pd.DataFrame(data).pct_change()
    change = change.replace([np.inf, -np.inf], np.nan)
    change = change.fillna(0.0).values.tolist()
    change = [c[0] for c in change]
    return change