new_scc <- SCC[grep("Mobile*", SCC$EI.Sector),]
new_nei <- subset(NEI, SCC %in% new_scc$SCC)

new_nei <- filter(new_nei, (fips == "24510" | fips == "06037") & (year == 1999 | year == 2002 | year == 2005 | year == 2008))

new_data <- ddply(
    new_nei, 
    .(fips, year), 
    function(x) { 
        sum(x$Emissions) 
    }
)
str(new_data)
p <- qplot(
    year, V1, data = new_data, 
    geom=c("point", "smooth"), method = "loess",
    formula=y~x, color=fips, size=2,
    xlab = "Years 1999-2000",
    ylab = "PM2.5 Emission in Tons",
    main = "Motor Vehicle Emission Baltimore(24510) City and Los Angeles(06037)"
) 

print(p)

png(filename = "./pics/plot6.png", width=640, height=640, units="px")
print(p)
dev.off()

return(new_data)