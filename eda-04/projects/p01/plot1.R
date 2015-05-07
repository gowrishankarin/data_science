

# Function to plot histogram for Global Active Power
plot_histogram <- function(data) {
    with(data, hist(Global_active_power, col="red", 
                    xlab = "Global Active Power (kilowatts)", 
                    main = "Global Active Power"))
}