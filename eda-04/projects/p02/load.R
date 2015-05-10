# This file is crafted focusing optimization of reading data and
# reshaping/tidying to most constructive ones

# INPUT <- NONE
# OUTPUT <- A List Object holding functions to operate on the household power 
# consumption data to retrieve and store.
makeFPMData <- function() {
    dataNEI <- NULL
    dataSCC <- NULL
    setNEIData <- function(new_data) {
        dataNEI <<- new_data
    }
    getNEIData <- function() {
        return(dataNEI)
    }
    setSCCData <- function(new_data) {
        dataSCC <<- new_data
    }
    getSCCData <- function() {
        return(dataSCC)
    }
    
    list(setNEIData = setNEIData, getNEIData = getNEIData, setSCCData = setSCCData, getSCCData = getSCCData)
    
}

# INPUT <- A function pointer to makeHPCDate method.
# OUTPUT <- Tidied data of table data frame(tbl_df) for further processing.
cacheFPMData <- function(x, dataType,  ...) {
    SCC <- x$getSCCData()
    NEI <- x$getNEIData()
    if(!is.null(SCC)) {
        message("Getting cached data")
        if(dataType == "SCC") {
            return(SCC)
        } else {
            return(NEI)
        }
    }
    
    NEI <- load("summarySCC_PM25.rds")
    x$setNEIData(NEI)
    
    SCC <- load("Source_Classification_Code.rds")
    x$setSCCData(SCC)
    
    if(dataType == "SCC") {
        return(SCC)
    } else {
        return(NEI)
    }

}

# INPUT <- File location of HPC data
# OUTPUT <- Filtered/Tidied data of table data frame(tbl_df) for further 
# processing.
load <- function(filename) {
    # Load required libraries
    library(data.table)
    library(dplyr)
    library(lubridate)
    
    # Chain it, Cache It
    # Read data file and account not available entries as "?" with column 
    # separator ';'
    data <- readRDS(filename)
    # Convert the data to table data and remove from the memory
    new_data <- tbl_df(data)
    rm(data)
    
    return(new_data)
}

# cacheHPCData and function pointer to access data list object are in global space.

