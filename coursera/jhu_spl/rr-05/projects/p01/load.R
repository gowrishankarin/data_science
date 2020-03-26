# This file is crafted focusing optimization of reading data and
# reshaping/tidying to most constructive ones

# INPUT <- NONE
# OUTPUT <- A List Object holding functions to operate on the household power 
# consumption data to retrieve and store.
makeActivityData <- function() {
    data <- NULL
    setData <- function(new_data) data <<- new_data
    getData <- function() data
    list(setData = setData, getData = getData)
    
}

# INPUT <- A function pointer to makeActivityDate method.
# OUTPUT <- Tidied data of table data frame(tbl_df) for further processing.
cacheActivityData <- function(x, ...) {
    data <- x$getData()
    if(!is.null(data)) {
        message("Getting cached data")
        return(data)
    }
    
    new_data <- load()
    x$setData(new_data)
    return(new_data)
}

# INPUT <- File location of Activity data
# OUTPUT <- Filtered/Tidied data of table data frame(tbl_df) for further 
# processing.
load <- function(file = "activity.csv") {
    # Load required libraries
    library(data.table)
    library(dplyr)
    library(lubridate)
    
    # Chain it, Cache It
    # Read data file and account not available entries as "?" with column 
    # separator ';'
    data <- read.table(file, header=T, sep=',', na.strings="NA", 
                       stringsAsFactors = FALSE)
    # Convert the data to table data and remove from the memory
    new_data <- tbl_df(data)
    rm(data)
    
    
    # Mutate so that the format of Date and Time(POSIXct) column is no longer a string
    new_data <- mutate(new_data, date = as.Date(date, format="%Y-%m-%d"))
    
    return(new_data)
}

# cacheActivityData and function pointer to access data list object are in global space.
pFunc <- makeActivityData()
cacheActivityData(pFunc)
