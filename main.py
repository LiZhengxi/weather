import requests
import json
class weather :

    def __init__(self,key = "1a607532e6e0383699a35ffd455d7ddc"):
        self.key = key
        self.url=" http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/63.0.3239.132 Safari/537.36'}
    def requestWeather(self):
        final_url = self.url.format(city="Lille, fr",key=self.key)
        r=requests.get(final_url,headers=self.header)
        sdw=r.content.decode('utf-8')
        lks=json.loads(sdw)
        K = lks['main'] ['temp']
        T = K - 273.15
        return T

if __name__ == '__main__':

    w = weather()
    T = w.requestWeather()
    print (str(T)+"°c")