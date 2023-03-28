var HOST = 'http://' + location.host+ '/'
lang_href = $("#language_dropdown").children("li").children('a')
lang = $('#dropdownMenuButton1').attr("value")

$("#language_dropdown").children("li").children('a').click(function(e){
    new_lang = $(this).attr('value')
    location_ =  window.location.href.replace(lang, new_lang)
    lang_href.attr("href", location_)
    console.log(location_)
})
