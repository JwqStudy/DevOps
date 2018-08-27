// $(document).ready(function(){
//     set_applist();
// });
//
// function set_applist() {
//     var data;
//     $.ajax({
//         type: "get",
//         url: "http://127.0.0.1:8000/saltstack/applist/",
//         async: false,
//         success: function (callback) {
//             if (callback.msg == 'success') {
//                 data = callback.data;
//                 for(var i=0; i<data.length; i++){
//                     $("#applist").append("<option>" + data[i].appname + "</option>");
//                 }
//             }
//         }
//     });
// }