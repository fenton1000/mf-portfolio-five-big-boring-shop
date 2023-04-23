$(function(){
    $('#all-items button').on("click", function(){
        let dataDeleteHref = $(this).attr('data-delete-href');
        $('#remove').attr('href', dataDeleteHref);
    });
});