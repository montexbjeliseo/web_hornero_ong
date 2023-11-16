const showImage = ({ image }) => {
    const modal = document.createElement('div');
    modal.classList.add('custom-modal');

    const img = document.createElement('img');
    img.src = image;
    img.classList.add('gallery-image-fluid');

    modal.appendChild(img);

    const cerrarModal = () => modal.parentNode.removeChild(modal);

    const aceptarBoton = document.createElement('button');
    aceptarBoton.textContent = 'Volver';
    aceptarBoton.classList.add('btn', 'btn-secondary');
    aceptarBoton.addEventListener('click', cerrarModal);
    modal.addEventListener('click', cerrarModal);
    modal.appendChild(aceptarBoton);

    document.body.appendChild(modal);
}

const configureGallery = () => {
    const galleryImages = document.querySelectorAll('.gallery-image');
    galleryImages.forEach(image => {
        image.addEventListener('click', () => {
            showImage({ image: image.src })
        })
    });
}

(() => document.addEventListener('DOMContentLoaded', configureGallery))();