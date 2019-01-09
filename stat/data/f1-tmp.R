# 東電の新フォーマット
# catcsv.rb f1-tmp-*.csv > f1-tmp.csv
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/f1-tmp.csv",
             header=TRUE, fileEncoding="SJIS", as.is=TRUE,
             na.strings=c("N/A","-","0",""))

t = as.POSIXct(paste(X[,1],X[,2]))

# μSv/hに統一
X[,3] = ifelse(X[,3] < 2, X[,3]*1000, X[,3])

# t0 = as.POSIXct("2011-03-11 00:00:00")
# t0 = as.POSIXct("2011-03-26 11:20:00")
t0 = as.POSIXct("2011-05-01 00:00:00")
t1 = t[t >= t0]
x1 = X[t >= t0, 3]  # 事務本館南側
plot(t1, x1, type="l", pch=16, ylab="線量率（μSv/h）", xaxt="n", xlab="", # log="y",
     col="#f39800")
r = as.POSIXct(round(range(c(t1,t2),na.rm=TRUE), "days"))
# r = as.POSIXct(round(range(c(t1,t2),na.rm=TRUE), "hours"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
# axis.POSIXct(1, at=seq(r[1],r[2],by="6 hour"), format="%d日%H時")

for (i in seq(r[1], r[2], by="day")) {
  abline(v=i, lty=2)
}

u1 = 0.5^((as.numeric(t1)-as.numeric(t0))/(8*24*60*60))
coef = lm(x1 ~ u1)$coefficients
curve(coef[2] * 0.5^((x-as.numeric(t0))/(8*24*60*60)) + coef[1], add=TRUE)
abline(h=coef[1],lty=2)
text(t1[1], coef[1], format(coef[1],digits=3), pos=3)

# coef = lm(log2(x1) ~ t1)$coefficients
# curve(2^(coef[2]*x+coef[1]), add=TRUE)
# (1/coef[2])/(60*60*24)
