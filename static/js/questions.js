;(function() {

    var postRequest = window.stackoverflow.postRequest;
    var displayError = window.stackoverflow.displayError;

    function submitQuestion(){

        $("#submit-question").text("")
            .addClass("fas fa-spinner fa-spin");

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
                $("#submit-question").text("Try again!")
                    .removeClass("btn-primary fas fa-spinner fa-spin")
                    .addClass("btn-danger");
            }
        });

    }

    $(document).on("click", "#submit-question", submitQuestion);
})();
