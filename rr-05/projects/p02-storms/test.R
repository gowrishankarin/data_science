library(data.table)
library(dplyr)
library(lubridate)
library(plyr)
library(reshape2)
library(ggplot2)

if (!(exists("storm_data"))) {
    print("Storm Data Loading...")
    if (!(exists("csv_data"))) {
        csv_data <- read.csv("StormData.csv", sep = ",", stringsAsFactors = F)
    }
    storm_data <- tbl_df(csv_data)
    rm(csv_data)
}

calcNetFatalitiesByEvent <- function(data) {
    fatalitiesByEvent <- ddply(
        storm_data, 
        .(EVTYPE), 
        function(x) {  
            sum(x$FATALITIES, na.rm = T)
        }
    )
    return(fatalitiesByEvent[order(-fatalitiesByEvent$V1), ])
}
netFatalities <- calcNetFatalitiesByEvent(storm_data)

calcNetInjuriesByEvent <- function(data) {
    injuriesByEvent <- ddply(
        storm_data, 
        .(EVTYPE), 
        function(x) {  
            sum(x$INJURIES, na.rm = T)
        }
    )
    return(injuriesByEvent[order(-injuriesByEvent$V1), ])
}
netInjuries <- calcNetInjuriesByEvent(storm_data)

tmpData1 <- netFatalities[1:5, ]

p <- qplot(
    EVTYPE, V1, stat="identity", data = tmpData1, geom = "bar",
    xlab = "Event Type",
    ylab = "No of Deaths",
    main = "Net Fatalities of Top 5 Events",
    fill = factor(EVTYPE)
) 
print(p)

tmpData2 <- netInjuries[1:5, ]

q <- qplot(EVTYPE, V1, stat="identity", data = tmpData2, geom = "bar",
    xlab = "Event Type",
    ylab = "No of Injuries",
    main = "Net Injuries of Top 5 Events",
    fill = factor(EVTYPE)
)
print(q)

calcNetCropDamage <- function(data) {
    cropDamageByEvent <- ddply(
        storm_data, 
        .(EVTYPE), 
        function(x) {  
            sum(x$CROPDMG, na.rm = T)
        }
    )
    return(cropDamageByEvent[order(-cropDamageByEvent$V1), ])
}

cropDamage <- calcNetCropDamage(storm_data)

calcNetPropertyDamage <- function(data) {
    propertyDamageByEvent <- ddply(
        storm_data, 
        .(EVTYPE), 
        function(x) {  
            sum(x$PROPDMG, na.rm = T)
        }
    )
    return(propertyDamageByEvent[order(-propertyDamageByEvent$V1), ])
}

cropDamage <- calcNetPropertyDamage(storm_data)
print(head(cropDamage))

propertyDamage <- calcNetPropertyDamage(storm_data)
print(head(propertyDamage))
