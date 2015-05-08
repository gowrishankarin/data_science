# Draws 4 plots in a 2x2 grid. Reuses the code written in plot2.R and plot3.R files
# 

data <- cacheHPCData(pFunc)

par(mfrow = c(2,2))

with(data, {
    plot2(ylab = "Global Active Power")
    plot(DateTime, Voltage, xlab = "datetime", ylab = "Voltage", type = "l")
    plot3(box.lwd = 0)
    plot(DateTime, Global_reactive_power, xlab = "datetime", type = "l")
    
})

dev.copy(png, file="plot4.png", width=480, height=480, units="px")
dev.off()
#reset the grid to 1x1
par(mfrow = c(1,1))