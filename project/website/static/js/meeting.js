document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var dateInput = document.getElementById('id_date');
    var timeInput = document.getElementById('id_time');
    var meetingTypeSelect = document.getElementById('id_meeting_type');
    var locationSelect = document.getElementById('id_location');
    var paymentMethodSelect = document.getElementById('id_payment_method');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        selectable: true,
        select: function(info) {
            dateInput.value = info.startStr;
            updateAvailableTimes(info.startStr);
        },
        validRange: function(nowDate) {
            return {
                start: nowDate,
                end: new Date(nowDate.getFullYear(), nowDate.getMonth(), nowDate.getDate() + 30)
            };
        },
        events: availableDates.map(date => ({
            start: date,
            display: 'background',
            color: '#90EE90'
        }))
    });
    calendar.render();

    function updateAvailableTimes(date) {
        fetch(`/api/available-times/${date}/`)
            .then(response => response.json())
            .then(data => {
                timeInput.innerHTML = '';
                data.times.forEach(time => {
                    var option = document.createElement('option');
                    option.value = time;
                    option.textContent = time;
                    timeInput.appendChild(option);
                });
            });
    }

    meetingTypeSelect.addEventListener('change', function() {
        if (this.value === 'video') {
            locationSelect.disabled = true;
            locationSelect.value = '';
        } else {
            locationSelect.disabled = false;
        }
    });

    paymentMethodSelect.addEventListener('change', function() {
        var onlinePaymentInfo = document.getElementById('online-payment');
        var depositInfo = document.getElementById('deposit-info');

        if (this.value === 'deposit') {
            onlinePaymentInfo.classList.add('hidden');
            depositInfo.classList.remove('hidden');
        } else if (this.value === 'online') {
            depositInfo.classList.add('hidden');
            onlinePaymentInfo.classList.remove('hidden');
        } else {
            onlinePaymentInfo.classList.add('hidden');
            depositInfo.classList.add('hidden');
        }
    });

    document.querySelector('form').addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Perform form validation here
        var isValid = validateForm();
        
        if (isValid) {
            this.submit();
        }
    });

    function validateForm() {
        // Add your form validation logic here
        // Return true if the form is valid, false otherwise
        return true;
    }
});