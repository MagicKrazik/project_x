// media.js

document.addEventListener('DOMContentLoaded', function() {
    const featureCards = document.querySelectorAll('.feature-card[data-preview]');
    const overlayPreview = document.getElementById('overlayPreview');
    const previewImage = document.getElementById('previewImage');
    const previewVideo = document.getElementById('previewVideo');
    const closeButton = document.querySelector('.close-button');
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');

    let currentMediaType = '';
    let currentIndex = 0;

    featureCards.forEach(card => {
        card.addEventListener('click', () => {
            const previewType = card.dataset.preview;
            openPreview(previewType);
        });
    });

    closeButton.addEventListener('click', closePreview);

    prevButton.addEventListener('click', () => navigateMedia(-1));
    nextButton.addEventListener('click', () => navigateMedia(1));

    function openPreview(type) {
        currentMediaType = type;
        currentIndex = 0;
        showMedia();
        overlayPreview.style.display = 'flex';
    }

    function closePreview() {
        overlayPreview.style.display = 'none';
        previewVideo.pause();
        previewVideo.currentTime = 0;
    }

    function showMedia() {
        const mediaUrl = window.previewMedia[currentMediaType][currentIndex];
        
        if (mediaUrl.endsWith('.mp4')) {
            previewImage.style.display = 'none';
            previewVideo.style.display = 'block';
            previewVideo.src = mediaUrl;
        } else {
            previewImage.style.display = 'block';
            previewVideo.style.display = 'none';
            previewImage.src = mediaUrl;
        }
    }

    function navigateMedia(direction) {
        const mediaArray = window.previewMedia[currentMediaType];
        currentIndex = (currentIndex + direction + mediaArray.length) % mediaArray.length;
        showMedia();
    }

    // Keyboard navigation
    document.addEventListener('keydown', function(event) {
        if (overlayPreview.style.display === 'flex') {
            switch(event.key) {
                case 'ArrowLeft':
                    navigateMedia(-1);
                    break;
                case 'ArrowRight':
                    navigateMedia(1);
                    break;
                case 'Escape':
                    closePreview();
                    break;
            }
        }
    });
});