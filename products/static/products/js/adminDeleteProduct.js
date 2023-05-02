$(function(){
    $('#delete-product-link').on("click", function(){
        let dataDeleteHref = $(this).attr('data-delete-href');
        $('#delete-product').attr('href', dataDeleteHref);
    });
});

$(function(){
    $('.text-danger').on("click", function(){
        let dataDeleteHref = $(this).attr('data-delete-href');
        $('#delete-selected-product').attr('href', dataDeleteHref);
    });
});