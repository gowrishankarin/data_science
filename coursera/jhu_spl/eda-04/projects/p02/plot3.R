
# Assuming data is not available for years 2000, 2001, 2003, 2004,2006 and 2007
# This analysis is done for years 1999, 2002, 2005, 2008


library(plyr)
library(reshape2)
library(ggplot2)

baltimore_data <- filter(NEI, fips == "24510" & (year == 1999 | year == 2002 | year == 2005 | year == 2008))

new_data <- ddply(
    baltimore_data, 
    .(type, year), 
    function(x) { 
        sum(x$Emissions) 
    }
)
p <- qplot(
    year, V1, data = new_data, 
    geom=c("point", "smooth"), method = "loess",
    formula=y~x, color=type, size=2,
    xlab = "Years 1999-2000",
    ylab = "PM2.5 Emission in Tons",
    main = "Baltimore Emission Trend of 4 Sources(point, nonpoint, onroad, nonroad)"
) 

png(filename = "./pics/plot3.png", width=640, height=640, units="px")
print(p)
dev.off()


    
