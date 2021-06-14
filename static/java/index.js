$(document).ready(function () {    
    $('search_btn1').click(function () { 
        var q =$("#search_id").val();
        var short =$("#SelectsShortId").val();       
    
        $.ajax({
            type: "GET ",
            url: "{% url 'api_search' %} ",
            data: {
                short: "rank",
                value: sea_id
            },
            success: function(response, status) {

                alert(status);
            }
        });
    
        
    });

});
