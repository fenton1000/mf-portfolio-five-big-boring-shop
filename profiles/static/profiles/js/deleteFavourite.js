$(function(){
    $('.text-danger').on("click", function(){
        let dataDeleteHref = $(this).attr('data-delete-href');
        $('#delete-selected-favourite').attr('href', dataDeleteHref);
    });
});