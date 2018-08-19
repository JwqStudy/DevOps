$(document).ready(function(){
    get_iplist();
});


function get_iplist() {
    var data;
    $.ajax({
        type: "get",
        url: "http://127.0.0.1:8000/saltstack/iplist/",
        async: false,
        success: function (callback) {
            // if (callback.msg == 'success') {
                data = callback.data;
                for(var i=0; i<data.length; i++){
                    $("#iplist").append("<option>" + data[i].ipnum + "</option>");
                }
            // }
        }
    });
}

