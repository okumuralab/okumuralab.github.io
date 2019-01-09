quartz()
par(family="HiraKakuProN-W3")
leu = read.csv("http://oku.edu.mie-u.ac.jp/~okumura/stat/data/leukemia.csv",
               as.is=TRUE, comment.char="#")
par(mgp=c(2,0.8,0))
par(las=1)
plot(NULL, xlim=c(1,12), ylim=range(leu[,2])*c(0.95,1.05), xaxt="n", xlab="月", ylab="")
axis(1, 1:12, 1:12)
points(leu[1:12,2], type="b", pch="8")
points(leu[13:24,2], type="b", pch="9")
points(leu[25:36,2], type="b", pch="0")
points(leu[37:47,2], type="b", pch="1")
title(main="2008-2011年の月ごとの白血病による死亡数", line=1)

