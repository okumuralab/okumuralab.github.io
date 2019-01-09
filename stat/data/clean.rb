#! /usr/bin/ruby -w
# -*- coding: utf-8 -*-

def isnum(x)
  return x =~ /^\d+(\.\d*)?$/
end

puts "desc,lat,lon,nni,μSv/h,datetime"
while line = gets()
  a = line.split(/,/)
  if isnum(a[1]) && isnum(a[2]) && isnum(a[3]) && a[3].to_f < 9900000 && isnum(a[4])
    date = "0000/00/00"
    time = "00:00:00"
    for j in 5...a.length do
      if a[j] =~ /^2011\/\d\d\/\d\d$/
        date = a[j]
      elsif a[j] =~ /^\d\d:\d\d:\d\d$/
        time = a[j]
      end
    end
    if date == "0000/00/00"
      if a[0] =~ /(2011\/\d\d\/\d\d)/
        date = $1
      end
    end
    puts "#{a[0]},#{a[1]},#{a[2]},#{a[3]},#{a[4]},#{date} #{time}"
  end
end
