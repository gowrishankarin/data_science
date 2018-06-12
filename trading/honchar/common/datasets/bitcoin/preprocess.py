import numpy as np
import pandas as pd

class BitCoinPreprocess():

    def __init__(self):
        self.X = []
        self.y = []

    def preprocess(self, data, WINDOW, STEP, FORECAST):

        openp = data.loc[:, 'Open'].tolist()
        highp = data.loc[:, 'High'].tolist()
        lowp = data.loc[:, 'Low'].tolist()
        closep = data.loc[:, 'Close'].tolist()
        volumep = data.loc[:, 'Volume_(BTC)'].tolist()
        volumecp = data.loc[:, 'Volume_(Currency)'].tolist()

        volatility = pd.DataFrame(closep).rolling(WINDOW).std().values.tolist()
        volatility = [v[0] for v in volatility]

        for i in range(0, len(data), STEP):
            try:
                o = openp[i: i + WINDOW]
                h = highp[i: i + WINDOW]
                l = lowp[i: i + WINDOW]
                c = closep[i: i + WINDOW]
                v = volumep[i: i + WINDOW]
                vc = volumecp[i: i + WINDOW]
                volat = volatility[i:i+WINDOW]

                o = (np.array(o) - np.mean(o)) / np.std(o)
                h = (np.array(h) - np.mean(h)) / np.std(h)
                l = (np.array(l) - np.mean(l)) / np.std(l)
                c = (np.array(c) - np.mean(c)) / np.std(c)
                v = (np.array(v) - np.mean(v)) / np.std(v)
                vc = (np.array(vc) - np.mean(vc)) / np.std(vc)
                volat = (np.array(volat) - np.mean(volat)) / np.std(volat)


                x_i = closep[i: i + WINDOW]
                y_i = closep[i + WINDOW + FORECAST]

                x_i = np.column_stack((o, h, l, c, v, vc, volat))
                x_i = x_i.flatten()

                y_i = (closep[i+WINDOW+FORECAST] - closep[i+WINDOW]) / closep[i+WINDOW]

                if(np.isnan(x_i).any()):
                    continue

            except Exception as e:
                print(str(e))
                break
            
            self.X.append(x_i)
            self.y.append(y_i)

        return np.array(self.X), np.array(self.y)
