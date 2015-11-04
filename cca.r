library(data.table)
library(ggplot2)
library(GGally)
library(CCA)
library(plyr)
amazonData = fread("~/Desktop/amazon.txt")
amazonData$date = as.Date(amazonData$date)
amazonData$date = as.numeric(amazonData$date)
avgAmazon = ddply(amazonData, ~item, summarize, ave.date = mean(date), ave.rating = mean(rating), ave.vote = mean(votes), ave.helpful = mean(helpful))
candidate = avgAmazon[,-c(1)]
ggpairs(candidate)
firstSet = avgAmazon[,c(2,3)]
secondSet = avgAmazon[,c(4,5)]
X <- as.matrix(firstSet)
Y <- as.matrix(secondSet)
correl <- matcor(X, Y)
img.matcor(correl, type = 1)
firstSet = avgAmazon[,c(4,3)]
secondSet = avgAmazon[,c(2,5)]
correl <- matcor(firstSet, secondSet)
img.matcor(correl, type = 1)
firstSet = avgAmazon[,c(2,4)]
secondSet = avgAmazon[,c(3,5)]
correl <- matcor(firstSet, secondSet)
img.matcor(correl, type = 1)