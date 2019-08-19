window.onload = function() {
  var botonesCursos = document.querySelectorAll(".boton-curso");
  botonesCursos.forEach(function(boton) {
    boton.addEventListener("click", function() {
      //console.log(boton.dataset.slug);
      var xhr = new XMLHttpRequest();
      xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var json_response = JSON.parse(this.response);
            console.log(json_response)
        }
      };
      xhr.open("GET", "getcurso" + "?q=" + boton.dataset.slug, true);
      xhr.send();
    });
  });
};