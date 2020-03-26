housing <- function() {
    housing <- read.csv("./data/housing.csv")
    houseS <- housing[which(housing$ACR > 2 & housing$AGS > 5),]
    houseS[,c("ACR", "AGS")]
}

