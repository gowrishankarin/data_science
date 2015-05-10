
# Assuming data is not available for years 2000, 2001, 2003, 2004,2006 and 2007
# This analysis is done for years 1999, 2002, 2005, 2008

emission <- c(
    sum(filter(NEI, fips == "24510" & year == 1999)$Emissions),  
    sum(filter(NEI, fips == "24510" & year == 2002)$Emissions),    
    sum(filter(NEI, fips == "24510" & year == 2005)$Emissions),    
    sum(filter(NEI, fips == "24510" & year == 2008)$Emissions)        
)

baltimore_data <- filter(NEI, fips == "24510")