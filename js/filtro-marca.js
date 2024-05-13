document.addEventListener('DOMContentLoaded', function() {
  const marcaCheckboxes = document.querySelectorAll('.marca');
  const cardProducts = document.querySelectorAll('.position-relative.col-lg-3');

  marcaCheckboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
      filterProducts();
    });
  });

  function filterProducts() {
    const marcaSelected = option('.marca');

    cardProducts.forEach(function(card) {
      const marcaProduct = card.querySelector('.card').dataset.marca;

      const marcaValid = marcaSelected.length === 0 || marcaSelected.includes(marcaProduct);

      if (marcaValid) {
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
        optionsSelected.push(checkbox.dataset.marca); 
      }
    });
    return optionsSelected;
  }
});
