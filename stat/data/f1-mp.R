# 東電の新フォーマット
# catcsv.rb f1-mp-*.csv > f1-mp.csv
# par(family="HiraKakuProN-W3") # Mac専用
library(colorspace)
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/f1-mp.csv",
             header=TRUE, fileEncoding="SJIS", as.is=TRUE,
             na.strings=c("N/A","-","欠測"))

t = as.POSIXct(paste(X[,1],X[,2]))

ts = trunc(t[length(t)], "days") - 31*24*60*60
t1 = t[t >= ts]
X1 = X[t >= ts, 3:10]
plot(range(t1,na.rm=TRUE), range(c(0,X1),na.rm=TRUE),
     xlab="", ylab="Dose Rate (uSv/h)", # log="y",
     xaxt="n", type="n")
r = as.POSIXct(round(range(t1,na.rm=TRUE), "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%m/%d")

n = length(t1)
# cols = rainbow(8)
# cols = palette()
cols = rainbow_hcl(8, l=40)
for (mp in 1:8) {
  points(t1, X1[,mp], type="l", pch=mp, col=cols[mp])
  k = n
  while (k > 1 && is.na(X1[k,mp])) k = k - 1
  text(t1[k], X1[k,mp], mp, pos=4, offset=0.1, cex=0.8, col=cols[mp])
  k = 1
  while (k < n && is.na(X1[k,mp])) k = k + 1
  text(t1[k], X1[k,mp], mp, pos=2, offset=0.1, cex=0.8, col=cols[mp])
}

# for (i in seq(ts, as.POSIXct("2011-04-18 00:00"), by="day")) {
#   abline(v=i, lty=2)
# }

# coef = lm(log2(x1) ~ t1)$coefficients
# curve(2^(coef[2]*x+coef[1]), add=TRUE)
# (1/coef[2])/(60*60*24)

# u1 = 0.5^((as.numeric(t1)-as.numeric(ts))/(8*24*60*60))
# coef = lm(x1 ~ u1)$coefficients
# curve(coef[2] * 0.5^((x-as.numeric(ts))/(8*24*60*60)) + coef[1], add=TRUE)
# abline(h=coef[1],lty=2)
# text(t1[1], coef[1], format(coef[1],digits=3), pos=3)

