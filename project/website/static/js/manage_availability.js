document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const dateInput = document.getElementById('id_date');
    const startTimeInput = document.getElementById('id_start_time');
    const endTimeInput = document.getElementById('id_end_time');
    const availabilityTable = document.querySelector('table tbody');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        if (validateForm()) {
            this.submit();
        }
    });

    function validateForm() {
        const date = new Date(dateInput.value);
        const startTime = new Date(dateInput.value + 'T' + startTimeInput.value);
        const endTime = new Date(dateInput.value + 'T' + endTimeInput.value);

        if (date < new Date().setHours(0, 0, 0, 0)) {
            alert('Please select a date in the future.');
            return false;
        }

        if (startTime >= endTime) {
            alert('End time must be after start time.');
            return false;
        }

        return true;
    }

    // Add event listeners to delete buttons
    availabilityTable.addEventListener('click', function(e) {
        if (e.target.classList.contains('delete-btn')) {
            e.preventDefault();
            if (confirm('Are you sure you want to delete this availability?')) {
                window.location.href = e.target.href;
            }
        }
    });

    // Add date picker to date input
    flatpickr(dateInput, {
        minDate: "today",
        dateFormat: "Y-m-d"
    });

    // Add time picker to time inputs
    flatpickr(startTimeInput, {
        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
        time_24hr: true
    });

    flatpickr(endTimeInput, {
        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
        time_24hr: true
    });

    // Function to highlight conflicts
    function highlightConflicts() {
        const rows = availabilityTable.querySelectorAll('tr');
        rows.forEach(row => {
            row.classList.remove('conflict');
        });

        for (let i = 0; i < rows.length; i++) {
            for (let j = i + 1; j < rows.length; j++) {
                if (checkConflict(rows[i], rows[j])) {
                    rows[i].classList.add('conflict');
                    rows[j].classList.add('conflict');
                }
            }
        }
    }

    function checkConflict(row1, row2) {
        const date1 = row1.cells[0].textContent;
        const start1 = new Date(date1 + 'T' + row1.cells[1].textContent);
        const end1 = new Date(date1 + 'T' + row1.cells[2].textContent);

        const date2 = row2.cells[0].textContent;
        const start2 = new Date(date2 + 'T' + row2.cells[1].textContent);
        const end2 = new Date(date2 + 'T' + row2.cells[2].textContent);

        return date1 === date2 && ((start1 < end2 && end1 > start2) || (start2 < end1 && end2 > start1));
    }

    // Call highlightConflicts on page load
    highlightConflicts();
});