
function add_pagination(data=null){
    pagination_container = $(".pagination")
    previous_page = pagination_container.find('#previous_page')
    next_page = pagination_container.find('#next_page')
    current = pagination_container.find('#current_page')
    current.html(1)

    if (data.previous){
        var prev_page_num = data.next.split('/').slice(-1)[0].match(/\d+/g)[0]
        previous_page.attr('value', prev_page_num)
    }
    if (data.next){
        var next_page_num = data.next.split('/').slice(-1)[0].match(/\d+/g)[0]
        next_page.attr('value', next_page_num)
    }


    // console.log(data.next, data.previous, data.count / 21)
}