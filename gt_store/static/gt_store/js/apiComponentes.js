const firebaseDatabaseURL = 'https://procesadores-c0ae0-default-rtdb.firebaseio.com/';

fetch(`${firebaseDatabaseURL}.json`)
    .then(response => response.json())
    .then(data => {
        generarFilasProcesadores(data.procesadores.top, document.getElementById('topProcesadores'));
        generarFilasProcesadores(data.procesadores.mid, document.getElementById('midProcesadores'));
        generarFilasProcesadores(data.procesadores.low, document.getElementById('lowProcesadores'));
    })
    .catch(error => console.error('Error al recuperar los datos de Firebase (procesadores):', error));

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

const firebaseDatabaseURLVideo = 'https://video-a3760-default-rtdb.firebaseio.com/';

fetch(`${firebaseDatabaseURLVideo}.json`)
    .then(response => response.json())
    .then(data => {
        generarFilasTarjetasVideo(data.tarjetas_video.top, document.getElementById('topVideo'));
        generarFilasTarjetasVideo(data.tarjetas_video.mid, document.getElementById('midVideo'));
        generarFilasTarjetasVideo(data.tarjetas_video.low, document.getElementById('lowVideo'));
    })
    .catch(error => console.error('Error al recuperar los datos de Firebase (tarjetas gráficas):', error));

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
