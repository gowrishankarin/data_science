from keras.models import Sequential
from keras.layers.recurrent import LSTM
from keras.layers.core import Dense, Activation

class HNetLSTM2StackReggression():

    @staticmethod
    def build():
        model = Sequential()
        model.add(LSTM(
            input_shape=inputShape,
            input_dim=inputShape[0],
            output_dim=HIDDEN_RNN,
            return_sequences==True
        ))

        model.add(LSTM(
            input_shape=inputShape,
            input_dim=inputShape[0],
            output_dim=HIDDEN_RNN,
            return_sequences==True
        ))

        model.add(Dense(1))
        model.add(Activation('linear'))

        return model

