plot1 <- function() {
    par(mar = c(5, 5, 2, 2))
    plot(Years, emission, type = "l", ylab = "Total PM2.5 Emission in Million Tons", xlab = "Year", pch = 19)
    text(Years + 0.005, emission + 0.0005, labels = as.character(round(emission, digits = 1)))
}

emission = c(
    sum(filter(NEI, year == 1999 )$Emissions), 
    sum(filter(NEI, year == 2002 )$Emissions),
    sum(filter(NEI, year == 2005 )$Emissions), 
    sum(filter(NEI, year == 2008 )$Emissions)
)/10^6
Years = c(1999, 2002, 2005, 2008)

plot1()

png(filename = "./pics/plot1.png", width = 480, height = 480, units = "px")
plot1()
dev.off()