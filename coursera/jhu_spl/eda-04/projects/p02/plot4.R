new_scc <- SCC[grep("Coal*", SCC$EI.Sector),]

new_nei <- subset(NEI, SCC %in% new_scc$SCC)

new_nei <- filter(new_nei, year == 1999 | year == 2002 | year == 2005 | year == 2008)

new_data <- ddply(
    new_nei, 
    .(type, year), 
    function(x) { 
        sum(x$Emissions) 
    }
)
str(new_data)
p <- qplot(
    year, V1, data = new_data, 
    geom=c("point", "smooth"), method = "loess",
    formula=y~x, color=type, size=2,
    xlab = "Years 1999-2000",
    ylab = "PM2.5 Emission in Tons",
    main = "US Emission Trend (Coal Combustion Related Sources)"
) 

print(p)

png(filename = "./pics/plot4.png", width=640, height=640, units="px")
print(p)
dev.off()

return(new_data)