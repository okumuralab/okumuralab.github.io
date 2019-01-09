<?php
function tex($x) {
  $t = md5($x);
  if (!file_exists("mathimg/$t.png")) {
    $f = fopen("mathimg/$t.tex", "w");
    fwrite($f, "\\documentclass{article}\n\\usepackage{mathptmx,amsmath,amssymb}\n\\pagestyle{empty}\n\\begin{document}\n$x\n\\end{document}\n");
    fclose($f);
    system("HOME=/tmp; ulimit -t 10 -f 1024 -c 0; cd mathimg; /usr/local/texlive/p2009/bin/x86_64-unknown-linux-gnu/latex -interaction=nonstopmode $t.tex >/dev/null 2>&1 && /usr/local/texlive/2009/bin/x86_64-linux/dvipng -q -D 144 -T tight -pp 1 $t.dvi -o $t.png >/dev/null 2>&1", $retval);
    if ($retval) die("Error");
  }
  echo "<img src=\"mathimg/$t.png\" alt=\"$x\" style=\"vertical-align:middle\" />";
}
?>
