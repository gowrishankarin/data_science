import pandas as pd
import numpy as np
import time
from datetime import date
from pandas import Series, DataFrame

import logging
import _pickle as cPickle

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')

IMG_HELP_PATH = '/Users/shankar/dev/code/ds/studies/data_science/trading/honchar'
import os
import sys
sys.path.append(os.path.abspath(IMG_HELP_PATH))
from common.preprocessing import data_2_percentage_change


def load_text_csv(filename='Combined_News_DJIA.csv', date_split=date(2014, 12, 31)):
    df = pd.read_csv(filename)
    df['Combined'] = df.iloc[:, 2:27].apply(lambda row: ''.join(str(row.values)), axis=1)
    
    train = df.loc[(pd.to_datetime(df["Date"]) <= date_split), ['Label', 'Combined']]
    test = df.loc[(pd.to_datetime(df["Date"]) > date_split), ['Label', 'Combined']]
    
    return train, test


def load_ts_csv(filename='DJIA_table.csv', date_split=date(2014, 12, 31)):
    data = pd.read_csv(filename)[::-1]
    
    train2 = data.loc[(pd.to_datetime(data["Date"]) <= date_split)]
    test2 = data.loc[(pd.to_datetime(data["Date"]) > date_split)]
    
    open_train = train2.loc[:, 'Open']
    open_test = test2.loc[:, 'Open']
    open_train = data_2_percentage_change(open_train)
    open_test = data_2_percentage_change(open_test)
    
    high_train = train2.loc[:, 'High']
    high_test = test2.loc[:, 'High']
    high_train = data_2_percentage_change(high_train)
    high_test = data_2_percentage_change(high_test)
    
    low_train = train2.loc[:, 'Low']
    low_test = test2.loc[:, 'Low']
    low_train = data_2_percentage_change(low_train)
    low_test = data_2_percentage_change(low_test)
    
    close_train = train2.loc[:, 'Close']
    close_test = test2.loc[:, 'Close']
    close_train = data_2_percentage_change(close_train)
    close_test = data_2_percentage_change(close_test)
    
    volume_train = train2.loc[:, 'Volume']
    volume_test = test2.loc[:, 'Volume']
    volume_train = data_2_percentage_change(volume_train)
    volume_test = data_2_percentage_change(volume_test)
    
    train = np.column_stack((open_train, high_train, low_train, close_train, volume_train))
    test = np.column_stack((open_test, high_test, low_test, close_test, volume_test))
    
    return train, test


from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer


def text_process(text):
    '''
    Takes in a string of text, then performs the following
    1. Tokenizes and removes punctuation
    2. Removes stopwords
    3. Stems
    4. Returns a list of the cleaned text
    '''
    if(pd.isnull(text)):
        return []
    
    # Tokenize 
    tokenizer = RegexpTokenizer(r'\w+')
    text_processed = tokenizer.tokenize(text)
    
    # Removing any stopwords
    text_processed = [word.lower() for word in text_processed if word.lower() not in stopwords.words('english')]
    
    # Stemming
    porterStemmer = PorterStemmer()
    
    text_processed = [porterStemmer.stem(word) for word in text_processed]
    
    try:
        text_processed.remove('b')
        
    except:
        pass
    
    return " ".join(text_processed)
    
    
def transform_text_2_sentences(train, test, save_train='../output/train_text.p', save_test='../output/test_text.p'):
    '''
    Transforming raw text into sentences, if @save_train or @save_test in not None - saves
    pickles for further use
    '''
    train_text = []
    test_text = []
    for each in train['Combined']:
        train_text.append(text_process(each))
    
    for each in test['Combined']:
        test_text.append(text_process(each))
        
    if(save_train != None):
        cPickle.dump(train_text, open(save_train, 'wb'))
        
    if(save_test != None):
        cPickle.dump(test_text, open(save_test, 'wb'))
        
    return train_text, test_text

from gensim.models import Word2Vec


def transform_text_into_vectors(train_text, test_text, embedding_size=100, model_path='../output/word2vec10.model'):
    
    '''
    Transforms sentences into sequences of word2vec vectors. Returns
    train, test set and trained word2vec model
    '''
    
    data_for_w2v = []
    for text in train_text + test_text:
        words = text.split(' ')
        data_for_w2v.append(words)
        
    model = Word2Vec(data_for_w2v, size=embedding_size, window=5, min_count=1, workers=4)
    model.save(model_path)
    model = Word2Vec.load(model_path)
    
    train_text_vectors = [[model[x] for x in sentence.split(' ')] for sentence in train_text]
    test_text_vectors = [[model[x] for x in sentence.split(' ')] for sentence in test_text]
    
    
    train_text_vectors = [np.mean(x, axis=0) for x in train_text_vectors]
    test_text_vectors = [np.mean(x, axis=0) for x in test_text_vectors]
    
    return train_text_vectors, test_text_vectors, model


def split_into_XY(data_chng_train, train_text_vectors, step, WINDOW, FORECAST):
    '''
    Splits textual and time series data into train or test dataset for hybrid model;
    Objective y_i is percentage change of price movement for next day
    '''
    X_train, X_train_text, Y_train, Y_train2 = [], [], [], []
    
    for i in range(0, len(data_chng_train), step):
        try:
            x_i =data_chng_train[i:i+WINDOW]
            y_i = np.std(data_chng_train[i:i+WINDOW+FORECAST][3])
            
            text_average = train_text_vectors[i:i+WINDOW]
            last_close = x_i[-1]
            
            y_i2 = None
            if(data_chng_train[i+WINDOW+FORECAST][3] > 0.0):
                y_i2 = 1.
            else:
                y_i2 = 0.
                
        except Exception as e:
            print('KEK', e)
            break
            
        X_train.append(x_i)
        X_train_text.append(text_average)
        Y_train.append(y_i)
        Y_train2.append(y_i2)
        
    X_train, X_train_text, Y_train, Y_train2 = np.array(X_train), np.array(X_train_text), np.array(Y_train), np.array(Y_train2)
    return X_train, X_train_text, Y_train, Y_train2