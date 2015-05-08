# Line plot of Global active power from mid night of Thursday to mid-night of Saturday

plot2 <- function(ylab = "Global Active Power (kilowatts)" ) {
    with(data, plot(DateTime, Global_active_power, type="l", ylab = ylab))
}


# Get the cached data laoded through load.R
data <- cacheHPCData(pFunc)

# Draw once on the current device for visual feedback then plot in the png device
plot2()
png(file="plot2.png", width=480, height=480, units="px")
plot2()
dev.off()
