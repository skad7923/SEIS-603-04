
class Day:
    """A day and its weather features.

    Attributes:
        date: date to represent mm-dd-yyyy.
        minTemp: float to represent the minimum temperature of the day.
        maxTemp: float to represent the maximum temperature of the day.
        curTemp: float to represent the current temperature.
        descripton: string to describe weather
        snow: float to represent the total of snow expected for the day.
        rain: float to represent the total of rain expected for the day.
    """

    def __init__(self, curr, min, max, description, snow, rain, date):
        """Creates a Day object with the information about the weather"""

        self.date = date
        self.curTemp = curr
        self.minTemp = min
        self.maxTemp = max
        self.description = description
        self.snow = snow
        self.rain = rain

    def getDay(self):
        return self.date

    def getMinTemp(self):
        return round(self.minTemp,1)

    def getMaxTemp(self):
        return round(self.maxTemp,1)

    def getCurTemp(self):
        return round(self.curTemp, 1)

    def getDescription(self):
        return self.description

    def getSnow(self):
        return round(self.snow,2)

    def getRain(self):
        return round(self.rain,2)