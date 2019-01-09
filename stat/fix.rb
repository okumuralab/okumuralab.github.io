#! /usr/bin/ruby
# coding: utf-8

ARGV.each do |file|
  buf = File.open(file, "r") do |f|
    f.read
  end
  x = buf.sub(/<script src="http:\/\/cdn\.mathjax\.org\/mathjax\/latest\/MathJax\.js\?config=TeX-AMS_HTML">.*?<\/script>/m, %q!<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  CommonHTML: { matchFontHeight: false },
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    processEscapes: true
  }
});
</script>
<script async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML"></script>!)
  if x != buf
    File.open(file, "w") do |f|
      f.write(x)
    end
  end
end
