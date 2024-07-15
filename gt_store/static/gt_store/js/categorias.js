document.addEventListener('DOMContentLoaded', function() {
    var categoriaField = document.getElementById('id_categoria');
    var camposEspecificos = {
        'pc': ['procesador', 'memoria_ram', 'tarjeta_video', 'almacenamiento', 'fuente_poder', 'placa_madre', 'refrigeracion', 'gabinete'],
        'notebook': ['procesador', 'memoria_ram', 'almacenamiento', 'tamano_pantalla', 'resolucion_pantalla', 'bateria'],
        'mouse': ['dpi', 'tipo_conexion', 'numero_botones', 'retroiluminacion', 'boton', 'tracking', 'sensor'],
        'teclado': ['tipo_conexion', 'tipo_teclado', 'retroiluminacion', 'distribucion'],
        'audifonos': ['tipo_conexion', 'microfono', 'tipo_auricular', 'cancelacion_ruido'],
        'procesador': ['velocidad', 'nucleos', 'hilos', 'socket'],
        'ram': ['capacidad', 'tipo_ram', 'velocidad', 'latencia'],
        'placa_madre': ['socket', 'formato', 'chipset', 'soporte_ram'],
        'tarjeta_video': ['memoria', 'tipo_memoria', 'velocidad_reloj', 'interfaz'],
        'fuente_poder': ['potencia', 'certificacion', 'modularidad'],
        'almacenamiento': ['tipo_almacenamiento', 'velocidad_lectura', 'velocidad_escritura', 'capacidad'],
        'gabinete': ['numero_bahias', 'ventilacion', 'nro_ventiladores'],
        'monitor': ['frecuencia', 'tipo_panel']
    };

    function actualizarCamposEspecificos() {
        var categoriaSeleccionada = categoriaField.value;
        var todosLosCampos = ['procesador', 'memoria_ram', 'almacenamiento', 'tarjeta_video', 'tamano_pantalla', 'resolucion_pantalla', 'bateria', 'fuente_poder', 'placa_madre', 'refrigeracion', 'gabinete', 'dpi', 'tipo_conexion', 'numero_botones', 'retroiluminacion', 'tipo_teclado', 'distribucion', 'microfono', 'tipo_auricular', 'cancelacion_ruido', 'velocidad', 'nucleos', 'hilos', 'socket', 'capacidad', 'tipo_ram', 'latencia', 'formato', 'chipset', 'soporte_ram', 'memoria', 'tipo_memoria', 'velocidad_reloj', 'interfaz', 'potencia', 'certificacion', 'modularidad', 'tipo_almacenamiento', 'velocidad_lectura', 'velocidad_escritura', 'numero_bahias', 'ventilacion', 'nro_ventiladores', 'frecuencia', 'tipo_panel',  'boton', 'tracking', 'sensor'];

        todosLosCampos.forEach(function(campo) {
            var campoElemento = document.getElementById('id_' + campo).closest('.form-row');
            if (campoElemento) {
                if (camposEspecificos[categoriaSeleccionada] && camposEspecificos[categoriaSeleccionada].includes(campo)) {
                    campoElemento.style.display = 'block';
                } else {
                    campoElemento.style.display = 'none';
                }
            }
        });
    }

    categoriaField.addEventListener('change', actualizarCamposEspecificos);
    actualizarCamposEspecificos();  // Llama a la función al cargar la página para establecer el estado inicial
});
