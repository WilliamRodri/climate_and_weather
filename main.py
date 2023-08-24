from geopy.geocoders import Nominatim
import requests
import pandas as pd

locationGeo = input("Digite sua Cidade<Ex. Fortaleza-CE> : ")

geolocator = Nominatim(user_agent="geoCoders")
location = geolocator.geocode(locationGeo)

lat = location.latitude
lon = location.longitude
API_key = 'f4b18aed5a17c8d04bedd4d6d985006f'

headers = {'Accept': 'application/json'}
URL = f'https://api.hgbrasil.com/weather?key=265756fb&lat={lat}&lon={lon}'

#print(URL)
requests = requests.get(URL, headers=headers)
#print(requests.status_code)

api_data_results = requests.json()['results']

api_data_forecast_1 = api_data_results['forecast'][0]
api_data_forecast_2 = api_data_results['forecast'][1]
api_data_forecast_3 = api_data_results['forecast'][2]
api_data_forecast_4 = api_data_results['forecast'][3]
api_data_forecast_5 = api_data_results['forecast'][4]

lista = {
    0: api_data_forecast_1,
    1: api_data_forecast_2,
    2: api_data_forecast_3,
    3: api_data_forecast_4,
    4: api_data_forecast_4,
}

for i in lista:
    df = pd.DataFrame(lista[i], index=[0], columns=['date', 'weekday', 'condition', 'description', 'rain_probability'])
    df = df.rename(columns={'date': 'Data', 'weekday': 'Dia', 'condition': 'Condição', 'description': 'Descrição', 'rain_probability': 'Probabilidade de Chuva'})
    df = df.to_string(index=False)
    print(df)