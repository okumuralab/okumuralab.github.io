# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/7houbu.csv",
              fileEncoding="SJIS", na.strings = "-", as.is=TRUE)
t = as.POSIXct(X$日時)

plot(NULL, type="l", xaxt="n", xlab="",
     ylab="線量率（μSv/h）", # log="y",
     xlim=range(t), ylim=range(X[,2:9], na.rm=TRUE))
for (i in 1:8)
  points(t, X[,i+1], type="l", col=rainbow(8)[i])
r = as.POSIXct(round(range(t), "days"))
# axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%d日")
legend(as.POSIXct("2011-03-27"), 25, names(X[2:9]), col=rainbow(8),lwd=1, ncol=2)

# 半減期8日の直線を引く
x0 = as.POSIXct("2011-03-15 18:30:00")
y0 = log2(X[t==x0,2])
curve(2^(y0-(x-as.numeric(x0))/(8*60*60*24)), add=TRUE)

#---------------------------------------------------------------------
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/7houbu.csv",
              fileEncoding="SJIS", na.strings = "-", as.is=TRUE)
t = as.POSIXct(X$日時)

t0 = as.POSIXct("2011-03-11 00:00:00")
t1 = t[t >= t0]
x1 = X[t >= t0, 2]
plot(t1, x1, type="o", pch=16, xaxt="n", xlab="", #log="y",
     ylab="線量率（μSv/h）", col="#f39800")
r = as.POSIXct(round(range(t1), "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")

y = x1 - 0.04
v1 = 0.5^(as.numeric(t1-t0)/(8*24*60*60))
# v2 = 0.5^(as.numeric(t1-t0)/(30*365*24*60*60))
# coef = lm(y ~ v1 + v2 - 1)$coefficients
coef = lm(y ~ v1 - 1)$coefficients
# curve(coef[1]*0.5^((x-as.numeric(t0))/(8*24*60*60))+coef[2]*0.5^((x-as.numeric(t0))/(30*365*24*60*60))+0.04, add=TRUE)
curve(coef[1]*0.5^((x-as.numeric(t0))/(8*24*60*60))+0.04, add=TRUE)

# 積分
a = 0
n = length(X[,2])
cum = rep(NA, n)
i = 1
cum[1] = 0
while (i < n && is.na(X[i,2])) {
  i = i + 1
}
while (i < n) {
  j = i + 1
  while (j < n && is.na(X[j,2])) j = j + 1
  dt = (as.numeric(t[j]) - as.numeric(t[i])) / (60 * 60)
  x = (X[i,2] + X[j,2]) / 2
  a = a + x * dt
  i = j
  cum[i] = a
}
