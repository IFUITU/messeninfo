
function make_buttons(){
    var letters = ['All','0-9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for(i = 0; i < letters.length; i++) {
        var button = document.createElement("button");
        button.innerHTML = letters[i];
        button.className = "btn btn-success btn-sm mx-1";
        button.id = letters[i]
        var buttonDiv = document.getElementById("filter_buttons");
        buttonDiv.appendChild(button);
    }
}


function append_result(res=null){
    let row_container = $("#row_container")
    row_container.empty()
    
    if(res != null){
        if(res.results.length == 0){
            row_container.append(`<h1>Nothing found!</h1>`)
        }else{
            res.results.forEach(function callback(currentValue, index, array) {
                html_data = `<div class="col-lg-3 col-md-12 mb-4">
                                <div class="card">
                                    <div class="bg-image hover-zoom ripple ripple-surface ripple-surface-light"
                                    data-mdb-ripple-color="light">
                                    <img src="https://mdbcdn.b-cdn.net/img/Photos/Horizontal/E-commerce/Products/belt.webp"
                                        class="w-100" />
                                    <a href="#!">
                                        <div class="hover-overlay">
                                        <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
                                        </div>
                                    </a>
                                    </div>
                                    <div class="card-body">
                                        <h5 class="card-title mb-3">`+currentValue.text+`</h5>
                                    </div>
                                </div>
                            </div>`
            
                row_container.append(html_data)
            });
        }
    }else{
        row_container.append(`<img src="/staic/load.gif" width=100 height=100>`)
    }
 
}


function load_data(attr=null){
    
    let lang = $("#dropdownMenuButton1").attr('value')
    let url = 'http://' + location.host+ '/' + lang + '/api/get-branchens'
    if (attr != null){
        url += '?text_letter='+attr
    }
    $.ajax({
        url: url,
        type: "GET",
        dataType: "json",
        headers: {
        "X-Requested-With": "XMLHttpRequest",
        //   "X-CSRFToken": getCookie("csrftoken"),
        },
        success: (data) => {
            append_result(data)
        },
        error: (error) => {
            alert(error)
        }
    });
}


$(document).ready(function (){
    append_result()
    make_buttons()
    load_data()


    $("#filter_buttons").children("button").click(function(e){
        letter = $(this).attr('id')
        load_data(letter)
    })

})
