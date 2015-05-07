
plot_2 <- function(data) {
    with(data, plot(Time, Global_active_power, type="l", ylab = "Global Active Power (kilowatts)"))
}