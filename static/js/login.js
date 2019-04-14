;(function() {

    var makeAjaxCall = window.stackoverflow.makeAjaxCall;
    var CSRF_TOKEN = window.stackoverflow.CSRF_TOKEN;
    var displayError = window.stackoverflow.displayError;

    function getUsername(){

        return $(document).find("#username").val();
    }

    function authenticateUser(){

        var username = getUsername();

        if (!username){
            alert("Please enter Username");
            return;
        }

        var params = {
            "username": username,
        };

        var url = "/login_user";

        var $obj = $.ajax({
            url: url,
            type: "POST",
            data: params,
            headers: {
                "X-CSRFToken": CSRF_TOKEN("csrftoken")
            },
            dataType: "json",
        });

        $obj.done(function(result){
            console.log(result)

            if (result.success){
                    window.location = "/home";
                    return;
                }

            else{
                var error_disp = $("#error");
                error_disp.addClass("alert alert-danger");
                error_disp.text("Invalid Credentials");

                $("#error").fadeOut(
                    2000,
                    function(){
                        $(this).remove();
                    }
                );
            }
        });
    }

    $(document).on("click", "#login", authenticateUser);
})();
