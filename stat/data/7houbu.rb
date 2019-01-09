#! /usr/bin/ruby -w
# -*- coding: utf-8 -*-

# http://www.pref.fukushima.jp/j/index.htm
# の「県内7方部　環境放射能測定結果」7houbuXX.pdf をCSVに変換
# pdftotext -raw 7houbuXX.pdf - | 7houbu.rb > 7houbu.csv

$KCODE = 'u'
# require 'jcode'
require 'iconv'

def hoge(x)
  if x.size == 1
    x = "0" + x
  end
  return x
end

print Iconv.conv("SJIS", "UTF-8", "日時,福島市,郡山市1,郡山市2,白河市,会津若松市,南会津町,南相馬市,いわき市平"), "\r\n"
while line = gets()
  line.gsub!(/－/, '-')
  if line =~ /^(\d)月(\d+)日/
    mon = hoge($1)
    day = hoge($2)
  end
  if line =~ /(\d+):(\d+) (.*)$/
    time = hoge($1) + ":" + hoge($2)
    data = $3
    a = data.split(nil)
    if a.size == 7
      a.insert(2, '-')
    end
    if a.size == 8
      print "2011-#{mon}-#{day} #{time},", a.join(","), "\r\n"
    end
  end
end
