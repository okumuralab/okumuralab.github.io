quartz(type="png", file="fc4.png", width=7, height=7, bg="white", family="HiraKakuProN-W3")
par(mgp=c(1.7,0.7,0)) # title and axis margins. default: c(3,1,0)
par(mar=c(3,3,2,2)) # bottom, left, top, right margins. default: c(5,4,4,2)+0.1
plot(NULL, xlim=c(0,10), ylim=c(0,10), xlab="x", ylab="lambda", xaxs="i", yaxs="i", asp=1)
for (lambda in seq(4,10,0.0001)) {
    r = dpois(0:100, lambda) / dpois(0:100, c(4,4,4,4,4:100))
    o = order(r, decreasing=TRUE)
    t = sort(dpois(0:100, lambda), decreasing=TRUE)
    s = cumsum(dpois(0:100, lambda)[o])
    m = r[o[sum(s < 0.95) + 1]]
    x = range((0:100)[r >= m])
    segments(x[1], lambda, x[2], lambda, col="#66ccff")
}
## abline(v=5)
## abline(h=3)
## abline(h=11.26)
## abline(h=6.54)
axis(4, 5.57, labels=5.57)
dev.off()
