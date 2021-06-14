// // $(document).ready(function() {
// //     $("#search_btn ").click(function() {
// //         var short = $("#SelectId ").val();
// //         var sea_id = $("#search_id ").val();
// //         alert("this is")
// //         $.ajax({
// //             type: "GET ",
// //             url: "{% url 'api_search' %} ",
// //             data: {
// //                 short: short,
// //                 value: sea_id
// //             },
// //             success: function(response, status) {
// //                 alert(status);
// //                 var len = response.length;
// //                 for (var i = 0; i < len; i++) {
// //                     var dependent_repos_count = response[i].dependent_repos_count;
// //                     var dependents_count = response[i].dependents_count;
// //                     var description = response[i].description;
// //                     var forks = response[i].forks;

// //                     $("#userTable tbody").append(tr_str);
// //                 }
// //                 $("#platform").hide();
// //             }
// //         });
// //     });

// // //     $("a").click(function() {
// // //         alert("okay")

// // //         var sea_id = $("#platform").val();
// // //         alert(sea_id)

// // //         // var short = $("#SelectId ").val();
// // //         // var sea_id = $("#search_id ").val();
// // //         $.ajax({
// // //             type: "GET ",
// // //             url: "{% url 'api_search' %} ",
// // //             data: {
// // //                 short: "rank",
// // //                 value: sea_id
// // //             },
// // //             success: function(response, status) {

// // //                 var platform = $("#stdId").val('data-id');
// // //                 alert(status);
// // //             }
// // //         });

// // //     });
// // // });

// // // success: function(resp) {
// // //         alert("poka")

// // //     },
// // //     error: function() {
// // //         alert("eeror")

// // //     },

// // //     console.log($(this).val());

// // $("#id_username").change(function() {
// //     var username = $(this).val();

// //     $.ajax({
// //         url: '/ajax/validate_username/',
// //         data: {
// //             'username': username
// //         },
// //         dataType: 'json',
// //         success: function(data) {
// //             if (data.is_taken) {
// //                 alert("A user with this username already exists.");
// //             }
// //         }
// //     });

// // });

// // <
// // script >
// //     $("#id_username").change(function() {
// //         var form = $(this).closest("form");
// //         $.ajax({
// //             url: form.attr("data-validate-username-url"),
// //             data: form.serialize(),
// //             dataType: 'json',
// //             success: function(data) {
// //                 if (data.is_taken) {
// //                     alert(data.error_message);
// //                 }
// //             }
// //         });

// //     }); <
// // /script>


// $.ajax({
//     type: "GET ",
//     url: "/search",
//     data: {
//       'short': short= $("#SelectsShortId").val(),
//       'q':  q = $("#search_id").val(),
//     },

//     success: function (data,status) {
//       alert("poka");
//     },
//     error: function () {
//       alert("eeror");
//     },
//   });

// ("#add_ons select").change(function() {
//     // get current price of the addons
//     var order_price_addon = $(".order_price_addon").text();
//     // get price of the clicked radio button from the rel attribute
//     var add = $(this).children('option').attr('label');
//     var name = $(this).attr('name');
//     var val = $(this).val();
    
    
//     if(val == "") {
//         var price = parseInt(order_price_addon) - parseInt(add);
//         removeSession(name);
//     } else {
//         if(isSession(name) == 0) {
//             var price = parseInt(order_price_addon) + parseInt(add);
//         }   
//         setSession(name, val);              
//     }
    
//     $(".order_price_addon").html(price);    
//     setSession('order_price_addon', price);         
//     updateTotal();
// });

// $("#search_btn").click(function () {
//     var short = $("#SelectId ").val();
//     var q = $("#search_id ").val();

//     $.ajax({
//       url: "/search/",
//       type: "GET",
//       data: {
//         q: q,
//         short: short,
//       },
//       dataType: "json",
//       success: function (data) {
//         return data;
//       },
//       error: function () {
//         alert("erroe");
//       },
//     });
//   });