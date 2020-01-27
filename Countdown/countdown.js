console.log("Connected");
var count = 60;
var reset = $('reset')

var timer = setInterval(function() {
    $("#time").html(count--);
    if(count == 1) clearInterval(timer);
}, 1000);

function reset_timer(){
  count = 60;
  $("#time").html(count--);
}
