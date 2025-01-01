import requests

class WeatherAPI:
    def __init__(self, access_key):
        self.url = "http://api.weatherapi.com/v1/current.json" # weather.com adligimiz API
        self.access_key = access_key

    def get_weather(self,city):
        response = requests.get(self.url, params={ # parametrleri
            "key": self.access_key,
            "q": city,
            "lang": "AZ"
        })

        if response.status_code == 200:
            return response.json() # eger status codu ugurludsa bise json deyerlrini qaytracaq
        
        else:
            print("xeta bas verdi.ERROR CODE:response.status_code") 
            return None
        
class Weather_trasnlator:
    def __init__(self):
        # API ile avtomatik azeri diiline cevrilmediyi ucun elle yazilib
        self.translation_dict = {
            
            "Clear":"aciq hava",
            "Partly Cloudy":"qismen buludlu",
            "Cloudy":"buludlu",
            "Rainy":"yagisli",
            "Sunny":"gunesli",
            "Windy":"yelledir az maz",
            "Patchy rain nearby":"hardasa babat leysan gedir"
        }        
        
    def translate_condition(self, condition):
        return self.translation_dict.get(condition, f"{condition}")
    
class Weather_add:
    def __init__(self,acceskey):
        self.weather_api = WeatherAPI(acceskey)  
        self.weather_translator = Weather_trasnlator()

    def to_start(self):
        city = input("Seher daxil edin>>")
        result = self.weather_api.get_weather(city)

        if result:
            city_name = result["location"]["name"]
            city_temprature = result["current"]["temp_c"]
            condition_text = result["current"]["condition"]["text"]
            local_time = result["location"]["localtime"]
            contion_text_add = self.weather_translator.translate_condition(condition_text)

            print(f"seher adi:{city_name}")
            print(f"Hazirki tempuratr:{city_temprature} °C")
            print(f"Saat:{local_time}")
            print(f"hava ile bagli werh:{contion_text_add}")

if __name__ == "__main__":
    accesskey = "fec541a967a5476f836184125250101"
    Weather_add = Weather_add(accesskey)
    Weather_add.to_start()
