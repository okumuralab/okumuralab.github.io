東京電力 http://www.tepco.co.jp/ で公開されている福島第一・第二原子力発電所の放射線量率データは，手打ちPDFのようで，そのままでは機械可読ではないので，コピペと若干の自動処理でExcelおよびCSVファイルにしました。

元データには午前と午後や小数点とコンマの書き間違いがありますが，わかる範囲で修正してあります（Excelファイルで赤の個所）。

ガンマ線データの単位は，低線量ではnGy/h（ナノグレイ毎時），高線量ではμSv/h（マイクロシーベルト毎時）となっていますが，おそらくセンサが異なるための違いで，ガンマ線についてはGyとSvは同じものと考えてかまいません。μ（マイクロ）は百万分の1，n（ナノ）は10億分の1です。

新たに文科省の全国データ
http://www.mext.go.jp/a_menu/saigaijohou/syousai/1303723.htm
もExcel/CSV化しました（mext*）。

このデータを視覚化・解析しておられるかたがたのリスト：

  mickey24 さん
  福島原発のγ線量測定データをggplot2で可視化してみた - ぬいぐるみライフ(仮)
  http://d.hatena.ne.jp/mickey24/20110315/ggplot2

  hal9000000000 さん
  http://sky.geocities.jp/shigeharunumata/
  http://sky.geocities.jp/shigeharunumata/mext_mp.html

  koh_t さん
  http://d.hatena.ne.jp/koh-t/20110316/1300249024

  tbman2 さん
  http://goo.gl/3tQPF
  http://goo.gl/Kpdfh

  AkiraOkumura さん
  http://dl.dropbox.com/u/16653989/NuclPlants/index.html

  takscape さん（Pythonで整形・tsvに変換）
  http://static.void.in/rad/

  垂水先生＠岡山大
  都道府県別環境放射能水準調査 - PukiWiki
  http://face.f7.ems.okayama-u.ac.jp/~t2/pukiwiki/index.php?%C5%D4%C6%BB%C9%DC%B8%A9%CA%CC%B4%C4%B6%AD%CA%FC%BC%CD%C7%BD%BF%E5%BD%E0%C4%B4%BA%BA

  ryotat さん
  http://www.ibis.t.u-tokyo.ac.jp/RyotaTomioka/Softwares/Earthquake

  sugibuchi さん
  http://www-958.ibm.com/software/data/cognos/manyeyes/visualizations/radiation-sv-by-2hour-and-city-in-
  http://public.tableausoftware.com/views/RadiationlevelsinJapanSv2h15-18Mar2011/Sheet1?:embed=yes&:toolbar=yes&:tabs=no

  高橋さん
  http://mmm0311.cloudapp.net/

