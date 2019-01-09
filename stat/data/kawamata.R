# http://www.town.kawamata.lg.jp/sokuhou/?p=478
# pdftotext -raw fileopen1.pdf - >kawamata.txt

# par(family="HiraKakuProN-W3") # Mac専用
par(mgp=c(2,0.8,0))

cnt = 0
tim = as.POSIXct(vector())
pla = numeric()
val = numeric()
t = rep(as.POSIXct("2011-06-04"),25)
txt = readLines("kawamata.txt")
for (i in 1:length(txt)) {
  if (!grepl("^\\d+ ", txt[i])) next
  a = strsplit(txt[i], " ")[[1]]
  k = as.numeric(a[1])
  if (k < 1 || k > 25) next
  j = length(a)
  while (j > 4) {
    t[k] = as.POSIXct(paste(substr(as.character(t[k]-24*60*60), 1, 10), a[j-1]))
    cnt = cnt + 1
    tim[cnt] = t[k]
    pla[cnt] = k
    val[cnt] = as.numeric(a[j])
    j = j - 2
  }
}

plot(range(tim,na.rm=TRUE), range(val,na.rm=TRUE), type="n",
     xaxt="n", xlab="", ylab="線量率（μSv/h）", log="y")

for (k in c(1,3:25,2)) {
  t1 = tim[pla == k]
  x1 = val[pla == k]
  points(t1, x1, type="o", pch=k, col=ifelse(k==2,"red","black"))
}

r = as.POSIXct(round(range(c(tim),na.rm=TRUE), "days"))
axis.POSIXct(1, at=seq(r[1],r[2],by="day"), format="%m/%d")
