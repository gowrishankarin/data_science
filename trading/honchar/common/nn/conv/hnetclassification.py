from keras.models import Sequential
from keras.layers.convolutional import Conv1D
from keras.layers.core import Activation, Flatten, Dense, Dropout
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Nadam

class HNetClassification():
    
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
        model.add(Dropout(0.5))
        
        model.add(Flatten())
        
        model.add(Dense(64))
        model.add(BatchNormalization())
        model.add((Activation('relu')))
        
        model.add(Dense(2))
        model.add(Activation('softmax'))
        
        opt = Nadam(lr=0.002)
        model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
        
        return model

