//inico sesion
let emailInicioValido = false;
let passInicioValido = false; 

const emailInicio = document.getElementById('emailInicio');
const passInicio = document.getElementById('passInicio');

const btnEnviarInicio = document.getElementById('btn');

const validacionIncioSesion = () =>{

    emailInicio.addEventListener('blur', function() {
        const email = emailInicio.value.trim();
        if (email === "") {
            emailInicio.classList.add('campo-invalido'); 
            emailInicio.classList.remove('campo-valido'); 
            document.getElementById('msgErrorMailInicio').textContent = "Ingrese su e-mail."; 
            emailInicioValido = false;
        } else if (!email.includes("@") || !email.includes(".")) {
            document.getElementById('msgErrorMailInicio').textContent="Ingrese un e-mail válido.";
            emailInicioValido = false;
        } else {
            document.getElementById('msgErrorMailInicio').textContent="";
            emailInicioValido = true;
            emailInicio.classList.remove('campo-invalido');
            emailInicio.classList.add('campo-valido');
        }
    });

    passInicio.addEventListener('blur', function(){
        const pass = passInicio.value;
        if (pass === "" || pass.length < 8) {
            passInicio.classList.add('campo-invalido');
            passInicio.classList.remove('campo-valido');
            document.getElementById('msgErrorPassInicio').textContent = "Ingrese su contraseña.";            
            passInicioValido = false;
        } else {
            document.getElementById('msgErrorPassInicio').textContent = "";
            passInicioValido = true;
            passInicio.classList.remove('campo-invalido');
            passInicio.classList.add('campo-valido');
        }
    });

    // Calcular esValido después de todas las validaciones
    const esValidoInicio = emailInicioValido && passInicioValido;
    return esValidoInicio;
}

btnEnviarInicio.addEventListener('click', (e) => {
    const esValidoInicio = validacionIncioSesion();
    
    if (!esValidoInicio) {
        e.preventDefault();
        emailInicio.focus();
        passInicio.focus();
    }
});