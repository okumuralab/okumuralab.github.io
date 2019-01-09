# 国立がん研究センター東病院（千葉県柏市）敷地内における放射線の測定結果
# http://www.ncc.go.jp/jp/information/sokutei_ncce.html

# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

X = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/ncc-kashiwa.csv",
             comment.char="#")
t = as.POSIXct(X[,1])
plot(NULL, xlim=range(t), ylim=range(c(0,X[,4:6]),na.rm=TRUE),
     xlab="", ylab="線量率（μSv/h）", xaxt="n")
for (i in 1:3) {
  points(t, X[,i+3], type="b", pch=i)
}
r = as.POSIXct(round(range(t), "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%b月%d日")
tm = as.POSIXct("2011-03-31")
text(tm, X[t == tm,4], "屋内1", pos=1)
text(tm, X[t == tm,5], "屋外A", pos=1)
text(tm, X[t == tm,6], "屋外B", pos=1)
