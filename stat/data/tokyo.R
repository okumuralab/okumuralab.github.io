# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

tokyo = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/tokyo.csv",
                 as.is=TRUE, comment.char="#")

t = as.POSIXct(tokyo$Date)

lowval = 0.028
hival = 0.079

plot(range(t), range(c(0,tokyo$Average)),
     type="n", xaxt="n", # log="y",
     # col="#f39800",
     # col="#0068b7",
     xlab="", ylab="線量率（μSv/h）")

r = as.POSIXct(round(range(t), "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")

# 過去の平常値の範囲
rect(t[1], lowval, t[length(t)], hival, col=gray(0.9), border=NA)

# 最後にデータをプロット
points(t, tokyo$Average, type="l", pch=16, col="#0068b7")

# m = floor(length(t)*0.25)
# text(t[m], lowval, "過去の平常値の範囲", pos=1)

#---------------------------------------------------------------------
# 範囲を限ってプロット

ts = as.POSIXct("2011-03-13")
te = as.POSIXct("2011-03-19")
t1 = t[t >= ts & t < te]
x1 = tokyo$Average[t >= ts & t < te]
xmax = tokyo$Max[t >= ts & t < te]
xmin = tokyo$Min[t >= ts & t < te]

plot(range(t1), range(c(0,xmax)),
     type="n", xaxt="n", # col="#f39800",
     xlab="", ylab="線量率（μSv/h）")
r = as.POSIXct(round(range(t1), "hours"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%m/%d")

# 過去の平常値の範囲
rect(t1[1], lowval, t1[length(t1)], hival, col=gray(0.9), border=NA)

# エラーバー（正確には最大値と最小値）
# segments(t1, xmin, t1, xmax)
# arrows(t1, xmin, t1, xmax, length=0.05, angle=90, code=3, col=gray(0.5))
segments(t1, xmin, t1, xmax, col=gray(0.5))

# 最後にデータをプロット
points(t1, x1, type="o", pch=16, col="#0068b7")

# 15日の平均
mean15 = mean(tokyo$Average[t >= as.POSIXct("2011-03-15 00:00") & t < as.POSIXct("2011-03-15 23:00")])
segments(as.POSIXct("2011-03-15 00:00"), mean15, as.POSIXct("2011-03-16 00:00"), mean15, col="#f39800", lwd=2)

#---------------------------------------------------------------------
# 線量

avg = mean(tokyo$Average[t < as.POSIXct("2011-03-14")])
sum(tokyo$Average - avg)


#---------------------------------------------------------------------
# フィット

t0 = as.POSIXct("2011-03-24")
t2 = t[t >= t0]
x2 = tokyo$Average[t >= t0]

u2 = 0.5^((as.numeric(t2)-as.numeric(t0))/(8*24*60*60))
coef = lm(x2 ~ u2)$coefficients
curve(coef[2] * 0.5^((x-as.numeric(t0))/(8*24*60*60)) + coef[1], add=TRUE)
abline(h=coef[1], lty=2)
text(t1[1000], coef[1], format(coef[1],digits=3), pos=1)
