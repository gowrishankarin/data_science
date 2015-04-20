read_dataset <- function(directory = "./UCI HAR Dataset") {

    
    # Read X Training and Test data set
	x_train <- read.table(paste(directory,"train/X_train.txt", sep="/"))
	x_test <- read.table(paste(directory,"test/X_test.txt", sep="/"))
    
    # Append them by rows.
    x <- rbind(x_train, x_test)
    
	
	# Read Y training and test data set
	y_train <- read.table(paste(directory, "train/Y_train.txt", sep="/"))
	y_test <- read.table(paste(directory,"test/y_test.txt", sep="/"))
    
    # Append them by rows
	y <- rbind(y_train, y_test)
	
	subject_train <- read.table(paste(directory, "train/subject_train.txt", sep="/"))
	subject_test <- read.table(paste(directory, "test/subject_test.txt", sep="/"))
	
    # Append them by rows
	subject <- rbind(subject_train, subject_test)
    
    main_data = cbind(x, y, subject)
	
	
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