from keras.models import Sequential
from keras.layers.convolutional import Conv1D
from keras.layers.core import Activation, Flatten, Dense, Dropout, MaxPooling1D

class HNet2LayerRegression():

    @staticmethod
    def build(inputShape):
        model = Sequential()
        model.add(Conv1D(
            input_shape=inputShape,
            nb_filter=64,
            filter_length=2,
            border_mode='valid',
            activation='relu',
            subsample_length=1
        ))

        model.add(MaxPooling1D(pool_length=2))

        model.add(Conv1D(
            input_shape=inputShape,
            nb_filter=64,
            filter_length=2,
            border_mode='valid',
            activation='relu',
            subsample_length=1
        ))
        model.add(MaxPooling1D(pool_length=2))

        model.add(Dropout(0.25))
        model.add(Flatten())

        model.add(Dense(250))
        model.add(Dropout(0.25))
        model.add(Activation('relu'))

        model.Dense(1)
        model.add(Activation('linear'))

        return model