// login.js

document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.querySelector('.login-form');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');

    loginForm.addEventListener('submit', function(event) {
        let isValid = true;

        if (usernameInput.value.trim() === '') {
            showError(usernameInput, 'El nombre de usuario es obligatorio');
            isValid = false;
        } else {
            clearError(usernameInput);
        }

        if (passwordInput.value.trim() === '') {
            showError(passwordInput, 'La contraseña es obligatoria');
            isValid = false;
        } else {
            clearError(passwordInput);
        }

        if (!isValid) {
            event.preventDefault();
        }
    });

    function showError(input, message) {
        const formGroup = input.closest('.form-group');
        let errorElement = formGroup.querySelector('.error-message');
        
        if (!errorElement) {
            errorElement = document.createElement('div');
            errorElement.className = 'error-message';
            formGroup.appendChild(errorElement);
        }
        
        errorElement.textContent = message;
        input.classList.add('error');
    }

    function clearError(input) {
        const formGroup = input.closest('.form-group');
        const errorElement = formGroup.querySelector('.error-message');
        
        if (errorElement) {
            errorElement.remove();
        }
        
        input.classList.remove('error');
    }
});