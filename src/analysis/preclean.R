library(data.table)
library(dplyr)
require(devtools)
install_github("Displayr/flipTime")
library(flipTime)

dt <- fread('../../gen/data-preparation/output/dataset.csv')

# tag retweets
dt[, retweet:=FALSE]
dt[grepl('^RT', text), retweet:=TRUE]

dt[, datetime:=paste(substr(timestamp, 5, 10),substr(timestamp, 27, 30),substr(timestamp, 12, 19))]
#dt[, time:=]

dt[, datetime:=AsDateTime(datetime)]


dir.create('../../gen/analysis/temp/', recursive = TRUE)
dir.create('../../gen/analysis/output/', recursive = TRUE)
fwrite(dt, '../../gen/analysis/temp/preclean.csv')


 