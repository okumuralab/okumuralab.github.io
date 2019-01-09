# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))
library(nlme)

X = read.csv("/var/www/html/rad/atommoc.csv", fileEncoding="SJIS", as.is=TRUE)

pos = "大野"
# pos = "浪江"
pp = pos == X[,2]
t = as.POSIXct(X[pp,1])
x = X[pp,3]
ts = as.POSIXct("2011-03-24 00:00:00")
t1 = t[t >= ts]
x1 = x[t >= ts]
xrange = range(t1)
# yrange = range(x1)
yrange = range(c(0,x1))
plot(t1, x1, xaxt="n", xlab="", ylab="Radiation Level (nGy/h)",
     type="l", col="#f39800", xlim=xrange, ylim=yrange)
r = as.POSIXct(round(xrange, "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="month"), format="%m/%d")

tt = as.numeric(t1)-as.numeric(t1[1])
data = data.frame(t=tt, y=x1)
fit = gnls(y ~ c + e*0.5^(t/(d*24*60*60)), data=data,
          start=list(c=6100,e=1150,d=61),  # 大野
#          start=list(c=1100,e=100,d=71),  # 浪江
           weights=varPower(fixed=0.5),
           control=list(nlsTol=1e-3))
a = coef(fit)
yrange = range(c(a['c'],x1))
plot(t1, x1, xaxt="n", xlab="", ylab="Radiation Level (nGy/h)",
     type="l", col="#f39800", xlim=xrange, ylim=yrange)
r = as.POSIXct(round(xrange, "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="month"), format="%m/%d")
curve(a['c'] + a['e'] * 0.5^((x-as.numeric(t1[1]))/(a['d']*24*60*60)), add=TRUE)
abline(h=a['c'], lty=2)

## makegraph("大野", 7, 400, 300, "oono.png")
## makegraph("富岡", 7, 400, 300, "tomioka.png")
## makegraph("松館", 7, 400, 300, "matsudate.png")
## makegraph("繁岡", 7, 400, 300, "shigeoka.png")
## makegraph("紅葉山", 7, 400, 300, "momijiyama.png")
## makegraph("浪江", 7, 400, 300, "namie.png")
## makegraph("二ツ沼", 7, 400, 300, "futatsunuma.png")
## makegraph("幾世橋", 7, 400, 300, "kiyohashi.png")
## makegraph("山田岡", 7, 400, 300, "yamadaoka.png")
## makegraph("上郡山", 7, 400, 300, "kamikooriyama.png")
## makegraph("下郡山", 7, 400, 300, "shimokooriyama.png")
## makegraph("夜ノ森", 7, 400, 300, "yonomori.png")
## makegraph("山田", 7, 400, 300, "yamada.png")
## makegraph("新山", 7, 400, 300, "shinzan.png")
## makegraph("郡山", 7, 400, 300, "kooriyama.png")
