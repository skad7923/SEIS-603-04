import constant as c

class WeatherMeme:
    """
    unitRequested
    futureWeather
    rainInForecast: true if there is > 1mm of rain in the forecast
    snowInForecast: true if there is > 1mm of snow in the forecast
    tempLevel: ranges from 1-5, 1 being very cold and 5 being very hot
    """
    def __init__(self):#, pFutureWeather, pUnitRequested):
        self.memeName = c.MEME_TEMP3
        self.snowInForecast = False
        self.rainInForecast = False
        self.tempLevel = 3

    def findMeme(self, pFutureWeather, pUnitRequested):
        self.futureWeather = pFutureWeather
        self.unitRequested = pUnitRequested

        aday=0

        while aday < self.futureWeather.getTotalOfDays():
            #Cheack snow and rain

            if self.futureWeather.getSnow(aday) > 10:
                self.snowInForecast = True
            if self.futureWeather.getRain(aday) > 5:
                self.rainInForecast = True

            # Check temperatures for each day
            if (self.unitRequested == c.CELSIUS and self.futureWeather.getMinTemp(aday) < c.TEMP_LOW_C_1) or (
                    self.unitRequested == c.FAHRENHEIT and self.futureWeather.getMinTemp(aday) < c.TEMP_LOW_F_1):
                self.tempLevel = 1
            elif (self.unitRequested == c.CELSIUS and self.futureWeather.getMinTemp(aday) < c.TEMP_LOW_C_2) or (
                    self.unitRequested == c.FAHRENHEIT and self.futureWeather.getMinTemp(aday) < c.TEMP_LOW_F_2):
                self.tempLevel = 2
            elif (self.unitRequested == c.CELSIUS and self.futureWeather.getMaxTemp(aday) < c.TEMP_LOW_C_3) or (
                    self.unitRequested == c.FAHRENHEIT and self.futureWeather.getMaxTemp(aday) < c.TEMP_LOW_F_3):
                self.tempLevel = 3
            elif (self.unitRequested == c.CELSIUS and self.futureWeather.getMaxTemp(aday) < c.TEMP_LOW_C_4) or (
                    self.unitRequested == c.FAHRENHEIT and self.futureWeather.getMaxTemp(aday) < c.TEMP_LOW_F_4):
                self.tempLevel = 4
            else:
                self.tempLevel = 5
            aday = aday + 1

        if self.snowInForecast:
            self.memeName = c.MEME_SNOW
        elif self.rainInForecast:
            self.memeName = c.MEME_RAIN
        elif self.tempLevel == 1:
            self.memeName = c.MEME_TEMP1
        elif self.tempLevel == 2:
            self.memeName = c.MEME_TEMP2
        elif self.tempLevel == 3:
            self.memeName = c.MEME_TEMP3
        elif self.tempLevel == 4:
            self.memeName = c.MEME_TEMP4
        else:
            self.memeName = c.MEME_TEMP5

        return self.memeName