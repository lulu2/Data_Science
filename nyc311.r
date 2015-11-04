library(data.table)
library(plyr)
data = fread("~/Downloads/nyc311calls.csv")

## function to display 10 decimal
specify_decimal <- function(x, k) format(round(x, k), nsmall=k)

names(data) = make.names(names(data))

## factor Agency Name
data$Agency = factor(data$Agency)
AgencyType = table(data$Agency)
AgencyType = AgencyType[order(AgencyType,decreasing=TRUE)]

## What fraction of complaints are associated with the 2nd most popular agency?
specify_decimal(AgencyType[2]/sum(AgencyType),10)
## 0.1719314121

## how many entries are missing in "Latitude"
sum(is.na(data$Latitude))

latitude = data$Latitude[!is.na(data$Latitude)]
## What is the distance (in degrees) between the 90% and 10% percentiles of degrees latitude?
specify_decimal(quantile(latitude,0.9)-quantile(latitude,0.1), 10)
##  0.2357908310

time = strptime(data$Created.Date,format="%m/%d/%Y %I:%M:%S %p")
time12 = which(time$hour==0 & time$min==0 & time$sec==0)
time7 = which(time$hour==7 & time$min==0 & time$sec==0)
temp = c(time12, time7)
real = time[-c(temp)]
calls = table(real$hour)
specify_decimal((max(calls)-min(calls))/2103,10)
### 237.7855444603

## 2103 days in total
as.Date(real[1])- as.Date(real[length(real)])

#temp = strptime("10/06/2012 7:00:00 PM", format="%m/%d/%Y %I:%M:%S %p")$min

complaint1 = ddply(data, ~Complaint.Type, summarize, n = sum(!is.na(Complaint.Type)))
complaint = ddply(data, ~Complaint.Type+Borough, summarize, n = sum(!is.na(Complaint.Type)))
borough = ddply(data, ~Borough, summarize, n = sum(!is.na(Borough)))
total = sum(complaint$n)
complaint$condprob = 0
complaint$result = 0

for( i in 1:nrow(complaint)){
  complaint$condprob[i] = (complaint$n[i])/(borough[which(borough$Borough==complaint$Borough[i]),]$n)
  complaint$result[i] = complaint$condprob[i]/(complaint1[which(complaint1$Complaint.Type==complaint$Complaint.Type[i]),]$n/total)
}

## suprising ratio
specify_decimal(max(complaint$result), 10)
## 18.2636539395

# Convert degrees to radians
deg2rad <- function(deg) return(deg*pi/180)

# Calculates the geodesic distance between two points specified by radian latitude/longitude using the
# Spherical Law olibrary(data.table)
library(plyr)
data = fread("~/Downloads/nyc311calls.csv")

## function to display 10 decimal
specify_decimal <- function(x, k) format(round(x, k), nsmall=k)

names(data) = make.names(names(data))

## factor Agency Name
data$Agency = factor(data$Agency)
AgencyType = table(data$Agency)
AgencyType = AgencyType[order(AgencyType,decreasing=TRUE)]

## What fraction of complaints are associated with the 2nd most popular agency?
specify_decimal(AgencyType[2]/sum(AgencyType),10)
## 0.1719314121

## how many entries are missing in "Latitude"
sum(is.na(data$Latitude))

latitude = data$Latitude[!is.na(data$Latitude)]
## What is the distance (in degrees) between the 90% and 10% percentiles of degrees latitude?
specify_decimal(quantile(latitude,0.9)-quantile(latitude,0.1), 10)
##  0.2357908310

time = strptime(data$Created.Date,format="%m/%d/%Y %I:%M:%S %p")
time12 = which(time$hour==0 & time$min==0 & time$sec==0)
time7 = which(time$hour==7 & time$min==0 & time$sec==0)
temp = c(time12, time7)
real = time[-c(temp)]
calls = table(real$hour)
specify_decimal((max(calls)-min(calls))/2103,10)
### 237.7855444603

## 2103 days in total
as.Date(real[1])- as.Date(real[length(real)])

#temp = strptime("10/06/2012 7:00:00 PM", format="%m/%d/%Y %I:%M:%S %p")$min

complaint1 = ddply(data, ~Complaint.Type, summarize, n = sum(!is.na(Complaint.Type)))
complaint = ddply(data, ~Complaint.Type+Borough, summarize, n = sum(!is.na(Complaint.Type)))
borough = ddply(data, ~Borough, summarize, n = sum(!is.na(Borough)))
total = sum(complaint$n)
complaint$condprob = 0
complaint$result = 0

for( i in 1:nrow(complaint)){
  complaint$condprob[i] = (complaint$n[i])/(borough[which(borough$Borough==complaint$Borough[i]),]$n)
  complaint$result[i] = complaint$condprob[i]/(complaint1[which(complaint1$Complaint.Type==complaint$Complaint.Type[i]),]$n/total)
}

## suprising ratio
specify_decimal(max(complaint$result), 10)
## 18.2636539395

# Convert degrees to radians
deg2rad <- function(deg) return(deg*pi/180)

# Calculates the geodesic distance between two points specified by radian latitude/longitude using the
# Spherical Law of Cosines (slc)
gcd.slc <- function(long1, lat1, long2, lat2) {
  R <- 6371 # Earth mean radius [km]
  d <- acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2) * cos(long2-long1)) * R
  return(d) # Distance in km
}

rad1 = deg2rad(data$Latitude[!is.na(data$Latitude)])
rad2 = deg2rad(data$Longitude[!is.na(data$Longitude)])

a = mean(rad1, na.rm = TRUE)
aa = sd(rad1, na.rm = TRUE)
b = mean(rad2, na.rm=TRUE)
bb = sd(rad2, na.rm = TRUE)

long= gcd.slc(a,b,a+aa, b)
short = gcd.slc(a,b,a,b+bb)
specify_decimal(pi*long*short,10)
## 76.7517951704

## standard deviation
realsecond = as.numeric(real)
realsecond = realsecond[order(realsecond)]
realsecond2 = c(realsecond[-c(1)], realsecond[length(realsecond)])
difference = realsecond2-realsecond
specify_decimal(sd(head(difference,-1), na.rm = TRUE),10)
## 64.4769629298f Cosines (slc)
gcd.slc <- function(long1, lat1, long2, lat2) {
  R <- 6371 # Earth mean radius [km]
  d <- acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2) * cos(long2-long1)) * R
  return(d) # Distance in km
}

rad1 = deg2rad(data$Latitude[!is.na(data$Latitude)])
rad2 = deg2rad(data$Longitude[!is.na(data$Longitude)])

a = mean(rad1, na.rm = TRUE)
aa = sd(rad1, na.rm = TRUE)
b = mean(rad2, na.rm=TRUE)
bb = sd(rad2, na.rm = TRUE)

long= gcd.slc(a,b,a+aa, b)
short = gcd.slc(a,b,a,b+bb)
specify_decimal(pi*long*short,10)
## 76.7517951704

## standard deviation
realsecond = as.numeric(real)
realsecond = realsecond[order(realsecond)]
realsecond2 = c(realsecond[-c(1)], realsecond[length(realsecond)])
difference = realsecond2-realsecond
specify_decimal(sd(head(difference,-1), na.rm = TRUE),10)
## 64.4769629298
