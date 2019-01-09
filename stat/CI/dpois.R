quartz(type="png", file="dpois.png", width=7, height=4, bg="white", family="HiraKakuProN-W3")
par(mgp=c(1.7,0.7,0)) # title and axis margins. default: c(3,1,0)
par(mar=c(2,2,2,2)) # bottom, left, top, right margins. default: c(5,4,4,2)+0.1
barplot(dpois(0:20,5), names.arg=c(sapply(seq(0,18,3), function(x){c(x,NA,NA)})),
        col=c("#ff9900", rep("#66ccff",10), rep("#ff9900",10)))
dev.off()
