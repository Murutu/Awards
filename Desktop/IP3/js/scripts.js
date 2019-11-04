$(document).ready(function() {
    $(".click").click(function() {
        $("#k-hidden").toggle();
        $("#d1-show").toggle();
    });
});

$(document).ready(function() {
    $(".click1").click(function() {
        $("#l-hidden").toggle();
        $("#d2-show").toggle();
    });
});

$(document).ready(function() {
    $(".click3").click(function() {
        $("#m-hidden").toggle();
            $("#d4-show").toggle();
    });
});

$(document).ready(function() {
$(".namee").hide()
$(".b1").hover(function(){
$(this).find(".namee").toggle();
        });
});

$(document).ready(function() {
    $(".frm").submit(function(){
        var name=$("input#name").val();
        alert("Thank you for reaching out to us " +name +".We have received your feedback.");

    });
});








