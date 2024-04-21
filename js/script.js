/*Auto show  */

$(document).ready(function(){
        // Abre el primer acordeón al cargar la página
    $('#collapseOne').collapse('show');
});

/*DSCTO disable show */
var containerDsctoTarget = document.querySelectorAll('.dsctoTarget');

containerDsctoTarget.forEach(function(dsctoTarget){
    var dscto = dsctoTarget.querySelector('.dscto'); 
    var oldPrice = dsctoTarget.querySelector('.oldPrice'); 
    
    if (dscto.textContent.trim() === '' && oldPrice.textContent.trim() === ''){
        dsctoTarget.style.display = 'none';
        dscto.style.display = 'none';
        oldPrice.style.display = 'none'; 
    } else {
        dsctoTarget.style.display = 'block'; 
        dscto.style.display = 'block';
        oldPrice.style.display = 'block';
    }
});

/**TRUNC TEXT FUNCTION */
document.addEventListener("DOMContentLoaded", function() { /*DOM CARGADO EJECUTA FUNCION*/
    var productDescriptions = document.querySelectorAll('.productDesc');

    productDescriptions.forEach(function(productDesc) {
        if (productDesc.textContent.length > 50) {
            productDesc.textContent = productDesc.textContent.substring(0, 50) + '...';
        }
    });
});

/**Mega Mennu */

