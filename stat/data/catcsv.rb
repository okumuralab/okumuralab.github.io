#! /usr/bin/ruby -w
# -*- coding: japanese-cp932 -*-

$KCODE = 's'
require 'jcode'

lines = Array.new
header = nil

while line = gets()
  line.strip!
  if line =~ /^(Œv‘ªêŠ,)?(Date|Œv‘ª“ú),/
    header = line
  elsif line =~ /^\d/ || line =~ /^[^,]+,201\d/
    line.tr!('‚O-‚X', '0-9')
    line.tr!('‚`-‚y', 'A-Z')
    line.tr!('‚-‚š', 'a-z')
    line.gsub!(/D/, '.')
    line.gsub!(/C/, '.')
    line.gsub!(/|/, '-')
    line.gsub!(/"(\d+),(\d)"/, '\1.\2')
    line.gsub!(/\/(\d)\//, '/0\1/')
    line.gsub!(/\/(\d),/, '/0\1,')
    line.gsub!(/,(\d):/, ',0\1:')
    line.gsub!(/\.0+,/, ',')
    lines.push(line)
  end
end

if header =~ /^Œv‘ªêŠ/
  a = header.split(/,/, -1)
  a[0],a[1],a[2] = a[1],a[2],a[0]
  header = a.join(',')
  newlines = Array.new
  lines.each { |s|
    a = s.split(/,/, -1)
    if a[3] =~ /^([\d.]+) *nSv\/h/
      a[3] = $1.to_f * 0.001
    elsif a[3] =~ /^([\d.]+)/
      a[3] = $1
    end
    if a[4] =~ /^([\d.]+).*–¢–/
      a[4] = '<' + $1
    elsif a[4] =~ /^([\d.]+)/
      a[4] = $1
    end
    if a[0] =~ /^\d+\//
      a.insert(5, '-')
    else
      a[0],a[1],a[2] = a[1],a[2],a[0]
    end
    newlines.push(a.join(','))
  }
  lines = newlines
end

lines.sort!
lines.uniq!

print header, "\r\n"
n = header.split(/,/, -1).size
lines.each { |s|
  print s.split(/,/, -1)[0...n].join(','), "\r\n"
}
