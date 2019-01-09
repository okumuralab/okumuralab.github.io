#---------------------------------------------------------------------
# 福島第一原発放射線量観測データ
# http://www.pref.fukushima.jp/j/schoolmonitamatome.pdf
# https://spreadsheets0.google.com/ccc?authkey=CNar_6sP&key=tSc4EaYnOD5AD8fW3yHugKg&authkey=CNar_6sP#gid=61
# 上をCSVで保存したものを schools.csv とする

#---------------------------------------------------------------------
# 市町村の頭1文字でプロット
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

schools = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/schools.csv",
                   skip=2, header=TRUE, as.is=TRUE, na.strings="-")

plot(schools$X1cm高さ, schools$X1m高さ, # pch=schools$市町村,
     xlab="μSv/h＠1cm", ylab="μSv/h＠1m", asp=1)

abline(h=3.8, col="gray")

#---------------------------------------------------------------------
# 特に多い3自治体だけ
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))
o = order(schools$X1m高さ, decreasing=TRUE)
head(schools[o,c(1,4,6,7)], 20)
foo = c("浪江町", "飯舘村", "川俣町")
plot(schools$X1m高さ[is.element(schools$市町村, foo)],
     schools$X1cm高さ[is.element(schools$市町村, foo)],
     pch=schools$市町村[is.element(schools$市町村, foo)],
     xlab="μSv/h＠1m", ylab="μSv/h＠1cm")

#---------------------------------------------------------------------
# 福島市
# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

福島市 = schools[schools$市町村 == "福島市",]

plot(jitter(福島市$X1cm高さ,amount=0.02), jitter(福島市$X1m高さ,amount=0.02),
     xlim=range(c(0,福島市$X1cm高さ),na.rm=TRUE),
     ylim=range(c(0,福島市$X1m高さ),na.rm=TRUE),
     xlab="μSv/h＠1cm", ylab="μSv/h＠1m", asp=1)

#---------------------------------------------------------------------
# 単純なヒストグラム
# par(family="HiraKakuProN-W3") # Mac専用
# par(mar = c(5,4,4,2)+0.1)
par(mgp=c(2,0.8,0))

schools = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/schools.csv",
                   skip=2, header=TRUE, as.is=TRUE, na.strings="-")
x = schools$X1m高さ
hist(x, col="#f39800", breaks=100, right=FALSE,
     xlim=range(0,x,na.rm=TRUE),
     xlab="μSv/h＠1m", ylab="学校数", main="福島県の学校の校庭の空間線量率の度数分布")
# abline(v=1000/365/24, col="red")
# text(1000/365/24, 200, "1mSv/年", srt=90, pos=3)
# abline(v=20000/365/24, col="red")
# text(20000/365/24, 200, "20mSv/年", srt=90, pos=3)
abline(v=3.8, col="red")
text(3.8, 270, "3.8μSv/h", # srt=90, pos=3,
     xpd=NA)
abline(v=3.8/2, col="red")
text(3.8/2, 290, "(3.8/2)μSv/h", # srt=90, pos=3,
     xpd=NA)
abline(v=3.8/20, col="red")
text(3.8/20, 310, "(3.8/20)μSv/h", # srt=90, pos=3,
     xpd=NA)
