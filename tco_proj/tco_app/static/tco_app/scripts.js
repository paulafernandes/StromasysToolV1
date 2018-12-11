document.addEventListener('DOMContentLoaded', () => {
    $("select#allsystems").on('change', function() {
        if ($(this).val() == 0) {
            $("select#allmodels").html("<option selected disabled>Select models</option>");
            $("select#allmodels").attr('disabled', true);
        }
        else {
            var url = "/simulation_page/" + $(this).val() + "/all_json_models/";
            $.getJSON(url, function(models) {
                // console.log(JSON.stringify(models));
                var options = '<option selected disabled multiple value="0">Select a model</option>';
                for (var i = 0; i < models.length; i++) {
                    options += '<option value="' + models[i].fields["id_system"] + '">' + models[i].fields["model_name"] + '</option>';
                }
                $("select#allmodels").html(options);
                $("select#allmodels option:first").attr('selected', 'selected');
                $("select#allmodels").attr('disabled', false);
            });
        }
    });
    
    $("select#allmodels").on('change', function(vent) {
        if ($(this).val() == -1) {
            return;
        }
        
    });	
});