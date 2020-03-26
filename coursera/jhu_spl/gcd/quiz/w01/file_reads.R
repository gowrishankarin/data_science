# Q1
q1 <- function() {
    housing <- fread("./data/housing.csv")
    housing[, .N, by="VAL"]
}


q4 <- function() {
    doc <- xmlTreeParse("./data/restaurant.xml", useInternal=T)
    zips <- xpathSApply(doc, "//zipcode", xmlValue)
    count <- 0
    for(i in 1:length(zips)) {
        if(zips[[i]] == "21231")
            count <- count + 1
    }
    
    count
}


perfmon <- function(DT) {
    
    
    a <- system.time(sapply(split(DT$pwgtp15, DT$SEX), mean))
    print(a)
    b1 <- system.time(mean(DT[DT$SEX==1,]$pwgtp15))
    print(b1)
    b2 <- system.time(mean(DT[DT$SEX==2,]$pwgtp15))
    print(b2)
    d <- system.time(DT[,mean(pwgtp15),by=SEX])
    print(d)
    e <- system.time(mean(DT$pwgtp15,by=DT$SEX))
    print(e)
    f <- system.time(tapply(DT$pwgtp15,DT$SEX,mean))
    print(f)
    
   

}