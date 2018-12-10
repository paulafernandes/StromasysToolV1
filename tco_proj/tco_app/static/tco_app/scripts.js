document.addEventListener('DOMContentLoaded', () => {
    // $('#allsystems').on('change', function() {
    //     // alert(this.value);
    // });
    // function() {
        $('#allsystems').on('change', function() {
            if ($(this).val() == '0') {
                $("select#allmodels").html("<option>Select a model</option>");
                $("select#allmodels").attr('disabled', true);
            }
            else {
                // var url = $(this).val() + "/all_json_models";
                // var url = "tco_app/" + $(this).val() + "/all_json_models";
                alert(url);
                var systemid = $(this).val();

                $.ajax({
                    url : 'all_json_models/', // the endpoint
                    // url : url, // the endpoint
                    type : "POST", // http method
                    data : { id_system : systemid }, // data sent with the post request
            
                    // handle a successful response
                    success : function(json) {
                        $('#divContent').val(''); // remove the value from the input
                        console.log(json); // log the returned json to the console
                        console.log("success"); // another sanity check
                    },
            
                    // handle a non-successful response
                    error : function(xhr,errmsg,err) {
                        $('#divContent').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                            " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                    }
                });
            }
        });
        
        $('select#allmodels').on('change', function(vent) {
            if ($(this).val() == -1) {
                return;
            }
            myAwesomeFunctionToCallWhenAModelIsSelected();
        });
    // }
});