quartz(type="png", file="pval.png", width=7, height=5, bg="white", family="HiraKakuProN-W3")
par(mgp=c(1.7,0.7,0)) # title and axis margins. default: c(3,1,0)
par(mar=c(3,3,2,2)) # bottom, left, top, right margins. default: c(5,4,4,2)+0.1
x = (1400:1500)/100
plot(x, sapply(x, function(x){poisson.test(7, r=x)$p.value}), type="p",
     xlab="lambda", ylab="p")
abline(v=14.3402)
abline(h=0.05)
dev.off()
