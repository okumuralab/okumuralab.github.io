# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/mext.csv",
             header=FALSE, skip=4, fileEncoding="SJIS", nrows=47,
             as.is=TRUE, na.strings=c("","0.000","欠測"))

n = dim(X)[2]
lowval = as.numeric(sub("([0-9.]+).*", "\\1", X[,n]))
hival = as.numeric(sub("[0-9.]+〜([0-9.]+)", "\\1", X[,n]))

# t0 = as.POSIXct("2011-03-15 17:00") # 最初の時刻
t0 = as.POSIXct("2011-03-11 00:00") # 最初の時刻
t = seq(t0, by=3600, length.out=n-3)
plot(range(t), range(X[,3:(n-1)], na.rm=TRUE),
     log="y",
     type="n", xaxt="n", xlab="", ylab="線量率（μSv/h）")

# 山口県の過去の平常値の範囲
rect(t[1], lowval[35], t[n-3], hival[35], col=gray(0.9), border=NA)

for (i in 1:47) {
  points(t, X[i,3:(n-1)], type="l")
  j = n - 3
  while (j > 1 && is.na(X[i,j+2])) j = j - 1
  text(t[n-3], X[i,j+2], substr(X[i,2],1,2), pos=4, offset=0.1, cex=0.6)
}
r = as.POSIXct(round(range(t), "days"))
# axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%d日")

m = floor(length(X[1,])*0.35)
text(t[m], 0.128, "灰色は山口県の過去の平常値の範囲", pos=1)

# abline(h=2400/365/24, lty=2)
# m = floor(length(X[1,])*0.8)
# text(t[m], 2400/365/24, "自然放射線の世界平均2.4mSv/年", pos=3)

#---------------------------------------------------------------------
# 特定の県だけ
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/mext.csv",
             header=FALSE, skip=4, fileEncoding="SJIS", nrows=47,
             as.is=TRUE, na.strings=c("","0.000","欠測"))

n = dim(X)[2]
lowval = as.numeric(sub("([0-9.]+).*", "\\1", X[,n]))
hival = as.numeric(sub("[0-9.]+〜([0-9.]+)", "\\1", X[,n]))

# t0 = as.POSIXct("2011-03-12 17:00:00") # 最初の時刻
t0 = as.POSIXct("2011-03-11 00:00") # 最初の時刻
t = seq(t0, by=3600, length.out=n-3)

# ken = 11 # 埼玉
# ken = 13 # 東京
ken = 24 # 三重県
x = X[ken,3:(n-1)]

ts = t0
# ts = as.POSIXct("2011-05-01 00:00:00") # 最初の時刻
# ts = as.POSIXct("2011-03-11 00:00:00") # 最初の時刻
ts = as.POSIXct("2011-06-15 00:00:00") # 最初の時刻
t1 = t[t >= ts]
x1 = x[t >= ts]

plot(range(t1), range(c(x1,lowval[ken],hival[ken]),na.rm=TRUE),
     ylab="線量率（μSv/h）", # log="y",
     type="n", xaxt="n", xlab="")

# 過去の平常値の範囲
rect(t1[1], lowval[ken], t1[length(t1)], hival[ken], col=gray(0.9), border=NA)

points(t1, x1, type="l")

r = as.POSIXct(round(range(t1), "days"))
# axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%m/%d")

n = length(x1)
text(t1[n], x1[n], x1[n], pos=1, offset=1, cex=0.8)
text(t1[1], x1[1], x1[1], pos=1, offset=1, cex=0.8)

# m = floor(length(x1)*0.25)
# text(t1[m], hival[ken], "過去の平常値の範囲", pos=1)

#---------------------------------------------------------------------
# まともなCSVに変換（未完）

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/mext.csv",
             header=FALSE, skip=4, fileEncoding="SJIS", nrows=47,
             as.is=TRUE, na.strings=c("","0.000","欠測"))

n = dim(X)[2]
# t0 = as.POSIXct("2011-03-12 17:00:00") # 最初の時刻
t0 = as.POSIXct("2011-03-11 00:00") # 最初の時刻
t = seq(t0, by=3600, length.out=n-3)
x = data.frame(X[,3:(n-1)], row.names=X[,2])
Xt = data.frame(DateTime=t, t(x))
write.csv(Xt, "prefs.csv", row.names=FALSE)

#---------------------------------------------------------------------
# http://mextrad2.cloudapp.net/csvdata.aspx から取得したCSVの処理（未完）
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

prefs = read.csv("....csv", skip=1, as.is=TRUE)

n = dim(prefs)[1]
pdata = matrix(nrow=24*n/47, ncol=47)
ptime = rep(as.POSIXct(NA), 24*n/47)
pname = character(47)
ppos = character(47)
pmin = rep(as.numeric(NA), 47)
pmax = rep(as.numeric(NA), 47)
pcnt = rep(0, 47)

k = 0
for (i in 1:n) {
  p = prefs[i,1]
  pname[p] = prefs[i,2]
  ppos[p] = prefs[i,3]
  pmin[p] = prefs[i,4]
  pmax[p] = prefs[i,5]
  t = as.POSIXct(prefs[i,6])
  for (j in 7:30) {
    pcnt[p] = pcnt[p] + 1
    pdata[pcnt[p],p] = prefs[i,j]
    ptime[pcnt[p]] = t
    t = t + 3600
  }
}
