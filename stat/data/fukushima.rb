#! /usr/bin/ruby -w
# -*- coding: utf-8 -*-

# http://www.tepco.co.jp/nu/monitoring/index-j.html
# で公開されている福島第一・第二原子力発電所の現状についてのPDFファイル
# をpdftotextでテキスト化したものをタブ区切りテキストに整形します。
# Usage: pdftotext -raw hoge.pdf - | fukushima.rb > x.txt
# x.txt をExcelで開いて確認してからマージしてください。

$KCODE = 'u'
require 'jcode'

def regularize(x)
  x.gsub!(/～/, '〜')    # U+FF5E (fullwidth tilde) to U+301C (wave dash)
  x.tr!('０-９', '0-9')  # 全角英数を半角英数に
  x.tr!('Ａ-Ｚ', 'A-Z')
  x.tr!('ａ-ｚ', 'a-z')
  x.gsub!(/．/, '.')     # 全角小数点
  x.gsub!(/－/, '-')     # 全角マイナス
  return x
end

foo = Array.new()
n = nil

while line = gets()
  line = regularize(line)
  a = line.split(nil)
  if a.size == 5
    t = "#{a[0]} #{a[1]}\t#{a[2]}\t#{a[3]}\t#{a[4]}"
  elsif a.size == 6
    t = a.join("\t")
  elsif a.size == 7
    t = "#{a[0]}\t#{a[1]}\t#{a[2]} #{a[3]}\t#{a[4]}\t#{a[5]}\t#{a[6]}"
  elsif a.size == 8
    t = "#{a[0]}\t#{a[1]}\t#{a[2]} #{a[3]}\t#{a[4]} #{a[5]}\t#{a[6]}\t#{a[7]}"
  else
    t = line
  end
  n = t.split("\t").size
  if n < 4
    puts foo.join("\n")
    foo = Array.new()
    puts t
  else
    foo.unshift(t)
  end
end
puts foo.join("\n")
