# Function to plot histogram for Global Active Power
data <- cacheHPCData(pFunc)

with(data, hist(Global_active_power, col="red", 
    xlab = "Global Active Power (kilowatts)", main = "Global Active Power"))
