var map = L.map('map').setView([0, 0], 2);  // Configurar mapa inicial com visualização padrão

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// ...

document.getElementById('location-form').addEventListener('submit', function (e) {
    e.preventDefault();

    var location = document.getElementById('location').value;

    fetch(`/previsao?cidade=${location}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('city-name').textContent = data.name;
            var countryCode = data.sys.country;
            var flagElement = document.getElementById('country-flag');
            flagElement.innerHTML = `<span class="flag-icon flag-icon-${countryCode.toLowerCase()}"></span>`;
            document.getElementById('temperature').textContent = data.main.temp;

            // Obtenha a descrição da condição climática
            var conditions = data.weather[0].description;
            document.getElementById('conditions').textContent = conditions;

            // Use as classes de ícones de clima do "Weather Icons" para exibir o ícone correspondente
            var weatherIconClass = getWeatherIconClass(conditions);
            var weatherIconElement = document.getElementById('weather-icon');
            weatherIconElement.className = weatherIconClass;

            map.setView([data.coord.lat, data.coord.lon], 10);
        })
        .catch(error => {
            alert('Não foi possível obter a previsão do tempo. Certifique-se de que a cidade esteja correta.');
            console.error(error);
        });
});

// Função para mapear as condições climáticas para classes de ícones de clima do "Weather Icons"
function getWeatherIconClass(conditions) {
    conditions = conditions.toLowerCase();

    if (conditions.includes('rain')) {
        return 'wi wi-rain';
    } else if (conditions.includes('cloud')) {
        return 'wi wi-cloudy';
    } else if (conditions.includes('clear')) {
        return 'wi wi-day-sunny';
    } else {
        return 'wi wi-day-sunny'; // Ícone padrão
    }
}

// ...
