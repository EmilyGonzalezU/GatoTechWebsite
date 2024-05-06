document.addEventListener('DOMContentLoaded', function() {
  const marcaCheckboxes = document.querySelectorAll('.marcaMouse');
  const categoriaCheckboxes = document.querySelectorAll('.categoriaMouse');
  const precioCheckboxes = document.querySelectorAll('.precioMouse');
  const productos = document.querySelectorAll('.producto');

  marcaCheckboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
      filtrarProductos();
    });
  });

  categoriaCheckboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
      filtrarProductos();
    });
  });

  precioCheckboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
      filtrarProductos();
    });
  });

  function filtrarProductos() {
    const marcasSeleccionadas = obtenerOpcionesSeleccionadas('.marcaMouse');
    const categoriasSeleccionadas = obtenerOpcionesSeleccionadas('.categoriaMouse');
    const preciosSeleccionados = obtenerOpcionesSeleccionadas('.precioMouse');

    productos.forEach(function(producto) {
      const marcaProducto = producto.dataset.marca;
      const categoriaProducto = producto.dataset.categoria;
      const precioProducto = producto.dataset.precio;

      const marcaValida = marcasSeleccionadas.length === 0 || marcasSeleccionadas.includes(marcaProducto);
      const categoriaValida = categoriasSeleccionadas.length === 0 || categoriasSeleccionadas.includes(categoriaProducto);
      const precioValido = preciosSeleccionados.length === 0 || preciosSeleccionados.includes(precioProducto);

      if (marcaValida && categoriaValida && precioValido) {
        producto.style.visibility = 'visible';
      } else {
        producto.style.visibility = 'hidden';
      }
    });
  }

  function obtenerOpcionesSeleccionadas(selector) {
    const opcionesSeleccionadas = [];
    const checkboxes = document.querySelectorAll(selector);
    checkboxes.forEach(function(checkbox) {
      if (checkbox.checked) {
        opcionesSeleccionadas.push(checkbox.value);
      }
    });
    return opcionesSeleccionadas;
  }
});
