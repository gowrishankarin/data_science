data <- read.table("household_power_consumption.txt", header=T, sep=';', na.strings="?")
new_data <- tbl_df(data)