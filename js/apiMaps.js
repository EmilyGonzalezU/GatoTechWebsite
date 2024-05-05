window.initMap = function (){
    const coords = {lat:-33.01015830516158, lng:-71.54569002393927};
    const map = new google.maps.Map(document.getElementById('map'),{
      zoom: 15,
      center: coords
    });
    const marker = new google.maps.Marker({
      position: coords,
      map: map,
    });
}