
my_png <- function(filename, width = 480, height = 480, units = "px") {
    png(filename = filename, width = width, height = height, units = units)
}


set.seed(12345)
par(mar = rep(0.2, 4))
dataMatrix <- matrix(rnorm(400), nrow = 40)
image(1:10, 1:40, t(dataMatrix)[, nrow(dataMatrix):1])



my_png(filename = "./pics/pca_1.png")
image(1:10, 1:40, t(dataMatrix)[, nrow(dataMatrix):1])
dev.off()

par(mar = rep(0.2, 4))
heatmap(dataMatrix)

my_png(filename = "./pics/pca_2-heatmap-1.png")
par(mar = rep(0.2, 4))
heatmap(dataMatrix)
dev.off()

### ADD PATTERN
set.seed(678910)
for(i in 1:40) {
    # flip a coin
    coinFlip <- rbinom(1, size = 1, prob = 0.5)
    
    # if coin is heads add a common pattern to that row
    if(coinFlip) {
        dataMatrix[i, ] <- dataMatrix[i, ] + rep(c(0, 3), each = 5)
    }
}

par(mar = rep(0.2, 4))
image(1:10, 1:40, t(dataMatrix)[, nrow(dataMatrix):1])

my_png(filename = "./pics/pca_3_modified_sample.png")
par(mar = rep(0.2, 4))
image(1:10, 1:40, t(dataMatrix)[, nrow(dataMatrix):1])
dev.off()


par(mar = rep(0.2, 4))
heatmap(dataMatrix)

my_png(filename = "./pics/pca_4_modified_dendrogram.png")
par(mar = rep(0.2, 4))
heatmap(dataMatrix)
dev.off()

## PLOTS PATTERNS

plots_patterns <- function() {
    par(mfrow = c(1, 3), mar = c(3, 3, 3, 3))
    image(t(dataMatrixOrdered)[, nrow(dataMatrixOrdered):1])
    plot(rowMeans(dataMatrixOrdered), 40:1, , xlab = "Row Mean", ylab = "Row", pch = 19)
    plot(colMeans(dataMatrixOrdered), xlab = "Column", ylab = "Column Mean", pch = 19)
}

hh <- hclust(dist(dataMatrix))
dataMatrixOrdered <- dataMatrix[hh$order, ]
plots_patterns()

my_png(filename = "./pics/pca_5_patterns_in_rows_cols.png")
plots_patterns()
dev.off()

## SVD UV

svd_uv_plots <- function() {
    image(t(dataMatrixOrdered)[, nrow(dataMatrixOrdered):1])
    plot(svd1$u[, 1], 40:1, , xlab = "Row",  ylab = "First left singular vector", pch = 19)
    plot(svd1$v[, 1], xlab = "Column", ylab = "First right singular vector", pch = 19)
}

svd1 <- svd(scale(dataMatrixOrdered))
svd_uv_plots()

my_png(filename = "./pics/pca_6_svd_u_v.png")
svd_uv_plots()
dev.off()

## SVD VARIANCE
svd_variance_plots <- function() {
    par(mfrow = c(1, 2))
    plot(svd1$d, xlab = "Column", ylab = "Singular value", pch = 19)
    plot(svd1$d^2/sum(svd1$d^2), xlab = "Column", ylab = "Prop. of variance explained", pch = 19)
}

svd_variance_plots()

my_png(filename = "./pics/pca_7_svd_variance.png")
svd_variance_plots()
dev.off()

## SVD vs PCA 
svd_pca_comparison_plot <- function() {
    plot(pca1$rotation[,1], svd1$v[,1], pch = 19, xlab = "Principal Component 1",  ylab = "Right Singular Vector 1")
    abline(c(0, 1))
}

svd1 <- svd(scale(dataMatrixOrdered))
pca1 <- prcomp(dataMatrixOrdered, scale = T)
svd_pca_comparison_plot()

my_png(filename = "./pics/pca_8_svd_pca_comparison.png")
svd_pca_comparison_plot()
dev.off()

## VARIANCE EXPLAINED
variance_explained_plot <- function() {
    par(mfrow = c(1, 3))
    image(t(constantMatrix)[, nrow(constantMatrix):1])
    plot(svd1$d, xlab = "Column", ylab = "Singular value", pch = 19)
    plot(svd1$d^2/sum(svd1$d^2), xlab = "Column", ylab = "Prop. of variance explained", pch = 19)
}

constantMatrix <- dataMatrixOrdered * 0
for(i in 1:dim(dataMatrixOrdered)[1]) {
    constantMatrix[i, ] <- rep(c(0, 1), each = 5)
}
svd1 <- svd(constantMatrix)

variance_explained_plot()

my_png(filename = "./pics/pca_9_variance_explained.png")
variance_explained_plot()
dev.off()

## SECOND PATTERN TO ADD
svd_true_pattern_plots <- function() {
    par(mfrow = c(1, 3))
    image(t(dataMatrixOrdered)[, nrow(dataMatrixOrdered):1])
    plot(rep(c(0, 1), each = 5, pch = 19, xlab = "Column", ylab = "Pattern 1"))
    plot(rep(c(0, 1), 5), pch = 19, xlab = "Column", ylab = "Pattern 2")
}

set.seed(678910)
for ( i in 1:40) {
    # flip a coin
    coinFlip1 <- rbinom(1, size = 1, prob = 0.5)
    coinFlip2 <- rbinom(1, size = 1, prob = 0.5)
    
    # if coin is heads add a common pattern to that row
    if(coinFlip1) {
        dataMatrix[i, ] <- dataMatrix[i, ] + rep(c(0, 5), each = 5)
    }
    if(coinFlip2) {
        dataMatrix[i, ] <- dataMatrix[i, ] + rep(c(0, 5), 5)
    }
}

hh <- hclust(dist(dataMatrix))
dataMatrixOrdered <- dataMatrix[hh$order, ]
svd2 <- svd(scale(dataMatrixOrdered))

svd_true_pattern_plots()

my_png(filename = "./pics/pca_10_svd_true_patterns.png")
svd_true_pattern_plots()
dev.off()


## V AND PATTERNS OF VARIANCE

v_and_patterns_of_variance_plot <- function() {
    par(mfrow = c(1, 3))
    image(t(dataMatrixOrdered)[, nrow(dataMatrixOrdered):1])
    plot(svd2$v[, 1], pch = 19, xlab = "Column", ylab = "First right singular vector")
    plot(svd2$v[, 2], pch = 19, xlab = "Column", ylab = "Second right singular vector")
}

v_and_patterns_of_variance_plot()

my_png(filename = "./pics/pca_11_v_patterns_of_variabce.png")
v_and_patterns_of_variance_plot()
dev.off()

## D AND VARIANCE EXPLAINED

d_and_variance_plot <- function() {
    par(mfrow = c(1, 2))
    plot(svd1$d, xlab = "Column", ylab = "Singular value", pch = 19)
    plot(svd1$d^2/sum(svd1$d^2), xlab = "Column", ylab = "Percent of variance explained", pch = 19)
}
svd1 <- svd(scale(dataMatrixOrdered))

d_and_variance_plot()

my_png(filename = "./pics/pca_12_d_and_variance.png")
d_and_variance_plot()
dev.off()

