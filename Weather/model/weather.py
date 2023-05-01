import requests

API_KEY = 'e1dfb90f76d04d13bdb12821230802'

class Weather:

    def __init__(self, Location:str='40324'):
        self.weatherData = {}
        self.fetch(Location)

        # ---- Location ----

    def getLocationData(self, name):
        data = self.weatherData['location'][name]
        return str(data)

    def getCity(self):
        return self.getLocationData('name')

    def getState(self):
        return self.getLocationData('region')

    def getCountry(self):
        return self.getLocationData('country')

    def getTimeZone(self):
        return self.getLocationData('tz_id')

    def getLocation(self):
        if 'America' in self.getTimeZone():
            return f'{self.getCity()}, {self.getState()}'
        else:
            return f'{self.getCity()}, {self.getCountry()}'

        # ---- Current

    def getCurrentData(self, name):
        data = self.weatherData['current'][name]
        return data if name == 'condition' else str(data)

    def getCurrentTempF(self):
        return self.getCurrentData('temp_f')+'\u00B0F'

    def getCurrentTempC(self):
        return self.getCurrentData('temp_c')+'\u00B0C'

    def getConditionText(self):
        condition = self.getCurrentData('condition')
        return str(condition['text'])

    def getConditionIcon(self):
        pass

    def getWindSpeedMPH(self):
        return self.getCurrentData('wind_mph')+' mph'

    def getWindDirection(self):
        return self.getCurrentData('wind_dir')

    def getFeelsLikeF(self):
        return self.getCurrentData('feelslike_f')+'\u00B0F'

    def getFeelsLikeC(self):
        return self.getCurrentData('feelslike_c')+'\u00B0C'

    #---- Fetch -----#
    def fetch(self, query):
        try:
            url= f'http://api.weatherapi.com/v1/current.json' + \
                f'?key={API_KEY}&q={query}&aqi=np'
            self.weatherData = requests.get(url).json()
        except:
            self.weatherData = {'error'}