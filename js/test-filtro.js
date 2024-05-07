document.addEventListener('DOMContentLoaded', function() {
  const marcaCheckbox = document.querySelectorAll('.marcaMouse');
  const sensorCheckbox = document.querySelectorAll('.sensorMouse');
  const productos = document.querySelectorAll('.card');


  [marcaCheckbox, sensorCheckbox].forEach(function(checkboxes) {
    checkboxes.forEach(function(checkbox) {
      checkbox.addEventListener('change', function() {
        filtrarProductos();
      });
    });
  });

  function filtrarProductos() {
    const marcaSelect = obtenerOpc('.marcaMouse');
    const sensorSelect = obtenerOpc('.sensorMouse');

    productos.forEach(function(producto) {
      const marcaProducto = producto.dataset.marca;
      const sensorProducto = producto.dataset.sensor;

      const marcaValida = marcaSelect.length === 0 || marcaSelect.includes(marcaProducto);
      const sensorValido = sensorSelect.length === 0 || sensorSelect.includes(sensorProducto);

      if (marcaValida && sensorValido) {
        producto.style.display = 'block';
      } else {
        producto.style.display = 'none';
      }
    });
  }

  function obtenerOpc(selector) {
    const opcSelect = [];
    const checkboxes = document.querySelectorAll(selector);
    checkboxes.forEach(function(checkbox) {
      if (checkbox.checked) {
        opcSelect.push(checkbox.dataset.marca);
      }
    });
    return opcSelect;
  }
});
