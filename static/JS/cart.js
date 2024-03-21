var updateButton =document.getElementsByClassName('save-vendor')

for (i=0; i <updateButton.length ; i++) { 
    updateButton[i].addEventListener("click", function(){
        var vendor = this.dataset.vendor
        var action = this.dataset.action
        console.log(vendor, action)
        updateClientOrder(vendor,action)
        
    
    })
}
function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function updateClientOrder(vendorId, action){
   

    var url = '/update_cart/'

    fetch(url, {
        method: 'POST',
        headers: {'Content-Type': 'application/json',
        'X-CSRFToken': getToken('csrftoken'),
    },
    body:JSON.stringify({'vendorId': vendorId, "action": action})
})
.then((response)=>{
        return response.json()
    })
    .then((data) => {
        location.reload()
    });

}