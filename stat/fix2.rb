#! /usr/bin/env ruby
# coding: utf-8

ARGV.each do |file|
  buf = File.open(file, "r") do |f|
    f.read
  end
  x = buf
  x = x.gsub(%r|<!DOCTYPE html .*?>|, %q|<!DOCTYPE html>|)
  x = x.gsub(%r|<html xmlns.*?>|, %q|<html lang="ja">|)
  x = x.gsub(%r|<meta .*?charset=UTF-8".*/>|, %q|<meta charset="UTF-8">
<meta name="viewport" content="width=device-width">|)
  x = x.gsub(%r|<link rel="stylesheet".*?>|, %q|<link rel="stylesheet" href="style.css">|)
  x = x.gsub(%r|href="/~okumura/"|, %q|href="../"|)
  x = x.gsub(%r| rel="me">|, %q| rel="author">|)
  x = x.gsub(%r|<hr />|, %q|<hr>|)
  x = x.gsub(%r|<img (.*?) />|, %q|<img \1>|)
  if x != buf
    File.open(file, "w") do |f|
      f.write(x)
    end
  end
end
