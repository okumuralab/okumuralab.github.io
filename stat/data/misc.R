# 文科省のまとめた空間線量率データのプロット
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

# 東京都2011-03-15 00:00から2011-04-30 23:00まで
東京都 = c(0.0345,0.0347,0.0345,0.0347,0.100,0.0875,0.0495,0.0453,0.0573,0.202,0.496,0.106,0.0713,0.0658,0.0716,0.0682,0.0682,
0.094,0.2,0.361,0.123,0.089,0.066,0.056,0.054,0.055,0.067,0.101,0.141,0.143,0.142,0.104,0.089,0.069,0.058,0.057,0.056,0.055,0.054,0.054,0.054,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.053,0.052,0.052,0.052,0.052,0.052,0.052,0.052,0.052,0.051,0.051,0.051,0.051,0.051,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.049,0.05,0.049,0.049,0.049,0.049,0.049,0.049,0.048,0.049,0.049,0.049,0.048,0.048,0.048,0.047,0.048,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.048,0.047,0.047,0.047,0.048,0.047,0.048,0.047,0.047,0.047,0.047,0.047,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.046,0.045,0.045,0.045,0.045,0.045,0.045,0.044,0.045,0.044,0.044,0.048,0.049,0.051,0.051,0.05,0.05,0.051,0.052,0.054,0.059,0.07,0.096,0.1,0.109,0.113,0.108,0.112,0.118,0.125,0.134,0.135,0.134,0.137,0.137,0.141,0.141,0.142,0.137,0.134,0.134,0.133,0.133,0.131,0.129,0.128,0.127,0.127,0.128,0.128,0.13,0.137,0.139,0.138,0.138,0.14,0.141,0.155,0.151,0.151,0.154,0.154,0.152,0.152,0.149,0.148,0.147,0.147,0.146,0.146,0.146,0.145,0.145,0.144,0.144,0.143,0.143,0.146,0.145,0.144,0.147,0.148,0.146,0.143,0.141,0.14,0.14,0.139,0.139,0.139,0.139,0.139,0.139,0.139,0.138,0.138,0.138,0.138,0.137,0.136,0.136,0.136,0.135,0.134,0.134,0.134,0.135,0.135,0.134,0.134,0.134,0.134,0.133,0.132,0.132,0.132,0.132,0.132,0.132,0.132,0.129,0.13,0.13,0.129,0.129,0.127,0.127,0.126,0.126,0.126,0.126,0.125,0.125,0.125,0.125,0.126,0.126,0.126,0.124,0.124,0.124,0.123,0.122,0.122,0.122,0.122,0.121,0.121,0.12,0.12,0.119,0.118,0.119,0.119,0.119,0.119,0.119,0.118,0.118,0.118,0.117,0.117,0.117,0.117,0.118,0.117,0.116,0.116,0.116,0.116,0.116,0.116,0.115,0.114,0.114,0.114,0.114,0.113,0.113,0.112,0.112,0.112,0.113,0.113,0.112,0.112,0.112,0.112,0.112,0.112,0.112,0.112,0.112,0.111,0.111,0.111,0.111,0.111,0.109,0.108,0.109,0.109,0.108,0.109,0.108,0.108,0.108,0.107,0.108,0.108,0.108,0.108,0.108,0.108,0.108,0.108,0.108,0.108,0.108,0.107,0.107,0.106,0.105,0.105,0.105,0.105,0.105,0.105,0.105,0.105,0.105,0.104,0.104,0.104,0.104,0.105,0.106,0.108,0.11,0.108,0.107,0.105,0.104,0.103,0.103,0.103,0.102,0.103,0.102,0.102,0.102,0.102,0.104,0.101,0.101,0.101,0.101,0.1,0.101,0.101,0.101,0.102,0.101,0.102,0.102,0.101,0.101,0.103,0.103,0.101,0.099,0.099,0.099,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.098,0.099,0.099,0.099,0.098,0.098,0.098,0.097,0.097,0.097,0.096,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.095,0.096,0.096,0.096,0.096,0.096,0.095,0.096,0.096,0.095,0.094,0.094,0.094,0.094,0.093,0.093,0.092,0.092,0.092,0.092,0.091,0.091,0.091,0.091,0.091,0.091,0.091,0.091,0.091,0.091,0.091,0.091,0.091,0.091,0.091,0.091,0.09,0.09,0.09,0.09,0.09,0.09,0.09,0.09,0.09,0.091,0.09,0.09,0.09,0.09,0.09,0.09,0.09,0.09,0.09,0.09,0.09,0.089,0.089,0.088,0.089,0.088,0.089,0.088,0.088,0.089,0.089,0.089,0.089,0.089,0.088,0.089,0.089,0.089,0.089,0.089,0.089,0.09,0.089,0.089,0.089,0.089,0.089,0.088,0.087,0.087,0.087,0.087,0.087,0.087,0.087,0.088,0.087,0.087,0.087,0.087,0.088,0.088,0.089,0.089,0.088,0.088,0.088,0.088,0.087,0.087,0.087,0.087,0.086,0.087,0.087,0.087,0.086,0.086,0.087,0.087,0.086,0.087,0.087,0.086,0.086,0.087,0.088,0.087,0.086,0.087,0.087,0.086,0.086,0.086,0.086,0.085,0.085,0.085,0.086,0.085,0.085,0.085,0.085,0.085,0.085,0.085,0.085,0.085,0.085,0.085,0.085,0.085,0.085,0.085,0.085,0.085,0.085,0.085,0.084,0.085,0.085,0.084,0.084,0.084,0.084,0.085,0.084,0.085,0.084,0.084,0.084,0.084,0.084,0.084,0.084,0.084,0.085,0.085,0.084,0.084,0.084,0.083,0.083,0.084,0.084,0.084,0.084,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.082,0.083,0.083,0.083,0.084,0.084,0.083,0.083,0.083,0.082,0.083,0.082,0.083,0.083,0.082,0.082,0.082,0.082,0.082,0.082,0.082,0.082,0.083,0.083,0.082,0.083,0.083,0.083,0.083,0.082,0.083,0.082,0.082,0.082,0.086,0.093,0.086,0.083,0.089,0.09,0.083,0.081,0.082,0.079,0.078,0.077,0.077,0.077,0.077,0.078,0.077,0.078,0.078,0.078,0.078,0.078,0.078,0.078,0.078,0.078,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.078,0.078,0.079,0.079,0.078,0.078,0.078,0.078,0.078,0.078,0.078,0.078,0.077,0.077,0.077,0.078,0.078,0.077,0.077,0.078,0.078,0.077,0.078,0.078,0.078,0.078,0.079,0.079,0.079,0.078,0.078,0.078,0.078,0.078,0.078,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.077,0.078,0.078,0.078,0.077,0.078,0.078,0.078,0.077,0.077,0.077,0.077,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.077,0.077,0.077,0.077,0.077,0.077,0.076,0.077,0.076,0.076,0.076,0.076,0.076,0.075,0.075,0.075,0.075,0.075,0.075,0.075,0.075,0.075,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.076,0.075,0.075,0.075,0.075,0.075,0.075,0.076,0.075,0.075,0.075,0.075,0.075,0.075,0.075,0.075,0.075,0.076,0.076,0.076,0.075,0.075,0.075,0.076,0.075,0.075,0.075,0.075,0.075,0.075,0.075,0.075,0.075,0.075,0.075,0.076,0.076,0.078,0.080,0.079,0.076,0.074,0.074,0.074,0.074,0.074,0.075,0.074,0.073,0.073,0.076,0.082,0.081,0.076,0.073,0.072,0.072,0.072,0.072,0.072,0.073,0.073,0.072,0.073,0.073,0.073,0.073,0.074,0.073,0.074,0.074,0.074,0.074,0.073,0.073,0.072,0.072,0.072,0.072,0.072,0.073,0.072,0.072,0.073,0.073,0.073,0.073,0.072,0.072,0.072,0.072,0.072,0.073,0.073,0.073,0.072,0.073,0.072,0.072,0.072,0.073,0.072,0.072,0.072,0.072,0.072,0.072,0.072,0.072,0.072,0.072,0.072,0.073,0.073,0.073,0.073,0.073,0.073,0.072,0.073,0.073,0.072,0.073,0.072,0.072,0.072,0.072,0.072,0.072,0.072,0.072,0.073,0.073,0.073,0.072,0.072,0.072,0.072,0.071,0.071,0.071,0.071,0.071,0.071,0.071,0.071,0.071,0.070,0.071,0.071,0.071,0.071,0.071,0.071,0.070,0.070,0.069,0.069,0.069,0.070,0.070,0.070,0.070,0.071,0.071,0.070,0.070,0.070,0.070,0.070,0.07,0.069,0.072,0.072,0.07,0.07,0.069,0.069,0.069,0.069,0.069,0.069,0.069,0.069,0.07,0.07,0.07,0.07,0.07,0.07,0.071,0.071,0.071,0.07,0.070,0.069,0.070,0.069,0.069,0.069,0.069,0.069,0.069,0.069,0.069,0.069,0.069,0.070,0.070,0.070,0.070,0.070,0.070,0.069,0.070,0.069,0.069,0.070,0.069,0.069,0.069,0.069,0.069,0.069,0.069,0.069,0.070,0.069,0.069,0.069,0.069,0.069,0.070,0.070,0.069,0.069,0.069,0.070,0.069,0.069,0.069,0.069,0.069,0.069,0.069,0.069,0.069,0.070,0.070,0.069,0.070,0.070,0.070,0.072,0.070,0.069,0.068,0.069,0.069,0.069,0.069,0.069,0.069,0.069,0.068,0.068,0.068,0.068,0.068,0.068,0.068,0.068,0.068,0.067,0.067,0.067,0.067,0.067,0.068,0.068,0.069,0.068,0.068,0.068,0.068,0.068,0.068,0.068,0.068,0.068,0.068,0.068,0.068,0.068,0.068,0.067,0.067,0.067,0.068,0.067,0.067,0.067,0.068,0.068,0.068,0.068,0.069,0.068,0.068,0.068,0.068,0.068,0.068,0.068,0.067,0.068,0.068,0.067,0.067,0.067,0.068)

lowval = 0.028
hival = 0.079

t0 = as.POSIXct("2011-03-15 00:00:00") # 最初の時刻
t = seq(t0, by=3600, along.with=東京都)
# t = seq(t0, as.POSIXct("2011-03-17 00:00:00"), by=3600)
# 東京都 = 東京都[1:length(t)]
plot(NULL, type="o", pch=16, xaxt="n", xlab="", # col="#f39800",
     ylab="線量率（μSv/h）",
     xlim = range(t),
     ylim=range(c(0,東京都)))
# lines(t, 茨城県, type="o", pch=16, col="#0068b7")
# m = floor(length(東京都)*0.4)
# text(t[m], max(東京都[(m-5):(m+5)]), "東京都", pos=3) # pos=3が上，pos=1が下
# text(t[m], max(茨城県[(m-5):(m+5)]), "茨城県", pos=3)
r = as.POSIXct(round(range(t), "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")

# 過去の平常値の範囲
rect(t[1], lowval, t[length(t)], hival, col=gray(0.9), border=NA)

points(t, 東京都, type="l", pch=16)

m = floor(length(t)*0.25)
text(t[m], lowval, "過去の平常値の範囲", pos=1)

#---------------------------------------------------------------------

# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/mext.csv",
             header=FALSE, skip=4, fileEncoding="SJIS", nrows=47,
             as.is=TRUE, na.strings=c("","欠測"))

n = dim(X)[2]
t0 = as.POSIXct("2011-03-15 17:00:00") # 最初の時刻
t = seq(t0, by=3600, length.out=n-3)
山口 = as.numeric(X[X$V1[grepl("^山口", X$V2)],3:(n-1)])
宮城 = as.numeric(X[X$V1[grepl("^宮城", X$V2)],3:(n-1)])
t0 = as.POSIXct("2011-04-01 00:00:00")
山口 = 山口[t >= t0]
宮城 = 宮城[t >= t0]
t = t[t >= t0]
plot(t, 山口, type="o", pch=16, xaxt="n", xlab="", col="#f39800",
     ylab="線量率（μSv/h）", ylim=range(c(山口,宮城),na.rm=TRUE))
lines(t, 宮城, type="o", pch=16, col="#0068b7")
m = floor(length(東京都)*0.3)
text(t[m], max(山口[(m-5):(m+5)]), "山口", pos=3) # pos=3が上，pos=1が下
text(t[m], max(宮城[(m-5):(m+5)]), "宮城", pos=3)
r = as.POSIXct(round(range(t), "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")

for (i in seq(as.POSIXct("2011-04-01 00:00"), as.POSIXct("2011-04-17 00:00"), by="day")) {
  abline(v=i, lty=2)
}


abline(h=2400/365/24, lty=2)
m = floor(length(東京都)*0.2)
text(t[m], 2400/365/24, "世界平均2.4mSv/年", pos=3)

#---------------------------------------------------------------------

# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/mext.csv",
             header=FALSE, skip=4, fileEncoding="SJIS", nrows=47,
             as.is=TRUE, na.strings=c("","欠測"))

n = dim(X)[2]
t0 = as.POSIXct("2011-03-15 17:00:00") # 最初の時刻
t = seq(t0, by=3600, length.out=n-3)
plot(NULL, type="l", xaxt="n", xlab="",
     ylab="線量率（μSv/h）", log="y",
     xlim=range(t), ylim=range(X[,3:(n-1)], na.rm=TRUE))
# 山口県の過去の平常値の範囲
rect(t[1],0.084,t[n-3],0.128,col=gray(0.9),border=NA)
for (i in 1:47) {
  points(t, X[i,3:(n-1)], type="l", col=ifelse(i==13,"red","black"))
# points(t, X[i,3:(n-1)], type="l", col=ifelse(i==13,"red",ifelse(i==31,"blue","black")))
  j = n - 3
  while (j > 1 && is.na(X[i,j+2])) j = j - 1
  text(t[n-3], X[i,j+2], X[i,2], pos=4, cex=0.6, col=ifelse(i==13,"red","black"))
# text(t[n-3], X[i,j+2], X[i,2], pos=4, cex=0.6, col=ifelse(i==13,"red",ifelse(i==31,"blue","black")))
}
r = as.POSIXct(round(range(t), "days"))
# axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%d日")

m = floor(length(X[1,])*0.7)
text(t[m], 0.128, "灰色は山口県の過去の平常値の範囲", pos=1)

# abline(h=2400/365/24, lty=2)
# m = floor(length(X[1,])*0.8)
# text(t[m], 2400/365/24, "自然放射線の世界平均2.4mSv/年", pos=3)

#---------------------------------------------------------------------

# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/mext.csv",
             header=FALSE, skip=4, fileEncoding="SJIS", nrows=47, as.is=TRUE)

n = dim(X)[2]
t0 = as.POSIXct("2011-03-15 17:00:00") # 最初の時刻
t = seq(t0, by=3600, length.out=n-3)

t0 = as.POSIXct("2011-03-24 00:00:00")
t1 = t[t >= t0]
x = as.numeric(X[8,3:(n-1)]) # 茨城県
x1 = x[t >= t0]
y = as.numeric(X[13,3:(n-1)]) # 東京都
y1 = y[t >= t0]
plot(t1, x1, type="l", xaxt="n", xlab="", col="#f39800",
     ylab="線量率（μSv/h）", log="y")
r = as.POSIXct(round(range(t1), "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%d日")
u1 = 0.5^((as.numeric(t1)-as.numeric(t0))/(8.04*24*60*60))

coef = lm(x1 ~ u1)$coefficients
curve(coef[2] * 0.5^((x-as.numeric(t0))/(8.04*24*60*60)) + coef[1], add=TRUE)

#---------------------------------------------------------------------
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/mext.csv",
             header=FALSE, skip=4, fileEncoding="SJIS", nrows=47,
             as.is=TRUE, na.strings=c("","欠測"))

n = dim(X)[2]
t0 = as.POSIXct("2011-03-15 17:00:00") # 最初の時刻
t = seq(t0, by=3600, length.out=n-3)
Y = X[,3:(n-1)]
t0 = as.POSIXct("2011-04-11 00:00:00")
t1 = t[t >= t0]
Z = Y[,t >= t0]
# par(mar = c(5,4,4,2)+0.1)
par(mar = c(5,4,4,8)+0.1)
plot(NULL, type="l", xaxt="n", xlab="",
     ylab="線量率（μSv/h）", log="y",
     xlim=range(t1), ylim=range(Z, na.rm=TRUE))
for (i in 1:47) {
  points(t1, Z[i,], type="l", col=ifelse(i==13,"red","black"))
  text(t1[length(t1)], Z[i,length(t1)], X[i,2], pos=4, xpd=TRUE)
}
# r = as.POSIXct(round(range(t1), "days"))
r = as.POSIXct(round(range(t1), "hour"))
# axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
# axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%d日")
axis.POSIXct(1, at=seq(r[1],r[2],by="6 hour"), format="%d日%H時")

#---------------------------------------------------------------------
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

# write.csv(X, "utokyo.csv",
#           quote=FALSE, eol="\r\n", row.names=FALSE, na="")

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/utokyo.csv",
             header=TRUE, as.is=TRUE)
t = as.POSIXct(X$Time)
plot(t[!is.na(X[,5])], X[!is.na(X[,5]),5], pch=16, type="o", xaxt="n",
     ylim=range(c(0,X[,5]),na.rm=TRUE),
     xlab="", ylab="線量率（μSv/h）")
for (i in 2:4)
  points(t[!is.na(X[,i])], X[!is.na(X[,i]),i], pch=16, type="o", col=rainbow(3)[i-1])
r = as.POSIXct(round(range(t), "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")

t0 = as.POSIXct("2011/3/29 9:00")
text(t0, X[t==t0,2], "本郷1", pos=3)
text(t0, X[t==t0,3], "本郷2", pos=3)
text(t0, X[t==t0,4], "駒場", pos=1)
text(t0, X[t==t0,5], "柏", pos=3)
