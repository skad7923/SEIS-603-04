from datetime import date


class Day:  # (object):
    """A day and its weather features.

    Attributes:
        date: date to represent mm-dd-yyyy.
        minTemp: float to represent the minimum temperature of the day.
        maxTemp: float to represent the maximum temperature of the day.
        curTemp: float to represent the current temperature.
        descripton: string to describe weather
        wind: float for wind speed
        snowTotal: float to describe the total of snow expected for the day.
    """

    def __init__(self, typeOfInput, data):
        """Return a Day object whose date is *mm-dd-yyyy* and other attributes is 0."""
        if typeOfInput == 'todayWeather':
            self.date = str(date.today())
            self.minTemp = data['main']['temp_min']
            self.maxTemp = data['main']['temp_max']
            self.curTemp = data['main']['temp']
            self.description = data['weather'][0]['description']
            self.wind = data['wind']['speed']
            self.snowTotal = 0

        else:
            self.date = date.today()
            self.minTemp = 0
            self.maxTemp = 0
            self.curTemp = 0
            self.description = 0
            self.wind = 0
            self.snowTotal = 0

    def getDay(self):
        return self.date

    def getMinTemp(self):
        return self.minTemp

    def getMaxTemp(self):
        return self.maxTemp

    def getTemp(self):
        return self.curTemp

    def getDescription(self):
        return self.description

    def getSnow(self):
        return self.snow

    def printWeather(self):
        print("Today ", self.getDay(), "\tWeather:", self.getDescription(),"\tMin temp:", self.getMinTemp(), "\tMax temp:", self.getMaxTemp())


    def setWeather(self, day, min, max, description, snow):
        self.date = day
        self.minTemp = min
        self.maxTemp = max
        self.description = description
        self.snow = snow
