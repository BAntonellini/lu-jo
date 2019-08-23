window.onload = function() {
  var botonesCursos = document.querySelectorAll(".boton-curso");
  botonesCursos.forEach(function(boton) {
    boton.addEventListener("click", function() {
      //console.log(boton.dataset.slug);
      var xhr = new XMLHttpRequest();
      xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          var json_response = JSON.parse(this.response);
          console.log(json_response);

          var modal_title = document.querySelector(".modal-title");
          modal_title.innerHTML = json_response.titulo;

          var modal_body = document.querySelector(".modal-body");
          modal_body.innerHTML = json_response.resumen;

          var modal_imagen = document.querySelector(".imagen-modal");
          modal_imagen.setAttribute("src", "media/" + json_response.imagen);

          var boton_registrar_curso = document.querySelector(
            "#boton-registrar-curso"
          );
          boton_registrar_curso.addEventListener("click", function(e) {
            console.log(e.target);
            window.location.href = "#contact-form";

            
            var dia = new Date();
            var hora = dia.getHours();
            var saludo = "";
            switch (true) {
              case (hora >= 0 && hora <= 5):
                saludo = "Buenas noches";
                break;
              case (hora >= 6 && hora <= 12):
                saludo = "Buenos días";
                break;
              case (hora >= 13 && hora <= 19):
                saludo = "Buenas tardes";
                break;
              case (hora >= 20):
                saludo = "Buenas noches";
                break;
              default:
                saludo = "default";
                break;
            }
            var pre_message = saludo +"\nQuisiera participar del siguiente curso: " +
              json_response.titulo;

            var form_message = document.querySelector('#form_message')
            form_message.value = pre_message;

            document.querySelector("#tipo_consulta").selectedIndex = "1";
          });
        }
      };
      xhr.open("GET", "getcurso" + "?q=" + boton.dataset.slug, true);
      xhr.send();
    });
  });
};

// MODAL ESCONDIDO
//<div class="modal" id="modal" style="display: none;" aria-hidden="true">

// MODAL SHOW
//<div class="modal show" id="modal" style="display: block; padding-right: 15px;" aria-modal="true">
