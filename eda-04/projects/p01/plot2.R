# Line plot of Global active power from mid night of Thursday to mid-night of Saturday

plot2 <- function(ylab = "Global Active Power (kilowatts)" ) {
    data <- cacheHPCData(pFunc)
    with(data, plot(DateTime, Global_active_power, type="l", ylab = ylab))
}

plot2()
dev.copy(png, file="plot2.png", width=480, height=480, units="px")
dev.off()