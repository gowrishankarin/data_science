
# coding: utf-8

# In[1]:


import matplotlib.pylab as plt
import seaborn as sns
sns.despine


# In[2]:


from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.normalization import BatchNormalization
from keras.layers import Merge, LeakyReLU
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, CSVLogger, EarlyStopping
from keras.optimizers import RMSprop, Adam, SGD, Nadam
from keras.layers.advanced_activations import *
from keras.layers import Convolution1D, MaxPooling1D, AtrousConvolution1D
from keras.layers.recurrent import LSTM, GRU
from keras import regularizers


# In[3]:


from preprocessing import shuffle_in_unison, create_Xt_Yt


# In[13]:


import pandas as pd

data = pd.read_csv("../datasets/snp/table.csv")[::-1]
data.head()


# In[14]:


data = data.loc[:, 'Adj Close'].tolist()
plt.plot(data)
plt.show()


# In[15]:


WINDOW = 30
EMB_SIZE = 1
STEP = 1
FORECAST = 5


# In[16]:


# Create time window
X, Y = [], []
for i in range(0, len(data), STEP):
    try:
        x_i = data[i:i + WINDOW]
        y_i = data[i + WINDOW + FORECAST]

        last_close = x_i[WINDOW - 1]
        next_close = y_i

        if last_close < next_close:
            y_i = [1, 0]
        else:
            y_i = [0, 1]
    except Exception as e:
        print(e)
        break
        
    X.append(x_i)
    Y.append(y_i)


# In[17]:


print(len(X))
print(len(X))


# In[18]:


import numpy as np
X = [(np.array(x) - np.mean(x)) / np.std(x) for x in X]
X, Y = np.array(X), np.array(Y)

X_train, X_test, Y_train, Y_test = create_Xt_Yt(X, Y)


# In[25]:


print(X.shape)
print(Y.shape)
print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)


# In[22]:


model = Sequential()
model.add(Dense(64, input_dim=30, activity_regularizer=regularizers.l2(0.01)))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Dropout(0.5))
model.add(Dense(16, activity_regularizer=regularizers.l2(0.01)))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Dense(2))
model.add(Activation('softmax'))

opt = Nadam(lr=0.001)

reduce_lr = ReduceLROnPlateau(monitor='val_acc', factor=0.9, patience=25, min_lr=0.000001, verbose=1)
checkpointer = ModelCheckpoint('output/test.hdf5', verbose=1, save_best_only=True)
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])


# In[24]:


H = model.fit(X_train, Y_train, epochs=50, batch_size=128, verbose=1,
    validation_data=(X_test, Y_test), callbacks=[reduce_lr, checkpointer], shuffle=True)


# In[ ]:


plt.figure()
plt.plot(H.history['loss'])
plt.plot(H.history['val_loss'])
plt.title("Model Loss")
plt.ylabel("Loss")
plt.xlabel("Epoch")
plt.legend(['train', 'test'], loc='best')
plt.show()


# In[ ]:


plt.figure()
plt.plot(H.history['acc'])
plt.plot(H.history['val_acc'])
plt.title("Model Accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Epoch")
plt.legend(['train', 'test'], loc='best')
plt.show()


# In[ ]:


from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

pred = model.predict(np.array(X_test))
C = confusion_matrix([np.argmax(y) for y in Y_test], [np.argmax(y) for y in pred])

print(C/C.astype(np.float).sum(axis=1))

FROM = 0
TO = FROM + 500

original = Y_test[FROM:TO]
predicted = pred[FROM:TO]

plt.plot(original, color='black', label='Original Data')
plt.plot(predicted, color='blue', label='Predicted Data')
plt.legend(loc = 'best')
plt.title("Actual and Predicted from point {} to point {} of test set".format(FROM, TO))
plt.show()


# In[ ]:














































