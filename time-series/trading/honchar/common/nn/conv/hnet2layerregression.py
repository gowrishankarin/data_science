from keras.models import Sequential
from keras.layers.convolutional import Conv1D
from keras.layers.core import Activation, Flatten, Dense, Dropout
from keras.layers import MaxPooling1D

class HNet2LayerRegression():

    @staticmethod
    def build(inputShape):
        model = Sequential()
        model.add(Conv1D(
            input_shape=inputShape,
            filters=64,
            kernel_size=2,
            padding='valid',
            activation='relu',
            strides=1
        ))

        model.add(MaxPooling1D(pool_size=2))

        model.add(Conv1D(
            input_shape=inputShape,
            filters=64,
            kernel_size=2,
            padding='valid',
            activation='relu',
            strides=1
        ))
        model.add(MaxPooling1D(pool_size=2))

        model.add(Dropout(0.25))
        model.add(Flatten())

        model.add(Dense(250))
        model.add(Dropout(0.25))
        model.add(Activation('relu'))

        model.add(Dense(1))
        model.add(Activation('linear'))

        return model