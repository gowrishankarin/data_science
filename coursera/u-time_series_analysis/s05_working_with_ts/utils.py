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