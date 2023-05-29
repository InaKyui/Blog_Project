function emailCaptcha(){
    $("#captcha-btn").click(function (event){
        var $this = $(this)
        event.preventDefault();

        var email = $("input[name='email']").val()
        if (email == ""){
            alert("Please check email.");
        }
        else{
            $this.off("click");
            var countdown = 60;
            var timer = setInterval(handler=function(){
                    $this.text(countdown);
                    countdown -= 1;
                    if (countdown <= 0){
                        clearInterval(timer);
                        $this.text("Get captcha");
                    }
                }, timeout=1000);
}
        $.ajax({
            url: "/auth/send_captcha?email=" + email,
            method: "GET",
        });
    });
}


$(function (){
    emailCaptcha();
});