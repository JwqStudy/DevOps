function get_param() {
    var param = {
        newEmail: $("#newEmail").val()
    };
    return param
}

function submitEmail() {
    var data = get_param();
    $.ajax({
        type: "post",
        url: "http://127.0.0.1:8000/public/setting/",
        data: data,
        // async: false,
        success: function (callback) {
            if (callback.msg == 'success') {
                // result = callback.data
                alert("send eamil success!")
            }
        }
    });
}