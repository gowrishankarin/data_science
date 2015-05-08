# Function to plot histogram for Global Active Power
plot1 <- function() {
     
    with(data, hist(Global_active_power, col="red", 
        xlab = "Global Active Power (kilowatts)", main = "Global Active Power"))
}

# Get the cached data laoded through load.R
data <- cacheHPCData(pFunc)

# Draw once on the current device for visual feedback then plot in the png device
plot1()
png(file="plot1.png", width=480, height=480, units="px")
plot1()
dev.off()