#! /usr/bin/ruby
# -*- coding: utf-8 -*-

n = 0
fprev = ""
while line = gets()
  line.strip!
  f = File.basename($FILENAME, ".*")
  newformat = (f =~ /^a/)
  f.gsub!(/^a/, '')
  if f != fprev
    n = 0
    fprev = f
  end
  a = line.split(/,/)
  next if a[0].to_i == 0
  if a[0].to_i == 1
    n = n + 1
  end
  a[0] = f + sprintf("%02d", n) + sprintf("%04d", a[0].to_i)
  if newformat
    a.insert(3, '-') # 部局
    a.insert(15, '-') # I131
  else
    a[6],a[7] = a[7],a[6]
    a.insert(10, '-') # 品目_その他
    a << ((a[16] =~ /^[^\d]/ && a[17] =~ /^[^\d]/) ? '<' : '') + (a[16].gsub(/</,'').to_f + a[17].gsub(/</,'').to_f).to_s.gsub(/\.0$/,'')
  end
  puts a.join(",") # 0..18
end
