document.addEventListener('DOMContentLoaded', function() {
  const marcaCheckboxes = document.querySelectorAll('.marca');
  const fabricanteCheckboxes = document.querySelectorAll('.fabricante');
  const tipoCheckboxes = document.querySelectorAll('.tipo');
  const sensorCheckboxes = document.querySelectorAll('.sensor');
  const cardProducts = document.querySelectorAll('.position-relative.col-lg-3'); //card
  const precioCheckboxes = document.querySelectorAll('.rango-precio');

  marcaCheckboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', filterProducts);
  });

  fabricanteCheckboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', filterProducts);
  });

  tipoCheckboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', filterProducts);
  });

  sensorCheckboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', filterProducts);
  });

  precioCheckboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', filterProducts);
  });

  function filterProducts() {
    const marcaSelected = option('.marca');
    const fabricanteSelected = option('.fabricante');
    const tipoSelected = option('.tipo');
    const sensorSelected = option('.sensor');
    const precioSelected = optionPrecio();

    cardProducts.forEach(function(card) {
      const marcaProduct = card.querySelector('.card').dataset.marca;
      const fabricanteProduct = card.querySelector('.card').dataset.fabricante;
      const tipoProduct = card.querySelector('.card').dataset.tipo;
      const sensorProduct = card.querySelector('.card').dataset.sensor;

      // Aquí tomamos todos los precios del producto
      const priceElements = card.querySelectorAll('.price');
      const preciosProducto = Array.from(priceElements).map(priceEl =>
        parseFloat(priceEl.textContent.replace(/\$|\./g, ''))
      );

      const marcaValid = marcaSelected.length === 0 || marcaSelected.includes(marcaProduct);
      const fabricanteValid = fabricanteSelected.length === 0 || fabricanteSelected.includes(fabricanteProduct);
      const tipoValid = tipoSelected.length === 0 || tipoSelected.includes(tipoProduct);
      const sensorValid = sensorSelected.length === 0 || sensorSelected.includes(sensorProduct);
      
      let precioValid = precioSelected.length === 0;

      preciosProducto.forEach(precioProduct => {
        precioSelected.forEach(range => {
          const [min, max] = range.split('-').map(Number);
          if (precioProduct >= min && precioProduct <= max) {
            precioValid = true;
          }
        });
      });

      if (marcaValid && fabricanteValid && tipoValid && sensorValid && precioValid) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  function option(selector) {
    const optionsSelected = [];
    const checkboxes = document.querySelectorAll(selector);
    checkboxes.forEach(function(checkbox) {
      if (checkbox.checked) {
        optionsSelected.push(checkbox.dataset[selector.slice(1)]);
      }
    });
    return optionsSelected;
  }

  function optionPrecio() {
    const selectedRanges = [];
    precioCheckboxes.forEach(function(checkbox) {
      if (checkbox.checked) {
        selectedRanges.push(checkbox.value);
      }
    });
    return selectedRanges;
  }
});
