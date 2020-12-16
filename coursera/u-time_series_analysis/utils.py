import os
import pandas as pd
import numpy as np

DATA_DIR = '../data'

def get_index_2018():
    raw_csv_data = pd.read_csv(os.path.join(DATA_DIR, "Index2018.csv"))
    df_comp  = raw_csv_data.copy()
    df_comp.date = pd.to_datetime(df_comp.date, dayfirst=True)
    df_comp.set_index('date', inplace=True)
    df_comp = df_comp.asfreq('b')
    df_comp = df_comp.fillna(method='ffill')
    
    return df_comp
    
    
def get_index_2018_market_value(market_name='spx'):
    df_comp = get_index_2018()
    df_comp['market_value'] = df_comp[market_name]
    del df_comp['spx'], df_comp['dax'], df_comp['nikkei'], df_comp['ftse']
    
    return df_comp
    
def get_index_2018_market_value_splits(market_name='spx', white_noise=True):    
    df_comp = get_index_2018_market_value(market_name)
    size = int(len(df_comp)*0.8)
    df = df_comp.iloc[:size]
    df_test = df_comp.iloc[size:]
    if(white_noise == True):
        wn = np.random.normal(loc=df.market_value.mean(), scale=df.market_value.std(), size=len(df))
        df['wn'] = wn
        
    return df, df_test

def get_random_walk_data():
    rw = pd.read_csv(os.path.join(DATA_DIR, "RandWalk.csv"))
    rw.date = pd.to_datetime(rw.date, dayfirst=True)
    rw.set_index("date", inplace=True)
    rw = rw.asfreq('b')
    
    return rw


from scipy.stats.distributions import chi2
def LLR_test(mod_1, mod_2, DF=1):
    L1 = mod_1.fit().llf
    L2 = mod_2.fit().llf
    
    LR = (2*(L2-L1))
    p = chi2.sf(LR, DF).round(3)
    
    return p

from statsmodels.tsa.arima_model import ARMA
def ARMA_LLR_test(data, model_ar_x_1, x):
    model_ar_x = ARMA(data, order=(x, 0))
    results_ar_x = model_ar_x.fit()
    llr = None
    if(model_ar_x_1 != None):
        llr = LLR_test(model_ar_x_1, model_ar_x)
        
    return (model_ar_x, llr)