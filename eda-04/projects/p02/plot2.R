plot2 <- function() {
    par(mfrow = c(1, 2))
    plot(year, emission, type="l",  xlab = "Years", ylab = "PM2.5 Emission in Tons", 
         main = "Baltimore PM2.5 City Emission", sub = "1999-2008")
    text(years + 0.005, emission + 0.0005, labels = as.character(round(emission, digits = 1)))
    
    plot(new_years, new_emission, type="l", xlab = "Years", ylab = "PM2.5 Emission in Tons", 
         main = "Baltimore PM2.5 City Emission Trend", sub = "1999, 2002, 2005, 2008")
    text(new_years + 0.007, new_emission + 0.0005, labels = as.character(round(new_emission, digits = 1)))
    
}


emission <- c(
    sum(filter(NEI, fips == "24510" & year == 1999)$Emissions),  
    sum(filter(NEI, fips == "24510" & year == 2000)$Emissions),    
    sum(filter(NEI, fips == "24510" & year == 2001)$Emissions),    
    sum(filter(NEI, fips == "24510" & year == 2002)$Emissions),    
    sum(filter(NEI, fips == "24510" & year == 2003)$Emissions),    
    sum(filter(NEI, fips == "24510" & year == 2004)$Emissions),    
    sum(filter(NEI, fips == "24510" & year == 2005)$Emissions),    
    sum(filter(NEI, fips == "24510" & year == 2006)$Emissions),    
    sum(filter(NEI, fips == "24510" & year == 2007)$Emissions),    
    sum(filter(NEI, fips == "24510" & year == 2008)$Emissions)        
)

years <- 1999:2008

new_emission <- emission[emission != 0]

# We observed for years 2000, 2001, 2003, 2004, 2006, 2007 data is not available. Let us draw another plot 
# filtering those years
new_years <- c(1999, 2002, 2005, 2008)

plot2()

png(filename = "./pics/plot2.png", width = 720, height = 480, units = "px")
plot2()
dev.off()
