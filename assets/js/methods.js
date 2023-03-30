
async function GET(url, data=null){
    var res_data = null
    await $.ajax({
        url: url,
        type: "GET",
        dataType: "json",
        headers: {
        "X-Requested-With": "XMLHttpRequest",
        //   "X-CSRFToken": getCookie("csrftoken"),
        },
        success: (data) => {
            res_data = data
        },
        error: (error) => {
            res_data = error
        }
    });
    return res_data
}

// function POST(url, data=null){
    
// }