document.addEventListener('DOMContentLoaded', () => {
    // $('#allsystems').on('change', function() {
    //     // alert(this.value);
    // });

    function() {
        $('#allsystems').on('change', function() {
            if ($(this).val() == '0') {
                $("select#allmodels").html("<option>Select a model</option>");
                $("select#allmodels").attr('disabled', true);
            }
            else {
                var url = "/brand/" + $(this).val() + "/all_json_models";
                var brand = $(this).val();
                $.getJSON(url, function(models) {
                    var options = '<option value="0">Select a model</option>';
                    for (var i = 0; i < models.length; i++) {
                        options += '<option value="' + models[i].pk + '">' + models[i].fields['description'] + '</option>';
                    }
                    $("select#allmodels").html(options);
                    $("select#allmodels option:first").attr('selected', 'selected');
                    $("select#allmodels").attr('disabled', false);
                });
            }
        });
        
        $('select#allmodels').on('change', function(vent) {
            if ($(this).val() == -1) {
                return;
            }
            myAwesomeFunctionToCallWhenAModelIsSelected();
        });
    }
});