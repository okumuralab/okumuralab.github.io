# 東電の新フォーマット
# catcsv.rb f1-mc-*.csv > f1-mc.csv
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/f1-mc.csv",
             header=TRUE, fileEncoding="SJIS", as.is=TRUE,
             na.strings=c("N/A","-"))

t = as.POSIXct(paste(X[,1],X[,2]))

# 東電のデータがnGy/hとμSv/hを混同している！
# X[,4] = ifelse(t < as.POSIXct("2011-03-12 06:00"), X[,4]/1000, X[,4])
# 2011-05-28の新データで直った

# ts = as.POSIXct("2011-03-14 00:00:00")
# ts = as.POSIXct("2011-03-26 11:20:00")
ts = as.POSIXct("2011-07-05 00:00:00")
# te = as.POSIXct("2011-03-17 00:00:00")
te = as.POSIXct("2011-12-31 00:00:00")
t1 = t[grepl("^西門", X[,3]) & t >= ts & t <= te]
x1 = X[grepl("^西門", X[,3]) & t >= ts & t <= te, 4]
t2 = t[grepl("^正門", X[,3]) & t >= ts & t <= te]
x2 = X[grepl("^正門", X[,3]) & t >= ts & t <= te, 4]

plot(range(c(t1),na.rm=TRUE),
     range(c(x1),na.rm=TRUE),
     type="n", ylab="線量率（μSv/h）", # log="y",
     xaxt="n", xlab="")

points(t1, x1, type="l", pch=16, col="#f39800")
# points(t2, x2, type="l", pch=16, col="#0068b7")

r = as.POSIXct(round(range(c(t1,t2),na.rm=TRUE), "days"))
# r = as.POSIXct(round(range(c(t1,t2),na.rm=TRUE), "hours"))
# axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%m/%d")
# axis.POSIXct(1, at=seq(r[1],r[2],by="6 hour"), format="%d日%H時")

mtext("福島第一原発　　・", adj=0)
mtext("　　　　　　正門", col="#0068b7", adj=0)
mtext("　　　　　　　　　西門", col="#f39800", adj=0)

n = length(x1)
while (is.na(x1[n])) n = n - 1
text(t1[n], x1[n], x1[n], pos=4, offset=0.1, cex=0.8)
text(t1[1], x1[1], x1[1], pos=2, offset=0.1, cex=0.8)

# for (i in seq(ts, as.POSIXct("2011-04-18 00:00"), by="day")) {
#   abline(v=i, lty=2)
# }

# coef = lm(log2(x1) ~ t1)$coefficients
# curve(2^(coef[2]*x+coef[1]), add=TRUE)
# (1/coef[2])/(60*60*24)

u1 = 0.5^((as.numeric(t1)-as.numeric(ts))/(8*24*60*60))
coef = lm(x1 ~ u1)$coefficients
curve(coef[2] * 0.5^((x-as.numeric(ts))/(8*24*60*60)) + coef[1], add=TRUE)
abline(h=coef[1],lty=2)
text(t1[1], coef[1], format(coef[1],digits=3), pos=3)

#-------------------------------------------------------------------------------

# catcsv.rb f1-mc-*.csv > f1-mc.csv
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/f1-mc.csv",
             header=TRUE, fileEncoding="SJIS", as.is=TRUE,
             na.strings=c("N/A","-"))

t = as.POSIXct(paste(X[,1],X[,2]))

ts = as.POSIXct("2011-03-11 00:00:00")
te = as.POSIXct("2011-03-17 00:00:00")
t1 = t[t >= ts & t <= te]
x1 = X[t >= ts & t <= te, 4]
p1 = sub("^(MP)?-?(.*)$", "\\2", X[t >= ts & t <= te, 3])

plot(t1, x1, pch=p1,
     type="p", ylab="線量率（μSv/h）", # log="y",
     xaxt="n", xlab="")

r = as.POSIXct(round(range(c(t1,t2),na.rm=TRUE), "days"))
# r = as.POSIXct(round(range(c(t1,t2),na.rm=TRUE), "hours"))
# axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%m/%d")
# axis.POSIXct(1, at=seq(r[1],r[2],by="6 hour"), format="%d日%H時")

#----------------------------------------------------------------------

ts = as.POSIXct("2011-03-11 00:00:00")
# ts = as.POSIXct("2011-03-26 11:20:00")
# ts = as.POSIXct("2011-07-05 00:00:00")
# te = as.POSIXct("2011-03-17 00:00:00")
te = as.POSIXct("2011-03-26 00:00:00")
t1 = t[grepl("^西門", X[,3]) & t >= ts & t <= te]
x1 = X[grepl("^西門", X[,3]) & t >= ts & t <= te, 4] / 1000
t2 = t[grepl("^正門", X[,3]) & t >= ts & t <= te]
x2 = X[grepl("^正門", X[,3]) & t >= ts & t <= te, 4] / 1000
t3 = t[grepl("^事務本館北", X[,3]) & t >= ts & t <= te]
x3 = X[grepl("^事務本館北", X[,3]) & t >= ts & t <= te, 4] / 1000

plot(range(c(t1,t2,t3),na.rm=TRUE),
     range(c(x1,x2,x3,0),na.rm=TRUE),
     type="n", ylab="線量率（mSv/h）", # log="y",
     xaxt="n", xlab="")

points(t1, x1, type="p", pch=1, col="#f39800")
points(t2, x2, type="p", pch=1, col="#0068b7")
points(t3, x3, type="p", pch=1, col="#669933")

r = as.POSIXct(round(range(c(t1,t2),na.rm=TRUE), "days"))
# r = as.POSIXct(round(range(c(t1,t2),na.rm=TRUE), "hours"))
# axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%m/%d")
# axis.POSIXct(1, at=seq(r[1],r[2],by="6 hour"), format="%d日%H時")
mtext("福島第一原発　　・　　・", adj=0)
mtext("　　　　　　正門", col="#0068b7", adj=0)
mtext("　　　　　　　　　西門", col="#f39800", adj=0)
mtext("　　　　　　　　　　　　事務本館北", col="#669933", adj=0)
