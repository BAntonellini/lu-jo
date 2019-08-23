// Cambiamos color de la navbar
$(window).scroll(function(){
  $('nav').toggleClass('scrolled', $(window).scrollTop() > 200);
});