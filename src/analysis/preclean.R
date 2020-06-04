library(data.table)
library(dplyr)
library(flipTime)

dt <- fread('../../gen/data-preparation/output/dataset.csv')

# tag retweets
dt[, retweet:=FALSE]
dt[grepl('^RT', text), retweet:=TRUE]

dt[, datetime:=paste(substr(timestamp, 5, 10),substr(timestamp, 27, 30),substr(timestamp, 12, 19))]
#dt[, time:=]

dt[, datetime:=AsDateTime(datetime)]
dt[, datetime:=gsub("T", " ", datetime)] 
dt[, datetime:=gsub("Z", "", datetime)]
dt[, event:= if_else(strftime(datetime, format = "%Y-%m-%d %H:%M:%S") <= 
    strftime("2020-04-23 23:25:00",format = "%Y-%m-%d %H:%M:%S"), "1", "")]
dt[,event:=if_else(strftime(datetime, format = "%Y-%m-%d %H:%M:%S") <= 
    strftime("2020-04-24 14:25:00",format = "%Y-%m-%d %H:%M:%S") & 
    strftime(datetime, format = "%Y-%m-%d %H:%M:%S") >= 
    strftime("2020-04-24 13:20:00",format = "%Y-%m-%d %H:%M:%S"), "2", event)] 
dt[,event:=if_else(strftime(datetime, format = "%Y-%m-%d %H:%M:%S") <= 
    strftime("2020-04-25 04:25:00",format = "%Y-%m-%d %H:%M:%S") & 
    strftime(datetime, format = "%Y-%m-%d %H:%M:%S") >= 
    strftime("2020-04-25 03:20:00",format = "%Y-%m-%d %H:%M:%S"), "3", event)]
dt[,event:=if_else(strftime(datetime, format = "%Y-%m-%d %H:%M:%S") <= 
    strftime("2020-04-25 15:25:00",format = "%Y-%m-%d %H:%M:%S") & 
    strftime(datetime, format = "%Y-%m-%d %H:%M:%S") >= 
    strftime("2020-04-25 14:20:00",format = "%Y-%m-%d %H:%M:%S"), "4", event)]
dt[,event:=if_else(strftime(datetime, format = "%Y-%m-%d %H:%M:%S") <= 
    strftime("2020-04-25 22:30:00",format = "%Y-%m-%d %H:%M:%S") & 
    strftime(datetime, format = "%Y-%m-%d %H:%M:%S") >= 
    strftime("2020-04-25 21:20:00",format = "%Y-%m-%d %H:%M:%S"), "5", event)]
dt[,event:=as.factor(event)]



dir.create('../../gen/analysis/temp/', recursive = TRUE)
dir.create('../../gen/analysis/output/', recursive = TRUE)
fwrite(dt, '../../gen/analysis/temp/preclean.csv')


 