import numpy as np

class Perceptron:
    def __init__(self, N, alpha=0.1):
        # Initialize the weight matrix and store the learning rate
        self.W = np.random.randn(N + 1)/np.sqrt(N)
        self.alpha = alpha
        
    def step(self, x):
        # Apply the step function
        return 1 if x > 0 else 0
    
    def fit(self, X, y, epochs=10):
        # Insert a column of 1s as the last entry in the feature
        # matrix -- this little trick allows us to treat the bias
        # as a trainable parameter within the weight matrix
        X = np.c_[X, np.ones((X.shape[0]))]
        
        # Loop over the desired number of epochs
        for epoch in np.arange(0, epochs):
            # Loop over each individual data point
            for(x, target) in zip(X, y):
                # Take the dot product between the input features
                # and the weight matrix, then pass this value
                # through the step function to obtain the prediction
                p = self.step(np.dot(x, self.W))
                
                # Only perform the weight update, if our prediction 
                # does not match the target
                if p != target:
                    # Determine the error
                    error = p - target
                    
                    # Update the weight matrix
                    self.W += -self.alpha * error * x
                    
    def predict(self, X, addBias=True):
        # ensure our input is a matrix
        X = np.atleast_2d(X)
        
        # Check to see if the bias column should be added
        if addBias:
            # Insert a column of 1s as the last entry in
            # the feature matrix(bias)
            X = np.c_[X, np.ones((X.shape[0]))]
            
        # Take the dot product between the input features and the 
        # weight matrix, then pass the value through the step function
        return self.step(np.dot(X, self.W))