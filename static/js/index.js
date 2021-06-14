$(document).ready(function () {
    // alert('alert')
    $('.id_100').click(function (e) {
        e.preventDefault();
       


        id = $(".likebutton").attr("data-catid");
        // short=$("div.id_100 select").val("val2");
        sort = $("div.id_100 select").val();
        // $("#offcanvasExample").hide();
        // alert(sort)

        //    a=$(this).val("data-catid");

        $.ajax({
            type: "GET",
            contentType: " application/json",
            url: "/search",
            data: {
                'q': id,
                'sort':sort
            },
            

        })




    });

});

 // var url = 'https://api.github.com/v1/...';
        // var data = {
        //     q: 'search',
        //     text: 'my text'
        // };

        // $.getJSON(url, data, function (data, status) {

        //     if (status === 200) {
        //         //Do stuff with the JSON data
        //     }
        // });