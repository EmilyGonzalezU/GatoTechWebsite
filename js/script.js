//Modal inicio sesion
document.getElementById('openModalBtn').addEventListener('click', function() {
    $('#loginModal').modal('show');
});

// Owl carousel resposivo
$(document).ready(function() { 
    $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 10,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
                nav: true
            },
            576: {
                items: 2,
                nav: false
            },
            768: {
                items: 3,
                nav: false
            },
            992: {
                items: 4,
                nav: false
            },
            1200: {
                items: 5,
                nav: false,
                loop: false
            }
        }
    })
});

// Auto show filtros

$(document).ready(function(){
        // Abre el primer acordeon al cargar la pagina
    $('#collapseOne').collapse('show');
});

// Activacion/Desactivacion DSCTO
var containerDsctoTarget = document.querySelectorAll('.dsctoTarget');

containerDsctoTarget.forEach(function(dsctoTarget){
    var dscto = dsctoTarget.querySelector('.dscto'); 
    var oldPrice = dsctoTarget.querySelector('.oldPrice'); 
    
    if (dscto.textContent.trim() === '' && oldPrice.textContent.trim() === ''){
        dsctoTarget.style.display = 'none';
        dscto.style.display = 'none';
        oldPrice.style.display = 'none'; 
    } else {
        dsctoTarget.style.display = 'block'; 
        dscto.style.display = 'block';
        oldPrice.style.display = 'block';
    }
});

// Trunc text
document.addEventListener("DOMContentLoaded", function() { /*DOM CARGADO EJECUTA FUNCION*/
    var productDescriptions = document.querySelectorAll('.productDesc');

    productDescriptions.forEach(function(productDesc) {
        if (productDesc.textContent.length > 50) {
            productDesc.textContent = productDesc.textContent.substring(0, 50) + '...';
        }
    });
});


// Validacion Registro usuario
const btnEnviar = document.getElementById('btnEnviar');

btnEnviar.addEventListener('click', (e) => {

    const esValido = validacion();
    
    
    if (!esValido) {
        e.preventDefault(); // Detieneee el envío del formulario si hay errores de validación
    }
});

const validacion = () => {
    const nombreUsuario = document.getElementById('nombre');
    const apellidoUsuario = document.getElementById('apellido');
    const telUsuario = document.getElementById('telefono');
    const rutUsuario = document.getElementById('RUT');
    const passUsuario = document.getElementById('pass');
    const emailUsuario = document.getElementById('email');

    let hayErrores = false;

    //Validar nombre
    if (nombreUsuario.value === "") {
        document.getElementById('msgErrorNom').textContent = "Por favor, escribe tu nombre.";
        hayErrores = true;
    } else {
        document.getElementById('msgErrorNom').textContent = "";
    }

    // Validar apellido
    if (apellidoUsuario.value === "") {
        document.getElementById('msgErrorAp').textContent = "Por favor, escribe tu apellido.";
        hayErrores = true;
    } else {
        document.getElementById('msgErrorAp').textContent = "";
    }

    // Validar email
    const emailValue = emailUsuario.value;
    const mensajeErrorEmail = document.getElementById('msgErrorMail');
    if (emailValue.value === "") {
        mensajeErrorEmail.textContent = "Por favor, escribe tu correo electrónico.";
        hayErrores = true;
    } else {
        if (!emailValido(emailValue)) {
            mensajeErrorEmail.textContent = "Por favor, Ingrese correo valido.";
        }else{
            mensajeErrorEmail.textContent = "";
        }
        
    }

    // Validar teléfono
    if (telUsuario.value === "") {
        document.getElementById('msgErrorTel').textContent = "Por favor, escribe tu teléfono.";
        hayErrores = true;
    } else {
        document.getElementById('msgErrorTel').textContent = "";
    }

    // Validar RUT 
    const rutValue = rutUsuario.value.trim();
    const mensajeErrorRut = document.getElementById('msgErrorRUT');

    // Vacio
    if (rutValue === "") {
        mensajeErrorRut.textContent = "Por favor, ingresa un RUT.";
        hayErrores = true;
    } else {
        // Validacion  RUT
        if (!Fn.validaRut(rutValue)) {
            mensajeErrorRut.textContent = "Por favor, ingresa un RUT válido.";
            hayErrores = true;
        } else {
            mensajeErrorRut.textContent = "";
        }
    }

    // Validar contraseña
    if (passUsuario.value === "") {
        document.getElementById('msgErrorPass').textContent = "Por favor, ingresa una contraseña válida.";
        
        hayErrores = true;
    } else {
        document.getElementById('msgErrorPass').textContent = "";
    }
    
    // Si hay errores, no se puede enviar el formulario
    return !hayErrores;
    
}

// Validacion email @ 
const emailValido = email => {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// Validacion RUT 
var Fn = {
    validaRut: function (rutCompleto) {
        rutCompleto = rutCompleto.replace("‐", "-");
        if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto))
            return false;
        var tmp = rutCompleto.split('-');
        var digv = tmp[1];
        var rut = tmp[0];
        if (digv == 'K') digv = 'k';

        return (Fn.dv(rut) == digv);
    },
    dv: function (T) {
        var M = 0, S = 1;
        for (; T; T = Math.floor(T / 10))
            S = (S + T % 10 * (9 - M++ % 6)) % 11;
        return S ? S - 1 : 'k';
    }
}

