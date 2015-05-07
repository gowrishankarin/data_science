load <- function() {
    library(data.table)
    library(dplyr)
    
    # Chain it, Cache It

    data <- read.table("household_power_consumption.txt", header=T, sep=';', 
        na.strings="?", stringsAsFactors = FALSE)
    new_data <- tbl_df(data)
    rm(data)
    
    new_data <- mutate(new_data, Date = as.Date(Date, format="%d/%m/%Y"))

    new_data <- filter(new_data, Date == as.Date("2007-02-01") | 
        Date == as.Date("2007-02-02"))    
    
    new_data

}