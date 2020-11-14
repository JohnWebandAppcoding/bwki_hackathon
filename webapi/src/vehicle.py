import math
import requests

class car():

    def weather_data(query):
        res = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?' + query + '&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
        return res.json();

    def get_wind(self,result,city):
        wind_spd = (result['wind']['speed'])
        return wind_spd

    def __init__(self):
        city = "Papenburg"
        try:
            query = 'q=' + city;
            wind = self.weather_data(query);
        except:
            print('City name not found...')
        self.name = "Ford Fiesta JD3"
        self.mass = 1112
        self.acceleration = 0
        self.coeff_roll_R = 0.06
        self.air_density = 1.225
        self.front_are = 1.7
        self.aero_drag_coeff = 0.5
        self.wind_speed = self.get_wind(wind,city)
        self.road_angle = 0
        self.co2 = 144

    def emission(self,angle, V):
        self.road_angle = angle
        rad = math.radians(angle)
        p1 = (self.mass * self.acceleration) * (self.mass * 9.8 * self.coeff_roll_R * math.cos(rad))
        p2 = 0.5 * self.air_density * self.front_area * self.aero_drag_coeff * ((V - self.wind_speed)**2)
        p3 = self.mass * 9.8 * math.sin(rad)
        p = p1 + p2 + p3 * V
        emissions = p * self.co2
        return emissions

