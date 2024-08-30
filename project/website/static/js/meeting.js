document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('meeting-form');
    const confirmation = document.getElementById('confirmation');
    const paymentMethod = document.getElementById('payment-method');
    const onlinePayment = document.getElementById('online-payment');
    const depositInfo = document.getElementById('deposit-info');

    paymentMethod.addEventListener('change', function() {
        onlinePayment.classList.add('hidden');
        depositInfo.classList.add('hidden');

        if (this.value === 'online') {
            onlinePayment.classList.remove('hidden');
        } else if (this.value === 'deposit') {
            depositInfo.classList.remove('hidden');
        }
    });

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        // Here you would typically send the form data to your backend
        // For this example, we'll just show the confirmation message

        // Validate form fields
        if (validateForm()) {
            // Hide the form
            form.style.display = 'none';

            // Show the confirmation message
            confirmation.classList.remove('hidden');
        }
    });

    function validateForm() {
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const meetingType = document.getElementById('meeting-type').value;
        const date = document.getElementById('date').value;
        const time = document.getElementById('time').value;
        const paymentMethod = document.getElementById('payment-method').value;

        if (!name || !email || !phone || !meetingType || !date || !time || !paymentMethod) {
            alert('Por favor, complete todos los campos obligatorios.');
            return false;
        }

        if (!isValidEmail(email)) {
            alert('Por favor, ingrese un correo electrónico válido.');
            return false;
        }

        if (!isValidPhone(phone)) {
            alert('Por favor, ingrese un número de teléfono válido.');
            return false;
        }

        return true;
    }

    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    function isValidPhone(phone) {
        const phoneRegex = /^\+?(\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$/;
        return phoneRegex.test(phone);
    }
});