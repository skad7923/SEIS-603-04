# Forecast module
import requests, pprint
from datetime import date
import day
import constant as c

def getTheGreater(num1, num2):
    """
    Returns the greater number between num1 and num2
    """
    if num1 > num2:
        return num1
    else:
        return num2


def getTheLess(num1, num2):
    """
    Returns the smaller number between num1 and num2
    """
    if num1 < num2:
        return num1
    else:
        return num2

class WeatherForecast:
    """
     Class responsible for calling the weather API, for receiving the data back and creating a data structure to store it.
    Attributes:
        zipcode: zipcode received as a parameter
        weatherRequested: type of forecast received as a parameter - today's, tomorrow or 5 days
        unit: metric (Celsius) or imperial (Fahrenheit) received as a parameter

        weatherData: list of objects 'Day' with the weather data stored
        rawData: data received from the Open Weather Map API
        totalOfDays: number of days in the weatherData
    """

    def __init__(self, pZipcode, pWeatherRequested, pUnit):

        self.zipcode = pZipcode
        self.weatherRequested = pWeatherRequested
        self.unit = pUnit

        self.totalOfDays = 0

        self.communicateWeatherAPI()

        self.weatherData = []
        self.readWeatherRawData()

    def communicateWeatherAPI(self):
        """
        Method that communicates with the Open Weather API and receives the data back.
        """
        # Defining the url to call based on the type of forecast chosen
        if self.weatherRequested == c.TODAY_WEATHER:
            url = c.API_TODAY_WEATHER.format(self.zipcode, self.unit)
        else:
            url = c.API_FIVE_DAYS_WEATHER.format(self.zipcode, self.unit)

        try:
            # API call
            res = requests.get(url)
            self.rawData = res.json()


        except:
            print("Communication with API not working")


    def readWeatherRawData(self):
        """
        Method responsible for reading the raw data received and creating 'Day' objects to sotre the weather information.
        """
        try:
            # Read today's weather
            if self.weatherRequested == c.TODAY_WEATHER:
                self.totalOfDays = 1
                self.weatherData.append(day.Day(curr=self.rawData['main']['temp'], min=self.rawData['main']['temp_min'], max=self.rawData['main']['temp_max'], description=self.rawData['weather'][0]['description'], snow=0, rain=0, date=str(date.today())))

            # Read 5 days forecast
            else:
                self.readFiveDaysRawData()
        except:
            print("Problem reading the data received by the API.")

    def readFiveDaysRawData(self):
        """
        The 5-days weather forecast data contains information about the weather for every 3h, so in order to know the
        minimum and maximum temperatures and total of snow expected it needs to do some comparisons/calculations
        """

        countList = 0
        countDays = 0

        min = 1000
        max = -1000
        snow = 0
        rain = 0

        self.totalOfDays = 0

        while countList < self.rawData['cnt']:
            # Find the min and max temperatures for the same day and adds the amount of snow
            min = getTheLess(self.rawData['list'][countList]['main']['temp_min'], min)
            max = getTheGreater(self.rawData['list'][countList]['main']['temp_max'], max)
            if 'snow' in self.rawData['list'][countList]:
                value = list(self.rawData['list'][countList]['snow'].values())
                if value:
                    snow = snow + value[0]
            if 'rain' in self.rawData['list'][countList]:
                value = list(self.rawData['list'][countList]['rain'].values())
                if value:
                    rain = rain + value[0]

            # If it is the last entry on data OR the next entry refers to a different day, then creates a new 'Day' and stores the data
            if (countList == self.rawData['cnt'] - 1) or (self.rawData['list'][countList]['dt_txt'][0:10] != self.rawData['list'][countList + 1]['dt_txt'][0:10]):
                self.weatherData.append(day.Day(0, min, max, self.rawData['list'][countList]['weather'][0]['description'], snow, rain, self.rawData['list'][countList]['dt_txt'][0:10]))

                self.totalOfDays = countDays + 1
                min = 1000
                max = -1000
                snow = 0
                rain = 0
                countDays = countDays + 1
                self.totalOfDays = countDays

            countList = countList + 1

    def getCurTemp(self, dayRequested):
        day = dayRequested
        return self.weatherData[day].getCurTemp()

    def getMinTemp(self, dayRequested):
        day = dayRequested
        return self.weatherData[day].getMinTemp()

    def getMaxTemp(self, dayRequested):
        day = dayRequested
        return self.weatherData[day].getMaxTemp()

    def getDescription(self, dayRequested):
        day = dayRequested
        return self.weatherData[day].getDescription()

    def getSnow(self, dayRequested):
        day = dayRequested
        return self.weatherData[day].getSnow()

    def getRain(self, dayRequested):
        day = dayRequested
        return self.weatherData[day].getRain()

    def getTotalOfDays(self):
        return self.totalOfDays

    def getDate(self, dayRequested):
        day = dayRequested
        return self.weatherData[day].getDay()