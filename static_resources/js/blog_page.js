
// for marked js
document.getElementById('content').innerHTML =
  marked(document.getElementById('markdown_src').innerHTML);
// for google code pretty
$("code").addClass("prettyprint");