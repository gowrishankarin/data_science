# This file is crafted focusing optimization of reading data and
# reshaping/tidying to most constructive ones

# INPUT <- NONE
# OUTPUT <- A List Object holding functions to operate on the household power 
# consumption data to retrieve and store.
makeHPCData <- function() {
    data <- NULL
    setData <- function(new_data) data <<- new_data
    getData <- function() data
    list(setData = setData, getData = getData)
    
}

# INPUT <- A function pointer to makeHPCDate method.
# OUTPUT <- Tidied data of table data frame(tbl_df) for further processing.
cacheHPCData <- function(x, ...) {
    data <- x$getData()
    if(!is.null(data)) {
        message("Getting cached data")
        return(data)
    }
    
    new_data <- load()
    x$setData(new_data)
    return(new_data)
}

# INPUT <- File location of HPC data
# OUTPUT <- Filtered/Tidied data of table data frame(tbl_df) for further 
# processing.
load <- function(file = "household_power_consumption.txt") {
    # Load required libraries
    library(data.table)
    library(dplyr)
    library(lubridate)
    
    # Chain it, Cache It
    # Read data file and account not available entries as "?" with column 
    # separator ';'
    data <- read.table(file, header=T, sep=';', na.strings="?", 
        stringsAsFactors = FALSE)
    # Convert the data to table data and remove from the memory
    new_data <- tbl_df(data)
    rm(data)

    new_data <- mutate(new_data, DateTime = paste(Date, Time, sep = " "))
    
    # Mutate so that the format of Date and Time(POSIXct) column is no longer a string
    new_data <- mutate(new_data, Date = as.Date(Date, format="%d/%m/%Y"), 
        DateTime = fast_strptime(DateTime, format="%d/%m/%Y %H:%M:%S"))
    
    # Acquire meter data for specific dates
    new_data <- filter(new_data, Date == as.Date("2007-02-01") | 
        Date == as.Date("2007-02-02"))    
    

    return(new_data)
}

# cacheHPCData and function pointer to access data list object are in global space.
pFunc <- makeHPCData()
cacheHPCData(pFunc)
