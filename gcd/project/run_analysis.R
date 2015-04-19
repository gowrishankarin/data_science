read_dataset <- function(directory = "./UCI HAR Dataset") {

	x_train <- read.table(paste(directory,"train/X_train.txt", sep="/"))
	print(dim(x_train))

	y_train <- read.table(paste(directory, "train/Y_train.txt", sep="/"))
	print(dim(y_train))
	
	subject_train <- read.table(paste(directory, "train/subject_train.txt", sep="/"))
	print(dim(subject_train))
	
    rel_path_signals <- paste(directory, "train", "Inertial Signals", sep="/")
    signal_files <- list.files(rel_path_signals)
    
    for ( i in 1:length(signal_files)) {
        file_name = paste(rel_path_signals, signal_files[i], sep="/")
        train_data <- read.table(file_name)
        print(dim(train_data))
    }
    
    
	
}