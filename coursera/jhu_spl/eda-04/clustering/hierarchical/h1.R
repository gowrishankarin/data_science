plot1 <- function() {
    plot(x, y, col = "blue", pch = 19, cex = 2)
    text(x + 0.05, y + 0.05, labels = as.character(1:12))
}

### DATA CREATION

set.seed(1234)
par(mar = c(0, 0, 0, 0))
x <- rnorm(12, mean = rep(1:3, each = 4), sd = 0.2)
y <- rnorm(12, mean = rep(c(1, 2, 1), each = 4), sd = 0.2)

plot1()
png(filename = "./pics/h1-plot1.png", width = 480, height = 480, units = "px")
plot1()
dev.off()

# Calculate the distance.
dataFrame <- data.frame(x = x, y = y)
dist(dataFrame)

hClustering <- hclust(distxy)

## DENDROGRAM

plot(hClustering)
png(filename = "./pics/h1-dendrogram.png", width = 480, height = 480, units = "px")
plot(hClustering)
dev.off()

source("myplclust.R")
myplclust(hClustering, lab = rep(1:3, each = 4), lab.col = rep(1:3, each = 4))

## PRETTY DENDROGRAM

png(filename = "./pics/h1-dendrogram-cool.png", width = 480, height = 480, units = "px")
myplclust(hClustering, lab = rep(1:3, each = 4), lab.col = rep(1:3, each = 4))
dev.off()


## HEATMAP

set.seed(143)
dataMatrix <- as.matrix(dataFrame)[sample(1:12), ]
heatmap(dataMatrix)

png(filename = "./pics/h1-heatmap.png", width = 480, height = 480, units = "px")
heatmap(dataMatrix)
dev.off()




