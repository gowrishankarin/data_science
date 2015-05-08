
plot3 <- function(box.lwd = 3) {

    data <- cacheHPCData(pFunc)
    
    # Draw a line graph for DateTime and sub meter 1's utilization
    with(data, plot(DateTime, Sub_metering_1, type="l", xlab = "", ylab = "Energy sub metering"))
    
    # Add lines for sub meter 2 and 3
    with(data, lines(DateTime, Sub_metering_2, type="l", col="red"))
    with(data, lines(DateTime, Sub_metering_3, type="l", col="blue"))
    
    # Add a legend @ top right corner.
    legend("topright", lwd=1, lty=1, col = c("black", "blue", "red"), box.lwd = box.lwd,
        legend = c("Sub_metering_1", "Sub_metering_2", "Sub_metering_3"))

}

plot3()
dev.copy(png, file="plot3.png", width=480, height=480, units="px")
dev.off()