let data = document.currentScript.dataset;
let userRating = data.userRating;

$(function () {

    function fillInUserRating() {
        $("option[value|='"+userRating+"']").attr('selected', 'selected');
    }

    fillInUserRating();
});