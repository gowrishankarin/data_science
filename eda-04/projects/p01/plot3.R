
data <- cacheHPCData(pFunc)

with(data, plot(DateTime, Sub_metering_1, type="l", ylab = "Energy sub metering"))

    
with(data, lines(DateTime, Sub_metering_2, type="l", col="red"))
with(data, lines(DateTime, Sub_metering_3, type="l", col="blue"))

legend("topright")
