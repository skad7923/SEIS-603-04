
class Day:
    """A day and its weather features.

    Attributes:
        date: date to represent mm-dd-yyyy.
        minTemp: float to represent the minimum temperature of the day.
        maxTemp: float to represent the maximum temperature of the day.
        curTemp: float to represent the current temperature.
        descripton: string to describe weather
        snowTotal: float to describe the total of snow expected for the day.
    """

    def __init__(self, curr, min, max, description, snow, date):
        """Creates a Day object with the information about the weather"""

        self.date = date
        self.curTemp = curr
        self.minTemp = min
        self.maxTemp = max
        self.description = description
        self.snow = snow

    def getDay(self):
        return self.date

    def getMinTemp(self):
        return self.minTemp

    def getMaxTemp(self):
        return self.maxTemp

    def getCurTemp(self):
        return self.curTemp

    def getDescription(self):
        return self.description

    def getSnow(self):
        return self.snow