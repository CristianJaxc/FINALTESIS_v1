/*------------------
        Background Set
 --------------------*/
window.onload=function(){

    $('#onload').delay(200).fadeOut(600);

    $('body').removeClass('hidden');
}
// <!-- PARA EL MENU DESPLEGABLE -->
$(".canvas-open").on('click', function () {
    $(".offcanvas-menu-wrapper").addClass("show-offcanvas-menu-wrapper");
    $(".offcanvas-menu-overlay").addClass("active");
});
$(".canvas-close, .offcanvas-menu-overlay").on('click', function () {
    $(".offcanvas-menu-wrapper").removeClass("show-offcanvas-menu-wrapper");
    $(".offcanvas-menu-overlay").removeClass("active");
});

