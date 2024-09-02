// register.js
document.addEventListener('DOMContentLoaded', function() {
    const paymentMethodSelect = document.getElementById('id_metodo_pago');
    const onlinePaymentInfo = document.getElementById('online-payment');
    const depositInfo = document.getElementById('deposit-info');

    function updatePaymentInfo() {
        if (paymentMethodSelect.value === 'online') {
            onlinePaymentInfo.style.display = 'block';
            depositInfo.style.display = 'none';
        } else if (paymentMethodSelect.value === 'deposito') {
            onlinePaymentInfo.style.display = 'none';
            depositInfo.style.display = 'block';
        } else {
            onlinePaymentInfo.style.display = 'none';
            depositInfo.style.display = 'none';
        }
    }

    paymentMethodSelect.addEventListener('change', updatePaymentInfo);

    // Call the function initially to set the correct state
    updatePaymentInfo();
});