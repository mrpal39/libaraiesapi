


$(document).ready(function() {
    $("#formid").hide();
 
    // catch the form's submit event
    // $('#id_username').keyup(function() {
        
    //     // create an AJAX call
    //     $.ajax({
    //         data: $(this).serialize(), // get the form data
    //         url: "{% url 'validate_username' %}",
    //         // on success
    //         success: function(data) {
    //             if (response.is_taken == true) {
    //                 $('#id_username').removeClass('is-valid').addClass('is-invalid');
    //                 $('#id_username').after('<div class="invalid-feedback d-block" id="usernameError">This username is not available!</div>')
    //             } else {
    //                 $('#id_username').removeClass('is-invalid').addClass('is-valid');
    //                 $('#usernameError').remove();

    //             }

    //         },
    //         // on error
    //         error: function(response) {
    //             // alert the error if any error occured
    //             console.log(response.responseJSON.errors)
    //         }
    //     });

    //     return false;
    // });
});