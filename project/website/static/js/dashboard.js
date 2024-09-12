document.addEventListener('DOMContentLoaded', function() {
    // Animate count up for numbers
    const countElements = document.querySelectorAll('.count');
    countElements.forEach(element => {
        if (element.id === 'profit') {
            const profit = parseInt(element.textContent.replace(/[^0-9]/g, ''));
            animateProfit(element, 0, profit, 2000);
        } else {
            const target = parseInt(element.textContent);
            animateCount(element, 0, target, 2000);
        }
    });
});

function animateCount(element, start, end, duration) {
    let current = start;
    const range = end - start;
    const increment = Math.ceil(range / (duration / 16)); // 60 FPS
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= end) {
            current = end;
            clearInterval(timer);
        }
        element.textContent = current;
    }, 16);
}

function animateProfit(element, start, end, duration) {
    let current = start;
    const range = end - start;
    const increment = Math.ceil(range / (duration / 16)); // 60 FPS
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= end) {
            current = end;
            clearInterval(timer);
        }
        element.textContent = '$' + current.toLocaleString() + ' MXN';
    }, 16);
}

// Refresh dashboard data every 5 minutes
setInterval(fetchDashboardData, 300000);

function fetchDashboardData() {
    // Replace this with actual AJAX call to fetch updated data
    console.log('Fetching updated dashboard data...');
    // Example AJAX call:
    // fetch('/admin_panel/api/dashboard-data/')
    //     .then(response => response.json())
    //     .then(data => {
    //         animateCount(document.querySelector('.total-users .count'), parseInt(document.querySelector('.total-users .count').textContent), data.total_users, 1000);
    //         animateCount(document.querySelector('.active-users .count'), parseInt(document.querySelector('.active-users .count').textContent), data.active_users, 1000);
    //         animateProfit(document.querySelector('#profit'), parseInt(document.querySelector('#profit').textContent.replace(/[^0-9]/g, '')), data.estimated_profit, 1000);
    //         // Update recent activity
    //         const activityList = document.getElementById('activity-list');
    //         activityList.innerHTML = '';
    //         data.recent_activity.forEach(activity => {
    //             const li = document.createElement('li');
    //             li.textContent = `Nuevo usuario registrado: ${activity.username} (${activity.date_joined})`;
    //             activityList.appendChild(li);
    //         });
    //     })
    //     .catch(error => console.error('Error fetching dashboard data:', error));
}