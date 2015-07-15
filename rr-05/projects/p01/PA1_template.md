# Reproducible Research: Peer Assessment 1


## Loading and preprocessing the data


```r
# Load required libraries
library(data.table)
library(dplyr)
```

```
## 
## Attaching package: 'dplyr'
## 
## The following objects are masked from 'package:data.table':
## 
##     between, last
## 
## The following object is masked from 'package:stats':
## 
##     filter
## 
## The following objects are masked from 'package:base':
## 
##     intersect, setdiff, setequal, union
```

```r
library(lubridate)
```

```
## 
## Attaching package: 'lubridate'
## 
## The following objects are masked from 'package:data.table':
## 
##     hour, mday, month, quarter, wday, week, yday, year
```

```r
library(plyr)
```

```
## -------------------------------------------------------------------------
## You have loaded plyr after dplyr - this is likely to cause problems.
## If you need functions from both plyr and dplyr, please load plyr first, then dplyr:
## library(plyr); library(dplyr)
## -------------------------------------------------------------------------
## 
## Attaching package: 'plyr'
## 
## The following object is masked from 'package:lubridate':
## 
##     here
## 
## The following objects are masked from 'package:dplyr':
## 
##     arrange, count, desc, failwith, id, mutate, rename, summarise,
##     summarize
```

```r
library(reshape2)

data <- read.table("activity.csv", header=T, sep=',', na.strings="NA", 
                   stringsAsFactors = FALSE)
# Convert the data to table data and remove from the memory
new_data <- tbl_df(data)
rm(data)


# Mutate so that the format of Date and Time(POSIXct) column is no longer a string
new_data <- mutate(new_data, date = as.Date(date, format="%Y-%m-%d"))
print(new_data)
```

```
## Source: local data frame [17,568 x 3]
## 
##    steps       date interval
## 1     NA 2012-10-01        0
## 2     NA 2012-10-01        5
## 3     NA 2012-10-01       10
## 4     NA 2012-10-01       15
## 5     NA 2012-10-01       20
## 6     NA 2012-10-01       25
## 7     NA 2012-10-01       30
## 8     NA 2012-10-01       35
## 9     NA 2012-10-01       40
## 10    NA 2012-10-01       45
## ..   ...        ...      ...
```

## What is mean total number of steps taken per day?

```r
stepsPerDay <- ddply(
    new_data, 
    .(date), 
    function(x) {  
        sum(x$steps, na.rm = T)
    }
)

plot(x = stepsPerDay$date, y = stepsPerDay$V1, type= "h")
```

![](PA1_template_files/figure-html/unnamed-chunk-2-1.png) 

```r
mean <- mean(stepsPerDay$V1)
print(mean)
```

```
## [1] 9354.23
```

```r
median <- median(stepsPerDay$V1)
print(median)
```

```
## [1] 10395
```

## What is the average daily activity pattern?



## Imputing missing values



## Are there differences in activity patterns between weekdays and weekends?

