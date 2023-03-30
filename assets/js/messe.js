
function append_result(res=null){
    let row_container = $("#messe_container")
    row_container.empty()
    
    if(res != null){
        if(res.results.length == 0){
            row_container.append(`<h1>Nothing found!</h1>`)
        }else{
            res.results.forEach(function callback(currentValue, index, array) {
                html_data = 
                `<div class="col">
                <div class="card h-100 border border-3">
                    
                    <a href="#">
                        <img src="https://www.messeninfo.de/vorschau/inter_alpin_logo_2389.png" class="messeLogo" alt="Interalpin, Innsbruck">
                        <img src="{%static '/default.jpg'%}" class="card-img-top" alt="...">
                        <div class="time text-light bg-success rounded">19. - 21. April 2023</div>
                    </a>
                    <div class="card-body">
                    <h5 class="card-title">Samrt systems interaction </h5>
                    
                    <!-- <div class="extra-line"></div> -->
                    <p class="card-text "> Internationale Fachmesse für alpine Technologien</p>
                    <small class="card-text d-inline-block text-truncate">für Fachbesucher und Privatbesucher </small>
                    </div>
                
                        <div class="container">
                            <div class="row ">
                                <small class="col-8 d-inline-block text-truncate">
                                    <a href="#"><p class="m-0">Last updated 3 mins ago,</p></a>
                                    <p class="mr-auto">dasdasd</p>
                                </small>
                                <small class="col-4">
                                    <img src="{%static 'img/flag/at.webp'%}" alt="Österreich" class="ml-auto" >
                                </small>
                            </div>
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
    // let url = 'https://' + location.host+ '/' + lang + '/api/get-branchens'
    
    let url = HOST + lang + '/api/get-messe/'
    if (attr != null){
        url += attr
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
            console.log(data)
            append_result(data)
        },
        error: (error) => {
            alert(error)
        }
    });
}


$(document).ready(function (){
    b_id = location.pathname.split('/')[3]
    append_result()
    load_data(b_id)

})
