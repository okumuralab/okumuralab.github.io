#! /usr/bin/ruby -w
# -*- coding: utf-8 -*-

# http://www.pref.fukushima.jp/j/index.htm
# の「20km〜50km圏付近環境放射能測定結果」20-50kmXX.pdf をCSVに変換
# pdftotext -raw 20-50kmXX.pdf - | 20-50km.rb > 20-50km.csv

$KCODE = 'u'
# require 'jcode'
require 'iconv'

def hoge(x)
  if x.size == 1
    x = "0" + x
  end
  return x
end

print Iconv.conv("SJIS", "UTF-8", "日時,伊達市役所,二本松市役所,川俣町山木屋郵便局,川俣町山木屋駐在所,田村市役所,田村市常葉行政局,福島空港,横川ダム,平野町役場,川内村役場,浪江町津島支所,葛尾村柏原地区,飯舘村役場,飯舘村長泥,いわき市川前支所"), "\r\n"
while line = gets()
  line.gsub!(/－/, '-')
  if line =~ /^(\d)月(\d+)日/
    mon = hoge($1)
    day = hoge($2)
  elsif line =~ /^0:00/
    day = hoge(day.to_i + 1)
  end
  if line =~ /(\d+):(\d+) (.*)$/
    time = hoge($1) + ":" + hoge($2)
    data = $3
    data.gsub!(/\*/, '')
    a = data.split(nil)
    if a.size < 15
      a.insert(7, '-')
    end
    if a.size < 15
      a.insert(3, '-')
    end
    if a.size < 15
      a.insert(10, '-', '-')
    end
    while a.size < 15
      a.push('-')
    end
    print "2011-#{mon}-#{day} #{time},", a.join(","), "\r\n"
  end
end
