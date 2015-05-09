plot1 <- function() {
    plot(x, y, col = "blue", pch = 19, cex = 2)
    text(x + 0.05, y + 0.05, labels = as.character(1:12))
}

plot2 <- function() {
    par(mar = rep(0.2, 4))
    plot(x, y, col = kmeansObj$cluster, pch = 19, cex = 2)
    points(kmeansObj$centers, col = 1:3, pch = 3, cex = 3, lwd = 3)
}

heatmap <- function() {
    par(mfrow = c(1, 2), mar = c(2, 4, 0.1, 0.1))
    image(t(dataMatrix)[, nrow(dataMatrix):1], yaxt = "n")
    image(t(dataMatrix)[, order(kmeansObj$cluster)], yaxt = "n")
}


set.seed(1234)
par(mar = c(0, 0, 0, 0))
x <- rnorm(12, mean = rep(1:3, each = 4), sd = 0.2)
y <- rnorm(12, mean = rep(c(1, 2, 1), each = 4), sd = 0.2)

plot1()
png(filename = "./pics/k1-plot1.png", width = 480, height = 480, units = "px")
plot1()
dev.off()

dataFrame <- data.frame(x, y)
kmeansObj <- kmeans(dataFrame, centers = 3)
print(names(kmeansObj))
print(kmeansObj$cluster)
print(kmeansObj$centers)

plot2()
png(filename = "./pics/k1-plot1-centroids.png", width = 480, height = 480, units = "px")
plot2()
dev.off()


## HEATMAP
set.seed(1234)
dataMatrix <- as.matrix(dataFrame)[sample(1:12), ]
kmeansObj2 <- kmeans(dataMatrix, centers = 3)

heatmap()
png(filename = "./pics/k1-heatmap.png", width = 480, height = 480, units = "px")
heatmap()
dev.off()

