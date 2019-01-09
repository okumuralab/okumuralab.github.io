CSV = 349.csv 350.csv 351.csv 352.csv 353.csv 354.csv 355.csv 356.csv \
      a357.csv 357.csv a358.csv 358.csv a359.csv 359.csv a360.csv 360.csv \
      a361.csv 361.csv a362.csv a363.csv a364.csv a365.csv a366.csv a367.csv \
      a368.csv a369.csv a370.csv a371.csv a372.csv a373.csv a374.csv 374.csv \
      a375.csv a376.csv a377.csv a378.csv a379.csv a38?.csv a390.csv 390.csv \
      a39[1-5].csv 395.csv a39[6-9].csv a400.csv 400.csv a40[1-9].csv a410.csv 410.csv \
      a41[1-9].csv a4[2-9]?.csv a[5-9]??.csv

all:
	./merge.rb $(CSV) >xxxx.csv
	mv -f xxxx.csv merged.csv
	tac merged.csv >xxxx.csv
	mv -f xxxx.csv reversed.csv
	gzip -c -9 merged.csv >merged.csv.gz
	gzip -c -9 reversed.csv >reversed.csv.gz
