document.addEventListener('DOMContentLoaded', function() {
    const userTableBody = document.getElementById('userTableBody');
    const activationModal = document.getElementById('activationModal');
    const activationUsername = document.getElementById('activationUsername');
    const confirmActivation = document.getElementById('confirmActivation');
    const cancelActivation = document.getElementById('cancelActivation');

    let currentUserId = null;

    // Activation/Deactivation functionality
    userTableBody.addEventListener('click', function(e) {
        if (e.target.classList.contains('btn-activate')) {
            currentUserId = e.target.dataset.userId;
            const username = e.target.closest('tr').cells[0].textContent;
            activationUsername.textContent = username;
            activationModal.style.display = 'block';
        } else if (e.target.classList.contains('btn-deactivate')) {
            deactivateUser(e.target.dataset.userId);
        }
    });

    confirmActivation.addEventListener('click', function() {
        activateUser(currentUserId);
        activationModal.style.display = 'none';
    });

    cancelActivation.addEventListener('click', function() {
        activationModal.style.display = 'none';
    });

    function activateUser(userId) {
        fetch(`/admin_panel/manage-users/activate/${userId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                updateUserRow(userId, true, data.activation_date, data.renewal_date, data.days_left);
                alert(data.message);
            } else {
                alert('Error activating user. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    }

    function deactivateUser(userId) {
        fetch(`/admin_panel/manage-users/deactivate/${userId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                updateUserRow(userId, false);
                alert(data.message);
            } else {
                alert('Error deactivating user. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    }

    function updateUserRow(userId, isActive, activationDate, renewalDate, daysLeft) {
        const row = document.querySelector(`tr[data-user-id="${userId}"]`);
        const statusCell = row.cells[3];
        const activationDateCell = row.cells[4];
        const renewalDateCell = row.cells[5];
        const daysLeftCell = row.cells[6];
        const actionCell = row.cells[7];

        statusCell.innerHTML = isActive ? '<span class="status-active">Activo</span>' : '<span class="status-inactive">Inactivo</span>';
        
        if (isActive) {
            activationDateCell.textContent = activationDate;
            renewalDateCell.textContent = renewalDate;
            daysLeftCell.textContent = daysLeft + ' días';
        } else {
            // Keep the existing dates for deactivated users
            daysLeftCell.textContent = 'N/A';
        }

        actionCell.innerHTML = isActive ? 
            `<button class="btn btn-deactivate" data-user-id="${userId}">Desactivar</button>` :
            `<button class="btn btn-activate" data-user-id="${userId}">Activar</button>`;
    }

    // Helper function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});