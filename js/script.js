

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




// Declaración de variables de validación fuera de la función
const btnEnviar = document.getElementById('btnEnviar');

// Declaración de variables de validación y mensajes de error
let nombreValido = false;
let apellidoValido = false;
let emailValido = false;
let telValido = false;
let rutValido = false;
let passValido = false;


const validacion = () => {
    const nombreUsuario = document.getElementById('nombre');
    const apellidoUsuario = document.getElementById('apellido');
    const telUsuario = document.getElementById('telefono');
    const rutUsuario = document.getElementById('RUT');
    const passUsuario = document.getElementById('pass');
    const emailUsuario = document.getElementById('email');


    // Validar nombre
    nombreUsuario.addEventListener('blur', function(){
        const nombreValue = nombreUsuario.value.trim();
        if (nombreValue === "" || !/^[a-zA-Z\s]+$/.test(nombreValue)) {
            nombreUsuario.classList.add('campo-invalido');
            nombreUsuario.classList.remove('campo-valido');
            document.getElementById('msgErrorNom').textContent = "Ingresa tu nombre";
            nombreValido = false;
        } else {
            document.getElementById('msgErrorNom').textContent = "";
            nombreValido = true;
            nombreUsuario.classList.remove('campo-invalido');
            nombreUsuario.classList.add('campo-valido');
        }
    });

    // Validar apellido
    apellidoUsuario.addEventListener('blur', function(){
        const apellidoValue = apellidoUsuario.value.trim();
        if (apellidoValue === "" || !/^[a-zA-Z\s]+$/.test(apellidoValue)) {
            apellidoUsuario.classList.add('campo-invalido');
            apellidoUsuario.classList.remove('campo-valido');
            document.getElementById('msgErrorAp').textContent = "Ingresa tu apellido";
            apellidoValido = false;
        } else {
            document.getElementById('msgErrorAp').textContent = "";
            apellidoValido = true;
            apellidoUsuario.classList.remove('campo-invalido');
            apellidoUsuario.classList.add('campo-valido');
        }
    });

    // Validar email
    emailUsuario.addEventListener('blur', function() {
        const emailValue = emailUsuario.value.trim();
        if (emailValue === "") {
            emailUsuario.classList.add('campo-invalido'); 
            emailUsuario.classList.remove('campo-valido'); 
            document.getElementById('msgErrorMail').textContent = "Ingresa tu e-mail."; 
            emailValido = false;
        } else if (!emailValue.includes("@") || !emailValue.includes(".")) {
            document.getElementById('msgErrorMail').textContent="Ingresa un correo electrónico válido.";
            emailValido = false;
        } else {
            document.getElementById('msgErrorMail').textContent="";
            emailValido = true;
            emailUsuario.classList.remove('campo-invalido');
            emailUsuario.classList.add('campo-valido');
        }
    });
    
    // Validar teléfono
    telUsuario.addEventListener('blur', function(){
        const telValue = telUsuario.value.trim();
        if (telValue === "" || !/^\d{8}$/.test(telValue)) {
            telUsuario.classList.add('campo-invalido');
            telUsuario.classList.remove('campo-valido');
            document.getElementById('msgErrorTel').textContent = "Ingresa un teléfono (8 dígitos).";
            telValido = false;
        } else {
            document.getElementById('msgErrorTel').textContent = "";
            telValido = true;
            telUsuario.classList.remove('campo-invalido');
            telUsuario.classList.add('campo-valido');
        }
    });

    // Validar RUT 
    rutUsuario.addEventListener('blur', function() {
        const rutValue = rutUsuario.value.trim();
        if (rutValue === "") {
            rutUsuario.classList.add('campo-invalido');
            rutUsuario.classList.remove('campo-valido'); 
            document.getElementById('msgErrorRUT').textContent = "Ingresa tu RUT (Sin puntos y con dígito verificador).";             
            rutValido = false;
        } else if (!Fn.validaRut(rutValue)) {
            document.getElementById('msgErrorRUT').textContent = "Ingresa un RUT válido. (Sin puntos y con dígito verificador).";             
            rutValido = false;
        } else {
            document.getElementById('msgErrorRUT').textContent = "";            
            rutUsuario.classList.remove('campo-invalido');
            rutUsuario.classList.add('campo-valido');
            rutValido = true;
        }
    });
    
    // Validar contraseña
    passUsuario.addEventListener('blur', function(){
        const passValue = passUsuario.value;
        if (passValue === "" || passValue.length < 8) {
            passUsuario.classList.add('campo-invalido');
            passUsuario.classList.remove('campo-valido');
            document.getElementById('msgErrorPass').textContent = "Ingresa una contraseña (Mínimo 8 dígitos).";            
            passValido = false;
        } else {
            document.getElementById('msgErrorPass').textContent = "";
            passValido = true;
            passUsuario.classList.remove('campo-invalido');
            passUsuario.classList.add('campo-valido');
        }
    });

    // Calcular esValido después de todas las validaciones
    const esValido = nombreValido && apellidoValido && emailValido && telValido && rutValido && passValido;
    return esValido;
}

btnEnviar.addEventListener('click', (event) => {
    const esValido = validacion();
    
    if (!esValido) {
        event.preventDefault();
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

