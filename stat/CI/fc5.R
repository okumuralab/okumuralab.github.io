quartz(type="png", file="fc5.png", width=7, height=7, bg="white", family="HiraKakuProN-W3")
par(mgp=c(1.7,0.7,0)) # title and axis margins. default: c(3,1,0)
par(mar=c(3,3,2,2)) # bottom, left, top, right margins. default: c(5,4,4,2)+0.1
plot(NULL, xlim=c(0,10), ylim=c(0,10), xlab="x", ylab="lambda", xaxs="i", yaxs="i", asp=1)
abline(h=6.54)
for (lambda in seq(5,6.5,0.001)) {
    r = dpois(0:100, lambda) / dpois(0:100, c(5,5,5,5,5,5:100))
    o = order(r, decreasing=TRUE)
    t = sort(dpois(0:100, lambda), decreasing=TRUE)
    s = cumsum(dpois(0:100, lambda)[o])
    m = r[o[sum(s < 0.95) + 1]]
    x = range((0:100)[r >= m])
    segments(x[1], lambda, x[2], lambda, col="#66ccff")
}
for (lambda in seq(6.5,6.6,0.000001)) {
    r = dpois(0:100, lambda) / dpois(0:100, c(5,5,5,5,5,5:100))
    o = order(r, decreasing=TRUE)
    t = sort(dpois(0:100, lambda), decreasing=TRUE)
    s = cumsum(dpois(0:100, lambda)[o])
    m = r[o[sum(s < 0.95) + 1]]
    x = range((0:100)[r >= m])
    segments(x[1], lambda, x[2], lambda, col="#66ccff")
}
for (lambda in seq(6.6,10,0.001)) {
    r = dpois(0:100, lambda) / dpois(0:100, c(5,5,5,5,5,5:100))
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
axis(4, 6.54, labels=6.54)
dev.off()
