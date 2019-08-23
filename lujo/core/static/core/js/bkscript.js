var nav = document.querySelector("#wrapper-navbar");

$(function() {
    $(window).scroll(function() {
    if ($(window).scrollTop() > 100) {
      nav.classList.remove("bg-transparent");
      nav.classList.add("bg-grey");
    } else {
      nav.classList.remove("bg-grey");
      nav.classList.add("bg-transparent");
    }
      });
  });