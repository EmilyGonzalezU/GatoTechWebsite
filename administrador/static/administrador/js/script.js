

// Owl carousel resposivo
$(document).ready(function() { 
    $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 10,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
                nav: true
            },
            576: {
                items: 2,
                nav: false
            },
            768: {
                items: 3,
                nav: false
            },
            992: {
                items: 4,
                nav: false
            },
            1200: {
                items: 5,
                nav: false,
                loop: false
            }
        }
    })
});

// Auto show filtros

$(document).ready(function(){
    $('#collapseOne').collapse('show');
});

// Trunc text
document.addEventListener("DOMContentLoaded", function() { /*DOM CARGADO EJECUTA FUNCION*/
    var productDescriptions = document.querySelectorAll('.productDesc');

    productDescriptions.forEach(function(productDesc) {
        if (productDesc.textContent.length > 50) {
            productDesc.textContent = productDesc.textContent.substring(0, 50) + '...';
        }
    });
});