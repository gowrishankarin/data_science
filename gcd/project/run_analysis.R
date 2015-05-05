# INPUT <- None
# OUTPUT <- Average of mean and standard deviation for a subject according to activity.
# Description <- Loads the UCI HAR Dataset from the local folder, merge them, extract
# the relevant cols and tidy them.
main <- function() {

    x_data <- load()
    merged_data <- read_dataset(x_data)
    extracted_data <- extract(merged_data)

    tidy_data <- tidy_dataset(extracted_data)
    
    tidy_data
}

# INPUT <- UCI HAR Dataset location(optional)
# OUTPUT <- Merged X train and test data set.
# Loads required libraries, X test and train data.
load <- function(directory = "./UCI HAR Dataset") {
    library(data.table)
    library(plyr)
    library(dplyr)
    
    
    # Read X Training and Test data set
    features <- read.table(paste(directory, "features.txt", sep="/"))
    features[,2] <- gsub("-", "_", features[,2])
    features[,2] <- gsub("\\()", "", features[,2])
    
    x_train <- read.table(paste(directory,"train/X_train.txt", sep="/"))
    colnames(x_train) <- features[,2]
    x_train$type <- "train"
    
    x_test <- read.table(paste(directory,"test/X_test.txt", sep="/"))
    colnames(x_test) <- features[,2]
    x_test$type <- "test"
    
    
    # Append them by rows.
    x <- rbind(x_train, x_test)    

    x
}

# INPUT <- Merged X train and test dataset
# OUTPUT <- Merged data of activities, subject and X
# Description <- Merge X, activity and subject info of test and train data.
read_dataset <- function(x, directory = "./UCI HAR Dataset") {
    
    
    print("Reading y training data...")
    # Read Y training and test data set
    y_train <- read.table(paste(directory, "train/Y_train.txt", sep="/"))
    y_test <- read.table(paste(directory,"test/y_test.txt", sep="/"))
    
    # Append them by rows
    y <- rbind(y_train, y_test)
    colnames(y) <- "y"
    
    print("Reading subject training data...")
    
    subject_train <- read.table(paste(directory, "train/subject_train.txt", sep="/"))
    subject_test <- read.table(paste(directory, "test/subject_test.txt", sep="/"))
    
    # Append them by rows
    subject <- rbind(subject_train, subject_test)
    colnames(subject) <- "subject"
    
    merged_data <- x
    merged_data$subject <- subject[,1]
    merged_data$activity <- y[,1]
    
    merged_data
    
}

# INPUT <- Merged Data Set
# OUTPUT <- Extracted columns of Mean and Standard Deviation
extract <- function(merged_data, directory="./UCI HAR Dataset") {
    
    # Identify the columns of "mean" and "sd"
    # Read features.txt and search for columns having mean and sd
    #angles <- grep(*angle)
    
    extracted_data <- merged_data[,grep("([m]ean()|[s]td())", colnames(merged_data))]
    # add subject and activity
    
    extracted_data$activity <- merged_data$activity
    extracted_data$subject <- merged_data$subject
    
    extracted_data <- tbl_df(extracted_data)
    
    extracted_data
    
}

# INPUT <- Extracted Data Set
# OUTPUT <- Tidy data set grouped by Subject and Activity
# Description <- Creates output dataset file named tidy_data.txt in the local directory
tidy_dataset <- function(extracted_data) {
    
    tidy_data <- ddply(extracted_data, .(subject, activity), function(x) colMeans(x[,1:79]))

    write.table(tidy_data, "./tidy_data.txt", row.name=FALSE)
    
    tbl_tidy_data <- tbl_df(tidy_data)

    tbl_tidy_data
    
}

# TEST FUNCTION
main2 <- function (x_data) {
    merged_data <- read_dataset(x_data)
    extracted_data <- extract(merged_data)
    tidy_data <- tidy_dataset(extracted_data)
    
    tidy_data
}

# Function to load Inertial data, NOT USED
read_inertial_data <- function(directory) {
    rel_path_signals <- paste(directory, "train", "Inertial Signals", sep="/")
    rel_path_signals_t <- paste(directory, "test", "Inertial Signals", sep="/")
    signal_files <- list.files(rel_path_signals)
    signal_files_t <- list.files(rel_path_signals)
    
    data <- array(dim=9)
    for ( i in 1:length(signal_files)) {
        file_name = paste(rel_path_signals, signal_files[i], sep="/")
        file_name_t = paste(rel_path_signals, signal_files_t[i], sep="/")
        
        
        field <- strsplit(file_name, "[.]")
        train <- read.table(file_name)
        test <- read.table(file_name_t)
        
        #print(paste(file_name, file_name_t, dim(train), dim(test), ":"))
        data[i] <- rbind(train, test)
        
    }
    
    
    data
    
}