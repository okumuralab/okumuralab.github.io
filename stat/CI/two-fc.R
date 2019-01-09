quartz(type="png", file="two-fc.png", width=7, height=7, bg="white", family="HiraKakuProN-W3")
par(mgp=c(1.7,0.7,0)) # title and axis margins. default: c(3,1,0)
par(mar=c(3,3,2,2)) # bottom, left, top, right margins. default: c(5,4,4,2)+0.1
plot(NULL, xlim=c(0,20), ylim=c(0,20), xlab="x", ylab="lambda", xaxs="i", yaxs="i", asp=1)
for (lambda in seq(0,20,0.1)) {
    t = sort(dpois(0:100, lambda), decreasing=TRUE)
    s = cumsum(t)
    m = t[sum(s < 0.95) + 1]
    x = range((0:100)[dpois(0:100, lambda) >= m])
    segments(x[1], lambda, x[2], lambda, col="#66ccff")
}
for (lambda in seq(0,20,0.1)) {
    r = dpois(0:100, lambda) / dpois(0:100, 0:100)
    o = order(r, decreasing=TRUE)
    t = sort(dpois(0:100, lambda), decreasing=TRUE)
    s = cumsum(dpois(0:100, lambda)[o])
    m = r[o[sum(s < 0.95) + 1]]
    x = range((0:100)[r >= m])
    segments(x[1], lambda+0.05, x[2], lambda+0.05, col="#ff99a0")
}
dev.off()
