document.addEventListener('DOMContentLoaded', () => {

  window.MathJax = {
    tex: { inlineMath: [['$', '$'], ['\\(', '\\)']] },
    svg: { fontCache: 'global' }
  };

  const loadScript = (src) => {
    return new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = src;
      script.async = false;
      script.onload = resolve;
      script.onerror = reject;
      document.head.appendChild(script);
    });
  };

  loadScript('https://cdn.jsdelivr.net/npm/marked/marked.min.js')
    .then(() => loadScript('https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js'))
    .then(() => {
      let md = document.body.innerHTML;
      md = md.replace(/\\/g, '\\\\').replace(/&lt;/g, '<').replace(/&gt;/g, '>');
      let html = marked.parse(md);
      html = html.replace(/<\/body>[\s\S]*$/, '');
      document.body.innerHTML = html;
      document.querySelectorAll('pre > code.language-python').forEach(code => {
        code.parentElement.classList.add('cell');
      });
      MathJax.typesetPromise();
      // DEBUG:
      // const pre = document.createElement('pre');
      // document.body.appendChild(pre);
      // pre.innerText = html;
    })
});
