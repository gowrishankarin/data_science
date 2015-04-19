housing <- function() {
    housing <- read.csv("./data/idaho.csv")
    houseS <- housing[which(housing$ACR > 2 & housing$AGS > 5),]
    head(houseS[,c("ACR", "AGS")], n=3)
}

gdp <- function() {
    gdp <- read.csv("./data/gdp.csv", skip=4)
    edu <- read.csv("./data/edu.csv")
    
    gdp <- rename(gdp, replace=c("X" = "CC", "X.1"="Rank", "X.3"="Name", "X.4"="GDP"))
    
    gdpC <- gdp[1:190,]
    
    # Merged Data
    mD <- merge(gdpC, edu, by.x="CC", by.y="CountryCode", all=F)
    
    mD <- mD[,c("CC", "Rank", "GDP", "Short.Name", "Income.Group")]
    xn <- as.numeric(gsub(",", "", mD$GDP))
    mD$GDPn <- xn
    mD[order(mD$GDPn, decreasing=F),]
}

oecd <- function() {
    library(plyr)
    gdp <- read.csv("./data/gdp.csv", skip=4, blank.lines.skip = TRUE)
    edu <- read.csv("./data/edu.csv")
    
    gdp <- rename(gdp, replace=c("X" = "CC", "X.1"="Rank", "X.3"="Name", "X.4"="GDP"))
    gdpC <- gdp[1:190,]
    
    # Merged Data
    mD <- merge(gdpC, edu, by.x="CC", by.y="CountryCode", all=F)
    
    xn <- as.numeric(gsub(",", "", mD$GDP))
    mD$GDPn <- xn
    
    y <- split(mD, mD$Income.Group)
    
    
    
    
    
    
    
    mD
}