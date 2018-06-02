from keras.models import Sequential
from keras.layers.convolutional import Conv1D
from keras.layers.core import Activation, Flatten, Dense, Dropout
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Nadam

class HNetRegression():
    
    @staticmethod
    def build(inputShape):
        
        # Initialize the model
        model = Sequential()
        
        model.add(Conv1D(
            input_shape=inputShape,
            nb_filter=16,
            filter_length=4,
            border_mode='same'
        ))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        # model.add(Dropout(0.5))
        
        model.add(Flatten())
        
        model.add(Dense(64))
        model.add(BatchNormalization())
        model.add((Activation('relu')))
        
        model.add(Dense(1))
        model.add(Activation('linear'))
        
        opt = Nadam(lr=0.002)
        model.compile(optimizer=opt, loss='mse', metrics=['accuracy'])
        
        return model

