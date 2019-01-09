# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/20-50km.csv",
              fileEncoding="SJIS", na.strings = c("-","--"), as.is=TRUE)
t = as.POSIXct(X$日時)

plot(NULL, type="l", xaxt="n", xlab="",
     ylab="線量率（μSv/h）", # log="y",
     xlim=range(t), ylim=range(X[,2:9], na.rm=TRUE))
for (i in 1:8)
  points(t, X[,i+1], type="o", pch=i, col=rainbow(8)[i])
r = as.POSIXct(round(range(t), "days"))
# axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%d日")
legend(as.POSIXct("2011-04-03"), 45, names(X[2:9]),
       col=rainbow(8), lty=1, pch=1:8, ncol=2)

# 半減期8日の直線を引く
x0 = as.POSIXct("2011-03-15 18:20:00")
y0 = log2(X[t==x0,4])
curve(2^(y0-(x-as.numeric(x0))/(8*60*60*24)), add=TRUE)

#---------------------------------------------------------------------
# 飯舘村だけ
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

p = 14 # 飯舘村役場
X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/20-50km.csv",
              header=TRUE, fileEncoding="SJIS", na.strings = c("-","--"), as.is=TRUE)
t = as.POSIXct(X$日時)
t0 = as.POSIXct("2011-03-11 00:00:00")
# t0 = as.POSIXct("2011-05-01 00:00:00")
t1 = t[t >= t0 & !is.na(X[,p])]
x1 = X[t >= t0 & !is.na(X[,p]), p]
plot(t1, x1, type="n", xaxt="n", xlab="", ylab="線量率（μSv/h）")
r = as.POSIXct(round(range(t1), "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
# axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%d日")

for (i in seq(r[1], r[2], by="day")) {
  abline(v=i, col=gray(0.8))
}

for (i in seq(0, max(x1), by=10)) {
  abline(h=i, col=gray(0.8))
}

points(t1, x1, type="l", col="#0068b7")

text(t1[length(t1)], x1[length(x1)], x1[length(x1)], pos=4, offset=0.1, cex=0.8)

#---------------------------------------------------------------------
# 飯舘村だけ
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

p = 13 # 飯舘村役場
# p = 4 # 飯舘村長泥
X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/20-50km5.csv",
              header=TRUE, fileEncoding="SJIS", na.strings = c("-","--"), as.is=TRUE)
t = as.POSIXct(X$日時)
# t0 = as.POSIXct("2011-03-11 00:00:00")
t0 = as.POSIXct("2011-05-01 00:00:00")
t1 = t[t >= t0 & !is.na(X[,p])]
x1 = X[t >= t0 & !is.na(X[,p]), p]
plot(t1, x1, type="n", xaxt="n", xlab="", ylab="線量率（μSv/h）")
r = as.POSIXct(round(range(t1), "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
# axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%d日")

for (i in seq(r[1], r[2], by="day")) {
  abline(v=i, col=gray(0.8))
}

for (i in seq(0, max(x1), by=10)) {
  abline(h=i, col=gray(0.8))
}

points(t1, x1, type="l")

text(t1[length(t1)], x1[length(x1)], x1[length(x1)], pos=4, offset=0.1, cex=0.8)

#---------------------------------------------------------------------
# 飯舘村の積算線量を求める

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/20-50km5.csv",
              fileEncoding="SJIS", na.strings = c("-","--",""), as.is=TRUE)
t = as.POSIXct(X$日時)

p = 3
a = 0
n = length(X[,p])
cum = rep(NA, n)
i = 1
cum[1] = 0
while (i < n && is.na(X[i,p])) {
  i = i + 1
}
while (i < n) {
  j = i + 1
  while (j < n && is.na(X[j,p])) j = j + 1
  dt = (as.numeric(t[j]) - as.numeric(t[i])) / (60 * 60)
  x = (X[i,p] + X[j,p]) / 2
  a = a + x * dt
  i = j
  cum[i] = a
}

# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))
plot(t, X[,p], type="o", xaxt="n", xlab="", # log="y",
     pch=16, ylab="線量率（μSv/h）", col="#0068b7")
r = as.POSIXct(round(range(t), "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%d日")

# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))
plot(t, cum/1000, type="o", xaxt="n", xlab="", # log="y",
     pch=16, ylab="線量（mSv）", col="#0068b7")
r = as.POSIXct(round(range(t), "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%d日")
