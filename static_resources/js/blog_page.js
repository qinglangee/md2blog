
// for marked js
var markdown = document.getElementById('markdown_src').innerHTML;
markdown = markdown.replace(/&lt;/g, "<")
markdown = markdown.replace(/&gt;/g, ">")
document.getElementById('content').innerHTML = marked(markdown);
// for google code pretty
$("code").addClass("prettyprint");