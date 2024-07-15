document.addEventListener('DOMContentLoaded', function() {
    const emailInicio = document.getElementById('email');
    const passInicio = document.getElementById('password');
    const form = document.getElementById('sing-up-form');
    const btnEnviarInicio = document.getElementById('btn');

    const validarEmail = () => {
        const email = emailInicio.value.trim();
        if (email === "") {
            emailInicio.classList.add('campo-invalido');
            emailInicio.classList.remove('campo-valido');
            document.getElementById('msgErrorMailInicio').textContent = "Ingrese su e-mail.";
            return false;
        } else if (!email.includes("@") || !email.includes(".")) {
            emailInicio.classList.add('campo-invalido');
            emailInicio.classList.remove('campo-valido');
            document.getElementById('msgErrorMailInicio').textContent = "Ingrese un e-mail válido.";
            return false;
        } else {
            emailInicio.classList.remove('campo-invalido');
            emailInicio.classList.add('campo-valido');
            document.getElementById('msgErrorMailInicio').textContent = "";
            return true;
        }
    };

    const validarPassword = () => {
        const pass = passInicio.value;
        if (pass === "" || pass.length < 8) {
            passInicio.classList.add('campo-invalido');
            passInicio.classList.remove('campo-valido');
            document.getElementById('msgErrorPassInicio').textContent = "Ingrese su contraseña (mínimo 8 caracteres).";
            return false;
        } else {
            passInicio.classList.remove('campo-invalido');
            passInicio.classList.add('campo-valido');
            document.getElementById('msgErrorPassInicio').textContent = "";
            return true;
        }
    };

    form.addEventListener('submit', (e) => {
        const emailValido = validarEmail();
        const passwordValido = validarPassword();

        if (!emailValido || !passwordValido) {
            e.preventDefault();
            validarEmail();
            validarPassword();
        }
    });

    emailInicio.addEventListener('input', validarEmail);
    passInicio.addEventListener('input', validarPassword);
});