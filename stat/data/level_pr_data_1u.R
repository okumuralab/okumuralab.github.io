# par(family="HiraKakuProN-W3") # Mac専用
# par(family="Helvetica")

X = read.csv("http://www.tepco.co.jp/nu/fukushima-np/f1/images/csv_level_pr_data_1u-j.csv",
             # "/usr/local/junk/tepco/csv_level_pr_data_1u-j.csv",
             skip=2, fileEncoding="SJIS", as.is=TRUE,
             na.strings=c("","−","計器不良"))

t = as.POSIXct(ifelse(is.na(X[,1]), NA, paste("2011/",X[,1],sep="")))

# t0 = as.POSIXct("2011-05-20 00:00:00")
n = length(t)
while (n > 1 && is.na(t[n])) n = n - 1
t0 = trunc(t[n], "days") - 7*24*60*60

t1 = t[t >= t0]
x1 = X[t >= t0, 8] # CAMS D/W (A)
x2 = X[t >= t0, 9] # CAMS D/W (B)
x3 = X[t >= t0, 10] # CAMS S/C (A)
x4 = X[t >= t0, 11] # CAMS S/C (B)

xrange = range(c(x1,x2,x3,x4),na.rm=TRUE)

library(Cairo)
Cairo(file="level_pr_data_1u.png", bg="white")
par(mgp=c(2,0.8,0))
plot(range(t1,na.rm=TRUE), xrange,
     type="n", pch=16, ylab="Dose Rate (Sv/h)",
     log=ifelse(xrange[1] > 0, "y", ""),
     xaxt="n", xlab="")

# title(main="CAMS D/W S/C", line=1)
mtext("CAMS", cex=1.2, adj=0.43)
mtext("D/W", col="#f39800", cex=1.2, adj=0.5)
mtext("S/C", col="#0068b7", cex=1.2, adj=0.55)

points(t1, x1, type="o", pch=16, col="#f39800")
points(t1, x2, type="o", pch=15, col="#f39800")
points(t1, x3, type="o", pch=16, col="#0068b7")
points(t1, x4, type="o", pch=15, col="#0068b7")

n = length(x1)
while (is.na(x1[n])) n = n - 1
text(t1[n], x1[n], "A", pos=4, offset=0.5)

n = length(x2)
while (is.na(x2[n])) n = n - 1
text(t1[n], x2[n], "B", pos=4, offset=0.5)

n = length(x3)
while (is.na(x3[n])) n = n - 1
text(t1[n], x3[n], "A", pos=4, offset=0.5)

n = length(x4)
while (is.na(x4[n])) n = n - 1
text(t1[n], x4[n], "B", pos=4, offset=0.5)

r = as.POSIXct(round(range(t1,na.rm=TRUE), "days"))
# r = as.POSIXct(round(range(t1,na.rm=TRUE), "hours"))
# axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%m/%d")
# axis.POSIXct(1, at=seq(r[1],r[2],by="6 hour"), format="%d日%H時")

dev.off()
