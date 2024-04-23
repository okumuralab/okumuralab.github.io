document.addEventListener('DOMContentLoaded', function() {
  const pres = document.querySelectorAll('pre');
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
});
function copyToClipboard(element) {
  const text = element.innerText;
  const tempTextArea = document.createElement("textarea");
  document.body.appendChild(tempTextArea);
  tempTextArea.value = text;
  tempTextArea.select();
  document.execCommand("copy");
  document.body.removeChild(tempTextArea);
}
