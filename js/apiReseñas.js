fetch('https://crafty-eye-422318-n9-default-rtdb.firebaseio.com/reviews.json')
  .then(response => response.json())
  .then(data => {
    const reseñasContainer = $('#slick-carousel-reviews');
    data.forEach(reseña => {
      const reseñaElement = `
        <div class="card mb-5 mt-5 ms-2" style="width: 27vwpx; height:25vh ;">
          <div class="card-body">
            <h5 class="card-title">${reseña.name}</h5>
            <div class="estrellas">
              ${crearEstrellas(reseña.calificacion)}
            </div>
            <p class="card-text">${reseña.comentario}</p>
          </div>
        </div>
      `;
      reseñasContainer.append(reseñaElement);
    });
    // Inicializar Slick Carousel después de cargar las reseñas
    reseñasContainer.slick({
      slidesToShow: 4,
      slidesToScroll: 1,
	  arrows: false,
      autoplay: true,
      autoplaySpeed: 2000,
      responsive: [
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 2
          }
        },
        {
          breakpoint: 576,
          settings: {
            slidesToShow: 1
          }
        }
      ]
    });
  })
  .catch(error => {
    console.error('Error al obtener las reseñas:', error);
  });

function crearEstrellas(calificación) {
  let estrellasHtml = '';
  for (let i = 1; i <= 5; i++) {
    if (i <= calificación) {
      estrellasHtml += '<i class="fas fa-star estrella text-warning"></i>';
    } else {
      estrellasHtml += '<i class="far fa-star estrella  text-warning"></i>';
    }
  }
  return estrellasHtml;
}
