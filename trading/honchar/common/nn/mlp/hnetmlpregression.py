from keras.models import Sequential
from keras.layers.core import Activation, Flatten, Dropout, Dense

class HNetMLPRegression():
    @staticmethod
    def build(inputShape):
        model = Sequential()

        model.add(Dense(500, input_shape=inputShape))
        model.add(Activation('relu'))
        model.add(Dropout(0.25))
        model.add(Dense(250))
        model.add(Activation('relu'))
        model.add(Dense(1))
        model.add(Activation('linear'))

        return model