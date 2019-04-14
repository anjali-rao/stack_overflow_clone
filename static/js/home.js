;(function() {

    var postRequest = window.stackoverflow.postRequest;


    function listQuestions(url, selector){
        params = {};
        var request = postRequest(url, params);
        request.done(function(result){

            $(selector).empty();
            if (result.success){
                $(selector).append(result.html);
            } else {
                $(selector).append("<span class='text-muted ml-4'>No questions yet</span>");
            }
        });
    }

    function userQuestions(){

        url = "/questions/user_questions?";
        selector = "#user-questions";
        listQuestions(url, selector);
    }

    function communityQuestions(){

        url = "/questions/community_questions?";
        selector = "#community-questions";
        listQuestions(url, selector);
    }

    function deleteQuestion(){
        var questionId = $(this).attr("id");
        $(this).addClass("no-display");
        $(this).parent().find(".del-wait").removeClass("no-display");

        url = "/questions/delete_question";
        params = {
            "question_id": questionId
        };

        var request = postRequest(url, params);
        request.done(function(result){

            if (result.success){
                userQuestions();
            }
        });
    }

    $(document).on("click", ".delete", deleteQuestion);

    userQuestions();
    communityQuestions();
})();
