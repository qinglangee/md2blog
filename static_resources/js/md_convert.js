
// for marked js
$(".markdown_box").each(function(){
    var markdown = $(this).find(".markdown_src").text();
    markdown = markdown.replace(/&lt;/g, "<")
    markdown = markdown.replace(/&gt;/g, ">")
    $(this).html(marked(markdown));
});
// for google code pretty
$("code").addClass("prettyprint");