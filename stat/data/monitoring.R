# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/monitoring.csv",
             comment.char="#")
X = read.csv("~/public_html/stat/data/monitoring.csv",
             comment.char="#")
t = as.POSIXct(X[,1])
plot(NULL, xlim=range(t), ylim=range(X[,2:4],na.rm=TRUE),
     xlab="", ylab="線量率（μSv/h）", xaxt="n", yaxt="n", log="y")
cols = c("#f39800", "#0068b7", "#000000")
for (i in 1:3) {
  points(t, X[,i+1], type="o", pch=16, col=cols[i])
}
r = as.POSIXct(round(range(c(as.POSIXct("2011-03-11 00:00"), t)), "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="6 hours"), format="%d日%H時")
tx = c(0.1,1,10,100,1000,10000)
axis(2, at=tx, labels=format(tx,scientific=FALSE,drop0trailing=TRUE))

tm = as.POSIXct("2011-03-31")
text(tm, X[t == tm,4], "屋内1", pos=1)
text(tm, X[t == tm,5], "屋外A", pos=1)
text(tm, X[t == tm,6], "屋外B", pos=1)
