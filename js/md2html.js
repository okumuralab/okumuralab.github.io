document.addEventListener('DOMContentLoaded', () => {

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
    .then(() => {
      const md = document.getElementById('md-content').innerText;
      // md = md.replace(/&lt;/g, '<').replace(/&gt;/g, '>');
      const html = marked.parse(md);
      // html = html.replace(/<\/body>[\s\S]*$/, '');
      document.body.innerHTML = html;
      document.querySelectorAll('pre > code.language-python').forEach(code => {
        code.parentElement.classList.add('cell');
      });
      // DEBUG:
      // const pre = document.createElement('pre');
      // document.body.appendChild(pre);
      // pre.innerText = html;
    })
    .then(() => {
      const pres = document.querySelectorAll('pre');
      function copyToClipboard(element) {
        const text = element.innerText;
        const tempTextArea = document.createElement("textarea");
        document.body.appendChild(tempTextArea);
        tempTextArea.value = text;
        tempTextArea.select();
        document.execCommand("copy");
        document.body.removeChild(tempTextArea);
      }
      pres.forEach(function(pre) {
        pre.addEventListener('click', function() {
          setTimeout(() => {
            if (window.getSelection().toString()) {
              return;
            }
            copyToClipboard(this);
          }, 100);
        });
        pre.setAttribute('title', 'Click to copy');
      });
    })
});
