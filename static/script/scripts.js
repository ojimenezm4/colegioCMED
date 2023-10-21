// Inicializo materializer

M.AutoInit();
M.Modal.init()
// Inicializa Materialize CSS

//fincion que muestra y colapsa

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems);
});
// Inicializa el modal
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);

    // Maneja la respuesta del formulario y actualiza la página si es exitoso
    var form = document.getElementById('crear-anuncio-form');
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        fetch(form.action, {
            method: 'POST',
            body: new FormData(form),
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    M.toast({html: 'Publicación creada con éxito'});
                    location.reload();  // Actualiza la página
                } else {
                    M.toast({html: 'Error al crear la publicación'});
                }
            });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.materialboxed');
    var instances = M.Materialbox.init(elems, options);
});

// Or with jQuery

$(document).ready(function () {
    $('.materialboxed').materialbox();
});


function setCurrentTime() {
    // Obtener el campo de fecha y hora
    var fechaYHoraInput = document.getElementById('fecha_y_hora');

    // Obtener la fecha y hora actual en el formato YYYY-MM-DDTHH:MM
    var currentDateTime = new Date().toISOString().slice(0, 16);

    // Establecer la fecha y hora actual en el campo de entrada
    fechaYHoraInput.value = currentDateTime;

    // Enviar el formulario
    document.getElementById('anuncio-form').submit();
}

// Inicializar el modal
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
});


document.addEventListener('DOMContentLoaded', function () {
    const modalInstance = M.Modal.init(document.getElementById('login-modal'));

    // Inicializa el modal de inicio de sesión
    const loginButton = document.querySelector('.modal-trigger');
    loginButton.addEventListener('click', function () {
        modalInstance.open(); // Abre el modal cuando se hace clic en "Iniciar sesión"
    });
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
});
document.getElementById('crear-alumno-form').addEventListener('submit', function (event) {
    var password1 = document.getElementById('{{ form.password.id_for_label }}').value;
    var password2 = document.getElementById('{{ form.password2.id_for_label }}').value;

    if (password1 !== password2) {
        // Las contraseñas no coinciden, muestra una alerta modal
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Las contraseñas no coinciden. Por favor, inténtalo de nuevo.'
        });

        event.preventDefault();  // Evita el envío del formulario
    }
});


document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.chips');
    var instances = M.Chips.init(elems, options);
});

