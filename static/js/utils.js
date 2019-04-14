;( function(global){

var ajax = global.ajax;

global.CSRF_TOKEN = function(name) {
                        var cookieValue = null;
                        if (document.cookie && document.cookie != '') {
                            var cookies = document.cookie.split(';');
                            for (var i = 0; i < cookies.length; i++) {
                                var cookie = $.trim(cookies[i]);
                                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                    break;
                                }
                            }
                        }
                        return cookieValue;
                    };

global.makeAjaxCall = function(url, type) {
                        return ajax({
                            url: url,
                            type: type,
                        });
                    };

global.displayError = function(selector, message) {

                        var errorDisp = $Dom.find(selector);
                        erroDisp.addClass("alert alert-danger");
                        erroDisp.text(message);

                        $(selector).fadeOut(
                            2000,
                            function(){
                                $(this).remove();
                            }
                        );

                    };
})(window.stackoverflow = window.stackoverflow || {});

