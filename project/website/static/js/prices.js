document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('modal');
    const modalTitle = document.getElementById('modal-title');
    const modalDescription = document.getElementById('modal-description');
    const closeBtn = document.getElementsByClassName('close')[0];
    const bookNowBtns = document.querySelectorAll('.book-now-btn');

    const serviceDetails = {
        'sesion-fotos': {
            title: 'Sesión de Fotos',
            description: 'Captura momentos especiales con nuestra sesión de fotos profesional. Ideal para retratos, familias, o cualquier ocasión que quieras inmortalizar.'
        },
        'boda': {
            title: 'Fotografía de Boda',
            description: 'Preserva los recuerdos de tu día especial con nuestro servicio de fotografía de bodas. Cubrimos todos los momentos importantes, desde la preparación hasta la recepción.'
        },
        'producto': {
            title: 'Fotografía de Producto',
            description: 'Destaca tus productos con fotografías de alta calidad. Ideal para catálogos, tiendas en línea y material publicitario. Resaltamos las mejores características de tus productos.'
        },
        'video-evento': {
            title: 'Video de Evento',
            description: 'Inmortaliza tu evento con un video profesional. Perfecto para bodas, cumpleaños, conferencias y más. Creamos un resumen emotivo y dinámico de tu ocasión especial.'
        },
        'video-corporativo': {
            title: 'Video Corporativo',
            description: 'Proyecta una imagen profesional de tu empresa con nuestros videos corporativos. Ideal para presentaciones, marketing y comunicación interna.'
        },
        'edicion-video': {
            title: 'Edición de Video',
            description: 'Transforma tu material en bruto en un video profesional y atractivo. Ofrecemos edición, corrección de color, y adición de efectos y música.'
        },
        'proyecto-digital': {
            title: 'Proyecto Digital',
            description: 'Desarrollamos proyectos digitales personalizados que integran fotografía, video y diseño. Ideal para campañas de marketing, presentaciones interactivas y más.'
        }
    };

    bookNowBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const service = this.closest('.service-card').dataset.service;
            const details = serviceDetails[service];
            modalTitle.textContent = details.title;
            modalDescription.textContent = details.description;
            modal.style.display = 'block';
        });
    });

    closeBtn.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
});