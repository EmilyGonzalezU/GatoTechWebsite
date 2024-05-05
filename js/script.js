

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
const btnEnviar = document.getElementById('btnEnviar'); // Variable del boton para poder leerlo.
const validacion = () => { // Validacion
    const nombreUsuario = document.getElementById('nombre'); // Varibles constantes porque no cambian. Se obtienen mediante ID.
    const apellidoUsuario = document.getElementById('apellido');
    const telUsuario = document.getElementById('telefono');
    const rutUsuario = document.getElementById('RUT');
    const passUsuario = document.getElementById('pass');
    const emailUsuario = document.getElementById('email');

    // Empieza con 0 errores detectados
    let  hayErrores= false;

    //Validar nombre
    nombreUsuario.addEventListener('blur', function(){ // Evento hace que no se vaya el foco de la validacion.
        const nombreValue = nombreUsuario.value.trim(); // Obtener el valor del campo de nombre y eliminar espacios en blanco
        if (nombreValue === "" || !/^[a-zA-Z\s]+$/.test(nombreValue)) { 
            nombreUsuario.classList.add('campo-invalido');
            nombreUsuario.classList.remove('campo-valido');
            document.getElementById('msgErrorNom').textContent = "Ingresa tu nombre";
            // Cada validacion que no pase en un error, verdadero. No pasa.
            hayErrores = true;
        } else {
            // Si pasa validacion texto error en blanco. No se muestra.
            nombreUsuario.classList.remove('campo-invalido');
            nombreUsuario.classList.add('campo-valido');
            document.getElementById('msgErrorNom').textContent = "";
             
        }
    });

    // Validar apellido
    apellidoUsuario.addEventListener('blur', function(){ 
        const apellidoValue = apellidoUsuario.value.trim(); // Obtener el valor del campo de nombre y eliminar espacios en blanco
        if (apellidoValue === "" || !/^[a-zA-Z\s]+$/.test(apellidoValue)) {
            apellidoUsuario.classList.add('campo-invalido');
            apellidoUsuario.classList.remove('campo-valido');
            document.getElementById('msgErrorAp').textContent = "Ingresa tu apellido";
            hayErrores = true;
        } else {
            apellidoUsuario.classList.remove('campo-invalido');
            apellidoUsuario.classList.add('campo-valido');
            document.getElementById('msgErrorAp').textContent = "";
             
        }
    });

    // Validar email
    emailUsuario.addEventListener('blur', function() {
        const emailValue = emailUsuario.value.trim(); 
        const mensajeErrorEmail = document.getElementById('msgErrorMail'); 

        if (emailValue === "") {
            emailUsuario.classList.add('campo-invalido'); 
            emailUsuario.classList.remove('campo-valido'); 
            mensajeErrorEmail.textContent = "Ingresa tu e-mail."; 
            hayErrores = true; 
        } else {
            if (!emailValue.includes("@") || !emailValue.includes(".")) {
                emailUsuario.classList.add('campo-invalido');
                emailUsuario.classList.remove('campo-valido');
                mensajeErrorEmail.textContent = "Por favor, ingresa un correo electrónico válido.";
                hayErrores = true;
            } else {
                emailUsuario.classList.remove('campo-invalido');
                emailUsuario.classList.add('campo-valido');
                mensajeErrorEmail.textContent = ""; 
                 
            }
        }
    });
    
    // Validar teléfono
    telUsuario.addEventListener('blur', function(){ 
        const telValue = telUsuario.value.trim();
        if (telValue === "" || !/^\d{8}$/.test(telValue)) {
            telUsuario.blur();
            telUsuario.classList.add('campo-invalido');
            telUsuario.classList.remove('campo-valido');
            document.getElementById('msgErrorTel').textContent = "Ingresa tu teléfono (Sin número 9)";
            hayErrores = true;
        } else {
            telUsuario.classList.remove('campo-invalido');
            telUsuario.classList.add('campo-valido');
            document.getElementById('msgErrorTel').textContent = "";
             
        }
    });

    // Validar RUT 
    rutUsuario.addEventListener('blur', function() {
        const rutValue = rutUsuario.value.trim(); 
        const mensajeErrorRut = document.getElementById('msgErrorRUT'); 
    
        // Validar si el campo está vacío
        if (rutValue === "") {
            rutUsuario.classList.add('campo-invalido');
            rutUsuario.classList.remove('campo-valido'); 
            mensajeErrorRut.textContent = "Ingresa tu RUT (Sin puntos y con dígito verificador)."; 
            hayErrores = true;
        } else {
            if (!Fn.validaRut(rutValue)) {
                rutUsuario.classList.add('campo-invalido');
                rutUsuario.classList.remove('campo-valido');
                mensajeErrorRut.textContent = "Ingresa un RUT válido (Sin puntos y con dígito verificador).";
                hayErrores = true;
            } else {
                rutUsuario.classList.remove('campo-invalido');
                rutUsuario.classList.add('campo-valido');
                mensajeErrorRut.textContent = ""; // Eliminar el mensaje de error
                 
            }
        }
    });
    
    // Validar contraseña
    passUsuario.addEventListener('blur', function(){ 
        if (passUsuario.value === "" || passUsuario.value.length < 8) {
            passUsuario.blur();
            passUsuario.classList.add('campo-invalido');
            passUsuario.classList.remove('campo-valido');
            document.getElementById('msgErrorPass').textContent = "Ingresa una contraseña (Mínimo 8 dígitos).";
            hayErrores = true;
        } else {
            passUsuario.classList.remove('campo-invalido');
            passUsuario.classList.add('campo-valido');
            document.getElementById('msgErrorPass').textContent = "";
             
        }
    });
    return hayErrores;
}


btnEnviar.addEventListener('click', (event) => {

    const esValido = validacion();
    
    
    if (!esValido) {
        event.preventDefault(); // Detieneee el envío del formulario si hay errores de validación
    }
});

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

