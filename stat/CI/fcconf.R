if (file.exists("fcconf.csv")) {
    data = read.csv("fcconf.csv")
    attach(data)
} else {
    fcconf = function(x, b) {
        ret = c(100, 0)
        for (lambda in seq(b,10,0.001)) {
            r = dpois(0:100, lambda) / dpois(0:100, pmax(b,0:100))
            o = order(r, decreasing=TRUE)
            t = sort(dpois(0:100, lambda), decreasing=TRUE)
            s = cumsum(dpois(0:100, lambda)[o])
            m = r[o[sum(s < 0.95) + 1]]
            if (x %in% (0:100)[r >= m]) {
                ret[1] = min(ret[1], lambda-b)
                ret[2] = max(ret[2], lambda-b)
            }
        }
        ret
    }
    b = (0:500)/100
    lambda2 = sapply(b, function(x){fcconf(0,x)})[2,]
    write.csv(data.frame(b,lambda2), "fcconf.csv", row.names=FALSE)
}
quartz(type="png", file="fcconf.png", width=7, height=5, bg="white", family="HiraKakuProN-W3")
par(mgp=c(1.7,0.7,0)) # title and axis margins. default: c(3,1,0)
par(mar=c(3,3,2,2)) # bottom, left, top, right margins. default: c(5,4,4,2)+0.1
plot(b, lambda2, xlab="b", ylab="lambda2 - b", type="l")
dev.off()
