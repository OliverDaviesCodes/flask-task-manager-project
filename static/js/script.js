$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "right"
    });
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "select"
        }
    });
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
});