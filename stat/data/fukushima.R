# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

microSv = function(x) {
  as.numeric(sub("([0-9.]+).*", "\\1", x)) * ifelse(grepl("nGy/h", x), 0.001, 1)
}

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/fukushima1.csv",
             header=TRUE, skip=1, fileEncoding="SJIS", as.is=TRUE)

for (i in 2:length(X$計測日)) {
  if (X$計測日[i] == "") X$計測日[i] = X$計測日[i-1]
}
gammaray = microSv(X$γ線)
日時 = as.POSIXct(sub("^\\D*(\\d+)\\D+(\\d+)\\D+(\\d+)\\D+(\\d+)",
                      "2011-\\1-\\2 \\3:\\4",
                      paste(X$計測日,X$計測時間),
                      perl=TRUE)) + ifelse(grepl("午後", X$計測時間), 12*3600, 0)
# t0 = as.POSIXct("2011-03-11 17:30:00")
# t0 = as.POSIXct("2011-03-19 03:00:00")
t0 = as.POSIXct("2011-04-10 00:00:00")
t1 = 日時[X$計測場所 == "西門" & 日時 >= t0]
x1 = gammaray[X$計測場所 == "西門" & 日時 >= t0]
t2 = 日時[X$計測場所 == "正門" & 日時 >= t0]
x2 = gammaray[X$計測場所 == "正門" & 日時 >= t0]
plot(t1, x1, type="o", pch=16, ylab="線量率（μSv/h）", xaxt="n", xlab="", # log="y",
     xlim=range(c(t1,t2)), ylim=range(c(x1,x2)), col="#f39800")
points(t2, x2, type="o", pch=16, col="#0068b7")
# r = as.POSIXct(round(range(c(t1,t2)), "days"))
r = as.POSIXct(round(range(c(t1,t2)), "hours"))
# axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
axis.POSIXct(1, at=seq(r[1],r[2],by="hour"), format="%d日%H時")

#---------------------------------------------------------------------
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/fukushima2.csv",
             header=TRUE, skip=1, fileEncoding="SJIS", as.is=TRUE)

for (i in 2:length(X$計測日)) {
  if (X$計測日[i] == "") X$計測日[i] = X$計測日[i-1]
}
gammaray = microSv(X$γ線)
日時 = as.POSIXct(sub("^\\D*(\\d+)\\D+(\\d+)\\D+(\\d+)\\D+(\\d+)",
                      "2011-\\1-\\2 \\3:\\4",
                      paste(X$計測日,X$計測時間),
                      perl=TRUE)) + ifelse(grepl("午後", X$計測時間), 12*3600, 0)
t0 = as.POSIXct("2011-03-25 00:00:00")
t = 日時[X$計測場所 == "MP-4付近" & 日時 >= t0]
x = gammaray[X$計測場所 == "MP-4付近" & 日時 >= t0]
plot(t, x, type="o", pch=16, ylab="線量率（μSv/h）",
     xaxt="n", xlab="", col="#0068b7")
r = as.POSIXct(round(range(t), "hours"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
# axis.POSIXct(1, at=seq(r[1],r[2],by="hour"), format="%d日%H時")

#---------------------------------------------------------------------
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

microSv = function(x) {
  as.numeric(sub("([0-9.]+).*", "\\1", x)) * ifelse(grepl("nGy/h", x), 0.001, 1)
}

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/fukushima1.csv",
             header=TRUE, skip=1, fileEncoding="SJIS", as.is=TRUE)

for (i in 2:length(X$計測日)) {
  if (X$計測日[i] == "") X$計測日[i] = X$計測日[i-1]
}
gammaray = microSv(X$γ線)
日時 = as.POSIXct(sub("^\\D*(\\d+)\\D+(\\d+)\\D+(\\d+)\\D+(\\d+)",
                      "2011-\\1-\\2 \\3:\\4",
                      paste(X$計測日,X$計測時間),
                      perl=TRUE)) + ifelse(grepl("午後", X$計測時間), 12*3600, 0)
t0 = as.POSIXct("2011-03-26 11:20:00")
t0 = as.POSIXct("2011-10-07 00:00:00")
t1 = 日時[X$計測場所 == "西門" & 日時 >= t0]
x1 = gammaray[X$計測場所 == "西門" & 日時 >= t0]
plot(t1, x1, type="o", pch=16, ylab="線量率（μSv/h）", xaxt="n", xlab="",
     col="#f39800", log="y")
r = as.POSIXct(round(range(t1), "hours"))
axis.POSIXct(1, at=seq(r[1],r[2],by="hours"), format="%d日%H時")

coef = lm(log2(x1) ~ t1)$coefficients
curve(2^(coef[2]*x+coef[1]), add=TRUE)
(1/coef[2])/(60*60*24)

# t00 = as.POSIXct("2011-03-28 10:00:00")
# t10 = 日時[X$計測場所 == "西門" & 日時 >= t00]
# x10 = gammaray[X$計測場所 == "西門" & 日時 >= t00]
# coef = lm(log2(x10) ~ t10)$coefficients
# curve(2^(coef[2]*x+coef[1]), from=as.numeric(t00), to=as.numeric(max(t1)), add=TRUE)
# coef = lm(log2(x1) ~ t1)$coefficients
# curve(2^(coef[2]*x+coef[1]), add=TRUE)
# (1/coef[2])/(60*60*24)
# 半減期8日の直線を引く
ybar = mean(log2(x1))
xbar = mean(as.numeric(t1))
curve(2^(ybar-(x-xbar)/(8*60*60*24)), add=TRUE)


#---------------------------------------------------------------------
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/fukushima1MP.csv",
             header=TRUE, skip=1, fileEncoding="SJIS", as.is=TRUE,
             col.names=c("日時","事務本館南側","正門","西門"),
             na.strings=c("故障につき欠測中","欠測"))
X$事務本館南側 = 1000 * X$事務本館南側 # μSv/hに統一
t = as.POSIXct(X$日時)
t0 = as.POSIXct("2011-04-07 00:00:00")
事務本館南側 = X$事務本館南側[t >= t0]
正門 = X$正門[t >= t0]
西門 = X$西門[t >= t0]
t = t[t >= t0]
plot(NULL, xaxt="n", log="y", xlab="", ylab="線量率（μSv/h）",
     xlim=range(t), ylim=range(c(事務本館南側 # ,正門,西門
                                ),na.rm=TRUE))
points(t, 事務本館南側, type="o", pch=16)
# points(t, 正門, type="o", pch=16, col="#0068b7")
# points(t, 西門, type="o", pch=16, col="#f39800")
r = as.POSIXct(round(range(t), "hours"))
axis.POSIXct(1, at=seq(r[1],r[2],by="12 hours"), format="%d日%H時")
m = floor(length(t)*0.1)
text(t[m], min(事務本館南側[1:(2*m)]), "事務本館南側", pos=1) # pos=3が上，pos=1が下
text(t[m], min(正門[1:(2*m)]), "正門", pos=1) # pos=3が上，pos=1が下
text(t[m], min(西門[1:(2*m)]), "西門", pos=1) # pos=3が上，pos=1が下
# coef = lm(log2(正門) ~ t)$coefficients
# curve(2^(coef[2]*x+coef[1]), add=TRUE)
# (1/coef[2])/(60*60*24)
# 半減期8日の直線を引く
ybar = mean(log2(c(事務本館南側,正門,西門)))
xbar = mean(as.numeric(t))
curve(2^(ybar-(x-xbar)/(8*60*60*24)), add=TRUE)

