;(function() {

    var postRequest = window.stackoverflow.postRequest;
    var displayError = window.stackoverflow.displayError;

    function submitQuestion(){

        $("#submit-question span").text("");
        $("#submit-question i").removeClass("no-display");

        var params = {
            "title": $("#title").val(),
            "description": $("#description").val(),
            "tags": $("#tags").val()
        };

        url = "/questions/add_question?"

        var request = postRequest(url, params);

        request.done(function(result){

            if (result.success){
                    window.location = "/";
                    return;
            } else {
                $("#submit-question").removeClass("btn-primary")
                    .addClass("btn-danger");
                $("#submit-question span").text("Try again!");
                $("#submit-question i").addClass("no-display");
            }
        });

    }

    $(document).on("click", "#submit-question", submitQuestion);
})();
