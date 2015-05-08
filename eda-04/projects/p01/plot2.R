# Line plot of Global active power from mid night of Thursday to mid-night of Saturday
data <- cacheHPCData(pFunc)
with(data, plot(DateTime, Global_active_power, type="l", ylab = "Global Active Power (kilowatts)"))
