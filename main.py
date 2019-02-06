# -*- coding: UTF-8 -*-
import requests
import json

'''Openweather map api is a free api which can get the weather situation
    For the moment we just define the function to get the temperture of Rouen 
    But we can add some functionality or change the city as we want
    check this site to see the available city https://openweathermap.org/city
'''
class weather :
    def __init__(self,key = "1a607532e6e0383699a35ffd455d7ddc"):
        self.key = key
        self.url1=" http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
        self.url2="http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}"
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/63.0.3239.132 Safari/537.36'}
    def requestTemperture(self):
        final_url = self.url1.format(city="Rouen, fr",key=self.key)
        r=requests.get(final_url,headers=self.header)
        sdw=r.content.decode('utf-8')
        lks=json.loads(sdw)
        K = lks['main'] ['temp']
        T = K - 273.15  # Kelvin to Celsius(°C)
        print(T)
        return T

    def requestToTemperture(self):
        final_url = self.url2.format(city="Rouen, fr",key=self.key)
        r=requests.get(final_url,headers=self.header)
        sdw=r.content.decode('utf-8')
        lks=json.loads(sdw)
        '''K = lks['main'] ['temp']
        T = K - 273.15  # Kelvin to Celsius(°C)
        return T
        '''
        K = lks['list'][0]['main']['temp']
        T = K - 273.15  # Kelvin to Celsius(°C)
        return T


if __name__ == '__main__':

    w = weather()   # Initialize the objet
    T = w.requestToTemperture()   # Ask for the temperture
    print(str(int(T)))