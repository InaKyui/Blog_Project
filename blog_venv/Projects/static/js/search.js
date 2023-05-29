function searchArticle(){
    $("#search").keydown(function (event){
        if (event.keyCode == 13){
            event.preventDefault();

            var key = $("input[id='search']").val();
            window.location.href = "/article/search?key=" + key;
        }
    });
}


$(function (){
    searchArticle();
});