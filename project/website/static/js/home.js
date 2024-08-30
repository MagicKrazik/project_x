document.addEventListener('DOMContentLoaded', function() {
    const ageVerification = document.getElementById('age-verification');
    const agreeButton = document.getElementById('agree-button');
    const declineButton = document.getElementById('decline-button');
    const contentWrapper = document.querySelector('.home-container');
    const featureCards = document.querySelectorAll('.feature-card');
    const previewOverlay = document.getElementById('previewOverlay');
    const previewContainer = document.getElementById('previewContainer');
    const previewImage = document.getElementById('previewImage');
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');
    const closeButton = document.querySelector('.close-button');

    let currentImages = [];
    let currentIndex = 0;

    if (!ageVerification || !agreeButton || !declineButton || !contentWrapper || !previewOverlay || !previewContainer || !closeButton || !previewImage || !prevButton || !nextButton) {
        console.error('One or more required elements are missing.');
        return;
    }

    function showAgeVerification() {
        ageVerification.style.display = 'flex';
        document.body.classList.add('body-blur');
    }

    function hideAgeVerification() {
        ageVerification.style.display = 'none';
        document.body.classList.remove('body-blur');
    }

    agreeButton.addEventListener('click', function() {
        hideAgeVerification();
        localStorage.setItem('ageVerified', 'true');
    });

    declineButton.addEventListener('click', function() {
        window.location.href = 'https://www.google.com';
    });

    // Show age verification immediately
    showAgeVerification();

    // Only hide age verification if previously verified
    if (localStorage.getItem('ageVerified') === 'true') {
        hideAgeVerification();
    }

    function showImage(index) {
        if (index >= 0 && index < currentImages.length) {
            previewImage.src = currentImages[index];
            currentIndex = index;
            updateNavigationButtons();
        }
    }

    function updateNavigationButtons() {
        prevButton.disabled = currentIndex === 0;
        nextButton.disabled = currentIndex === currentImages.length - 1;
    }

    prevButton.addEventListener('click', () => showImage(currentIndex - 1));
    nextButton.addEventListener('click', () => showImage(currentIndex + 1));

    featureCards.forEach(card => {
        card.addEventListener('click', () => {
            const previewType = card.dataset.preview;
            if (previewType && window.previewImages && window.previewImages[previewType]) {
                currentImages = window.previewImages[previewType];
                showImage(0);
                previewOverlay.style.display = 'flex';
                document.body.style.overflow = 'hidden'; // Prevent scrolling when overlay is open
            }
        });
    });

    function closeOverlay() {
        previewOverlay.style.display = 'none';
        document.body.style.overflow = ''; // Re-enable scrolling
    }

    closeButton.addEventListener('click', closeOverlay);

    previewOverlay.addEventListener('click', (e) => {
        if (e.target === previewOverlay) {
            closeOverlay();
        }
    });

    const reviewsContainer = document.getElementById('reviewsContainer');

    // Sample review data (you can replace this with actual data from your backend)
    const reviews = [
        { name: "Juan D.", date: "2024-08-15", rating: 5, content: "¡Contenido increíble! Sofía es asombrosa y su personalidad brilla en cada publicación." },
        { name: "Anonimo", date: "2024-08-10", rating: 4, content: "Gran variedad de contenido. ¡Siempre estoy esperando nuevas actualizaciones!" },
        { name: "Alejandro", date: "2024-08-05", rating: 5, content: "Ya era hora de que se profesionalizara este tipo de servicios." },
        { name: "Luis", date: "2024-07-30", rating: 4, content: "No mas perder depositos y que me dejen plantado...aqui vas a la segura." }
    ];

    function createStarRating(rating) {
        let stars = '';
        for (let i = 1; i <= 5; i++) {
            if (i <= rating) {
                stars += '<i class="fas fa-star"></i>';
            } else {
                stars += '<i class="far fa-star"></i>';
            }
        }
        return stars;
    }

    function formatDate(dateString) {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(dateString).toLocaleDateString(undefined, options);
    }

    reviews.forEach(review => {
        const reviewCard = document.createElement('div');
        reviewCard.className = 'review-card';
        reviewCard.innerHTML = `
            <div class="review-header">
                <span class="reviewer-name">${review.name}</span>
                <span class="review-date">${formatDate(review.date)}</span>
            </div>
            <div class="review-stars">${createStarRating(review.rating)}</div>
            <p class="review-content">${review.content}</p>
        `;
        reviewsContainer.appendChild(reviewCard);
    });
});