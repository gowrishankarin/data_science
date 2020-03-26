import numpy as np

class Classification():
    def __init__(self, multivariate=False):
        self.multivariate = multivariate
        self.X = []
        self.y = []
        
    def preprocessor_multi(self, data, WINDOW, STEP, FORECAST):
        openp = data.loc[:, 'Open'].tolist()
        highp = data.loc[:, 'High'].tolist()
        lowp = data.loc[:, 'Low'].tolist()
        closep = data.loc[:, 'Adj Close'].tolist()
        volumep = data.loc[:, 'Volume'].tolist()
        
        for i in range(0, len(data), STEP):
            try:
                o = openp[i: i + WINDOW]
                h = highp[i: i + WINDOW]
                l = lowp[i: i + WINDOW]
                c = closep[i: i + WINDOW]
                v = volumep[i: i+ WINDOW]

                o = (np.array(o) - np.mean(o)) / np.std(o)
                h = (np.array(h) - np.mean(h)) / np.std(h)
                l = (np.array(l) - np.mean(l)) / np.std(l)
                c = (np.array(c) - np.mean(c)) / np.std(c)
                v = (np.array(v) - np.mean(v)) / np.std(v)

                x_i = closep[i: i + WINDOW]
                y_i = closep[i + WINDOW + FORECAST]

                last_close = x_i[-1]
                next_close = y_i

                if last_close < next_close:
                    y_i = [1, 0]
                else:
                    y_i = [0, 1]

                x_i = np.column_stack((o, h, l, c, v))
            except Exception as e:
                print(str(e))
                break
            
            self.X.append(x_i)
            self.y.append(y_i)
            
    def preprocessor_uni(self, data, WINDOW, STEP, FORECAST):
        return
        
    def preprocess(self, data, WINDOW, STEP, FORECAST):
        if(self.multivariate == True):
            self.preprocessor_multi(data, WINDOW, STEP, FORECAST)
        else:
            self.preprocessor_uni(data, WINDOW, STEP, FORECAST)
            
        return np.array(self.X), np.array(self.y)