import requests

class OpenWeatherMapAPI:
    """
    Classe para interagir com a API OpenWeatherMap e obter informações meteorológicas.
    """

    def __init__(self, api_key):
        """
        Inicializa a instância da classe.

        Parâmetros:
        - api_key (str): Chave de API para autenticação na OpenWeatherMap.
        """
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"

    def get_current_weather(self, city_name, units="metric"):
        """
        Obtém as informações meteorológicas atuais para uma cidade.

        Parâmetros:
        - city_name (str): Nome da cidade para a qual obter a previsão do tempo.
        - units (str): Unidade de medida para as informações meteorológicas (padrão: "metric").

        Retorna:
        dict: Dados da condição meteorológica atual em formato JSON.
        """
        endpoint = f"{self.base_url}/weather"
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": units
        }
        response = requests.get(endpoint, params=params)
        data = response.json()
        return data

    def get_forecast(self, city_name, days=7, units="metric"):
        """
        Obtém a previsão do tempo para uma cidade nos próximos dias.

        Parâmetros:
        - city_name (str): Nome da cidade para a qual obter a previsão do tempo.
        - days (int): Número de dias para a previsão (padrão: 7).
        - units (str): Unidade de medida para as informações meteorológicas (padrão: "metric").

        Retorna:
        list: Lista de dados de previsão do tempo para cada dia em formato JSON.
        """
        endpoint = f"{self.base_url}/forecast"
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": units
        }
        response = requests.get(endpoint, params=params)
        data = response.json()
        forecast_data = data["list"][:days]
        return forecast_data

    def get_weather_by_coordinates(self, lat, lon, units="metric"):
        """
        Obtém as informações meteorológicas para uma localização específica através de coordenadas.

        Parâmetros:
        - lat (float): Latitude da localização.
        - lon (float): Longitude da localização.
        - units (str): Unidade de medida para as informações meteorológicas (padrão: "metric").

        Retorna:
        dict: Dados da condição meteorológica em formato JSON.
        """
        endpoint = f"{self.base_url}/weather"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": units
        }
        response = requests.get(endpoint, params=params)
        data = response.json()
        return data

    def get_historical_weather(self, city_name, date, units="metric"):
        """
        Obtém as informações meteorológicas históricas para uma cidade e data específicas.

        Parâmetros:
        - city_name (str): Nome da cidade para a qual obter as informações históricas.
        - date (int): Timestamp da data para a qual obter as informações históricas.
        - units (str): Unidade de medida para as informações meteorológicas (padrão: "metric").

        Retorna:
        dict: Dados da condição meteorológica histórica em formato JSON.
        """
        endpoint = f"{self.base_url}/onecall/timemachine"
        params = {
            "q": city_name,
            "dt": date,
            "appid": self.api_key,
            "units": units
        }
        response = requests.get(endpoint, params=params)
        data = response.json()
        return data

if __name__ == "__main__":
    api_key = "e372837973594d5ec420db445a2f17f7"
    weather_api = OpenWeatherMapAPI(api_key)

    city_name = str(input("Digite o nome da cidade"))

    current_weather = weather_api.get_current_weather(city_name)
    print("Condição atual do tempo em", city_name, ":", current_weather["weather"][0]["description"])
    print("Temperatura atual:", current_weather["main"]["temp"], "°C")

    forecast = weather_api.get_forecast(city_name, days=7)
    print("\nPrevisão para os próximos 7 dias:")
    for day in forecast:
        date = day["dt_txt"]
        temp = day["main"]["temp"]
        description = day["weather"][0]["description"]
        print(f"{date}: {description}, {temp} °C")
