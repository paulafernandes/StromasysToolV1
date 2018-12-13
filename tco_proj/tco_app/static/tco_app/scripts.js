document.addEventListener('DOMContentLoaded', () => {
    $("select#allsystems").on('change', function() {
        if ($(this).val() == 0) {
            $("#divModels").css('display', 'none');
        }
        else {
            var url = "/simulation_page/" + $(this).val() + "/all_json_models/";
            $.getJSON(url, function(models) {
                // console.log(JSON.stringify(models));
                var options = '<option selected value="0">Select Model</option>';
                for (var i = 0; i < models.length; i++) {
                    options += '<option value="' + models[i].pk + '">' + models[i].fields["model_name"] + '</option>';
                }
                $("#divModels").css('display', 'block');
                $("select#allmodels").html(options);
                $("select#allmodels option:first").attr('selected', 'selected');
            });
        }
    });
    
    $("select#allmodels").on('change', function(vent) {
        if ($(this).val() == 0) {
            $("#divCpus").css('display', 'none');
            $("#lblCpu").css('display', 'none');
        }
        else {
            var url = "/simulation_page/" + $(this).val() + "/all_json_cpus/";
            $.getJSON(url, function(cpus) {
                console.log(JSON.stringify(cpus));
                var options = '<option selected value="0">Select CPU</option>';
                for (var i = 0; i < cpus.length; i++) {
                    if (cpus.length == 1)
                    {
                        $("#cpulabel").val(cpus[i].fields["min_cpu"]);
                        $("#lblCpu").css('display', 'block');
                        $("#divCpus").css('display', 'none');
                    }
                    else {
                        let labelcpu;
                        if (cpus[i].fields["max_cpu"] > 0)
                            labelcpu = cpus[i].fields["min_cpu"] + ' - ' + cpus[i].fields["max_cpu"];
                        else 
                            labelcpu = cpus[i].fields["min_cpu"];
    
                        options += '<option value="' + cpus[i].pk + '">' + labelcpu + '</option>';
                        $("#lblCpu").css('display', 'none');
                        $("#divCpus").css('display', 'block');
                        $("select#allcpus").html(options);
                        $("select#allcpus option:first").attr('selected', 'selected');
                    }        
                }
            });
        }
    });	
});