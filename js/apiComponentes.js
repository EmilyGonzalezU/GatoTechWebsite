// URL de la base de datos en tiempo real de Firebase para procesadores
const firebaseDatabaseURL = 'https://procesadores-c0ae0-default-rtdb.firebaseio.com/';

// Recupera los datos de la base de datos en tiempo real de Firebase para procesadores
fetch(`${firebaseDatabaseURL}.json`)
    .then(response => response.json())
    .then(data => {
        // Genera las filas para cada categoría de procesadores
        generarFilasProcesadores(data.procesadores.top, document.getElementById('topProcesadores'));
        generarFilasProcesadores(data.procesadores.mid, document.getElementById('midProcesadores'));
        generarFilasProcesadores(data.procesadores.low, document.getElementById('lowProcesadores'));
    })
    .catch(error => console.error('Error al recuperar los datos de Firebase (procesadores):', error));

// Función para generar las filas de la tabla de procesadores
function generarFilasProcesadores(procesadores, contenedor) {
    procesadores.forEach(procesador => {
        const fila = `
              <tr>
                  <td class="fs-9">${procesador.modelo}</td>
                  <td>${procesador.velocidad_reloj}</td>
                  <td>${procesador.num_nucleos}</td>
                  <td>${procesador.num_hilos}</td>
                  <td>${procesador.tdp}</td>
                  <td>${procesador.recomendaciones.uso_previsto}</td>
                  <td>${procesador.recomendaciones.consejos}</td>
              </tr>
          `;
        contenedor.innerHTML += fila;
    });
}

// URL de la base de datos en tiempo real de Firebase para tarjetas gráficas
const firebaseDatabaseURLVideo = 'https://video-a3760-default-rtdb.firebaseio.com/';

// Recupera los datos de la base de datos en tiempo real de Firebase para tarjetas gráficas
fetch(`${firebaseDatabaseURLVideo}.json`)
    .then(response => response.json())
    .then(data => {
        // Genera las filas para cada categoría de tarjetas gráficas
        generarFilasTarjetasVideo(data.tarjetas_video.top, document.getElementById('topVideo'));
        generarFilasTarjetasVideo(data.tarjetas_video.mid, document.getElementById('midVideo'));
        generarFilasTarjetasVideo(data.tarjetas_video.low, document.getElementById('lowVideo'));
    })
    .catch(error => console.error('Error al recuperar los datos de Firebase (tarjetas gráficas):', error));

// Función para generar las filas de la tabla de tarjetas gráficas
function generarFilasTarjetasVideo(tarjetas, contenedor) {
    tarjetas.forEach(tarjeta => {
        const fila = `
            <tr>
                <td>${tarjeta.modelo}</td>
                <td>${tarjeta.memoria}</td>
                <td>${tarjeta.velocidad_reloj}</td>
                <td>${tarjeta.ancho_banda}</td>
                <td>${tarjeta.consumo_energetico}</td>
                <td>${tarjeta.recomendaciones.uso_previsto}</td>
                <td>${tarjeta.recomendaciones.consejos}</td>
            </tr>
        `;
        contenedor.innerHTML += fila;
    });
}
