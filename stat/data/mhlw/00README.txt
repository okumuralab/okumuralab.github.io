厚生労働省 http://www.mhlw.go.jp/ で公開されている「食品中の放射性物質の検査結果について（第*報）」をCSV化したもの（実験中）
ファイル名が数字で始まるものは旧フォーマット，aの付く数字のものは2012-04-01以降の新フォーマット（ヨウ素を含まない）です。
yasaikensa.csv は http://yasaikensa.cloudapp.net/ の3月末までのデータをCSV化したものです。

2r*.csv は http://www.mhlw.go.jp/stf/houdou/2r98520000029prx.html で公開されているExcelファイルをCSVにしたものです：
                                             総数  非ND >100
2r98520000029rve.csv 牛肉以外（H23.3-H24.3） 44327 14135 5012
2r98520000029ruw.csv 牛肉のみ（H23.3-H23.12）55526  5298 1023
2r98520000029rw2.csv 牛肉のみ（H24.1-H24.3） 33979   489   54

other = read.csv("2r98520000029rve.csv", as.is=TRUE)
niku1 = read.csv("2r98520000029ruw.csv", as.is=TRUE)
niku2 = read.csv("2r98520000029rw2.csv", as.is=TRUE)
foo = function(x) { ifelse(is.na(as.numeric(x)), 0, as.numeric(x)) }
othercs = foo(other[,17]) + foo(other[,18])
niku1cs = foo(niku1[,17]) + foo(niku1[,18])
niku2cs = foo(niku2[,17]) + foo(niku2[,18])
sum(othercs >= 0)
sum(othercs > 0)
sum(othercs > 100)
...

357報以降：
総数   非ND  >100
292592 24742 2461
all = read.csv("merged.csv", header=FALSE, as.is=TRUE)
all357 = all[all[,1] >= "357000000", ]
all357cs = as.numeric(all357[,19])
