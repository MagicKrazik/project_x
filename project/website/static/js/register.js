// register.js
document.addEventListener('DOMContentLoaded', function() {
    const paymentMethodSelect = document.getElementById('payment-method');
    const onlinePaymentInfo = document.getElementById('online-payment');
    const depositInfo = document.getElementById('deposit-info');

    paymentMethodSelect.addEventListener('change', function() {
        if (this.value === 'online') {
            onlinePaymentInfo.style.display = 'block';
            depositInfo.style.display = 'none';
        } else if (this.value === 'deposit') {
            onlinePaymentInfo.style.display = 'none';
            depositInfo.style.display = 'block';
        } else {
            onlinePaymentInfo.style.display = 'none';
            depositInfo.style.display = 'none';
        }
    });
});