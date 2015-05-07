
plot_3 <- function(data) {
    with(data, plot(Time, Sub_metering_1, type="l", ylab = "Energy sub metering"))
    with(data, lines(Sub_metering_2, type="l", col="red"))
    with(data, lines(Sub_metering_3, type="l", col="blue"))
    
    legend("topright")
}