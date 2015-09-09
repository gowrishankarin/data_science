
# Francis Galton: Child vs Parent
library(UsingR)

galton_francis <- function() {
    data(galton)
    
    par(mfrow = c(1, 2))
    hist(galton$parent, col = "blue", breaks = 100)
    hist(galton$child, col = "blue", breaks = 100)
    
}

par(mfrow = c(1, 1))
# Manipulate to minimize 'mu'

library(manipulate)

myHist <- function(mu) {
    hist(galton$child, col = "blue", breaks = 100)
    lines(c(mu, mu), c(0, 150), col = "red", lwd = 5)
    mse <- mean((galton$child - mu)^2)
    text(63, 150, paste("mu = ", mu))
    text(63, 140, paste("MSE = ", round(mse, 2)))
    
}

#manipulate(myHist(mu), mu = slider(62, 74, step = 0.5))

minimizeMu <- function(mu) {
    # Consider the data set given below
    x <- c(0.18, -1.54, 0.42, 0.95)
    # and weights given by
    w <- c(2, 1, 3, 1)
    # Give the value of 'mu' that minimizes the least squares equation 
    # SUM(w*(x - mu)^2)
    
    hist(x, col = "blue", breaks = 100)
    lines(c(mu, mu), c(-2, 1), col = "red", lwd = 0.5)
    mse <- mean(w*(x - mu)^2)
    
    text(-1.0, 0.8, paste("mu = ", mu))
    text(-1.0, 0.6, paste("MSE = ", mse, 2))
}

#manipulate(minimizeMu(mu), mu = slider(0, 0.35, step = 0.01))

fitThruOrigin <- function(beta) {
    # Consider the following data set
    x <- c(0.8, 0.47, 0.51, 0.73, 0.36, 0.58, 0.57, 0.85, 0.44, 0.42)
    y <- c(1.39, 0.72, 1.55, 0.48, 1.19, -1.59, 1.23, -0.65, 1.49, 0.05)
    # Fit the regression through the origin and get the slope treating y as the
    # the outcome and x as the regressor. (Hint, do not center the data since 
    # we want regression through the origin, not through the means of the data)
    
    x0 <- x - mean(x)
    y0 <- y - mean(y)
    
    freqData <- as.data.frame(table(x0, y0))
    
    names(freqData) <- c("X_0", "Y_0")
    
    plot(
        as.numeric(as.vector(freqData$X_0)),
        as.numeric(as.vector(freqData$Y_0)),
        pch = 21, col = "black", bg = "lightblue",
        xlab = "X_0", ylab = "Y_0"
    )
    
    abline(0, beta)
    points(0, 0, cex = 2, pch = 19)
    
    mse <- mean((y - beta *x)^2)
    title(paste("beta = ", beta,  " mse = ", round(mse, 3)))

    
 #   plot(x - mean(x), y - mean(y), pch = 19, col = "blue")
    
}

# manipulate(fitThruOrigin(beta), beta = slider(-0.5, 1.5, step = 0.01))

fitMtCars <- function() {
    # Do "data(mtcars)" from the datasets package and fit the regression model 
    # with mpg as the outcome and weight as the predictor. Give the slope 
    # coefficient
    data(mtcars)
    lm(mpg ~ wt, data = mtcars)
}

predictor <- function() {
    # Consider the following data set (used above as well). What is the intercept
    # for fitting the model with x as the predictor and y as the outcome
    
    x <- c(0.8, 0.47, 0.51, 0.73, 0.36, 0.58, 0.57, 0.85, 044, 0.42)
    
    y <- c(1.39, 0.72, 1.55, 0.48, 1.19, -1.59, 1.23, -0.65, 1.49, 0.05)
    
    
    
    
    
    
}




