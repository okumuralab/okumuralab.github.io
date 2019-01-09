#! /usr/bin/ruby -w
# -*- coding: utf-8 -*-

# http://www.mext.go.jp/a_menu/saigaijohou/syousai/1303723.htm
# で公開されている都道府県別環境放射能水準調査結果PDFファイル
# をpdftotextでテキスト化したものをタブ区切りテキストに整形します。
# Usage: pdftotext -raw hoge.pdf - | mext.rb > x.txt
# x.txt をExcelで開いて確認してからマージしてください。

$KCODE = 'u'
# require 'jcode'

while line = gets()
  if line =~ /^\d+-\d+ \d+-\d+ /
    a = line.split(nil)
    a.insert(0, "")
    puts a.join("\t")
  elsif line =~ /^\d+ /
    line.gsub!(/～/, "〜")
    line.gsub!(/∼/, "〜")
    a = line.split(nil)
    puts a.join("\t")
  end
end
