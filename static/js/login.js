;(function() {

    var postRequest = window.stackoverflow.postRequest;
    var displayError = window.stackoverflow.displayError;

    function getUsername(){

        username = $(document).find("#username").val();

        if (!username){
            displayError("#error", "Please enter Username")
            return;
        }

        return username
    }

    function authenticateUser(){

        var username = getUsername();
        var params = {
            "username": username,
        };
        var url = "/login_user";

        var request = postRequest(url, params);
        request.done(function(result){

            if (result.success){
                    window.location = "/";
                    return;
            } else {
                displayError("#error", result.message);
            }
        });
    }

    function signupUser(){

        username = getUsername();
        var params = {
            "username": username,
        };
        var url = "/signup";

        var request = postRequest(url, params);
        request.done(function(result){

            if (result.success){
                    window.location = "/";
                    return;
            } else {
                displayError("#error", result.message);
            }
        });
    }

    $(document).on("click", "#login", authenticateUser)
            .on("click", "#signup", signupUser);
})();
