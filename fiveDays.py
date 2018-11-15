import day


def getTheGreater(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def getTheLess(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2


class FiveDay:#(object):
    """A group of 5 days and its weather features.

    Attributes:
        listOfDays: a list to store objects of the type Day.
        totalOfDays: number of days in the forecast as it varies for each API call
   """

    def __init__(self, data):
        """Return a FiveDays object that has a group of five Day objects.
        """
        countList = 0
        countDays = 0

        min = 1000
        max = -1000
        snow = 0

        self.listOfDays = []
        self.totalOfDays = 0

        while countList < data['cnt']:
            # Find the min and max temperatures for the same day and adds the snow
            min = getTheLess(data['list'][countList]['main']['temp_min'], min)
            max = getTheGreater(data['list'][countList]['main']['temp_max'], max)
            if 'snow' in data['list'][countList]:
                value = list(data['list'][countList]['snow'].values())
                if value:
                    snow = snow + value[0]

            # If it is the last entry on data OR the next entry refers to a different day, then creates a new day and stores the data
            if (countList == data['cnt'] - 1) or (data['list'][countList]['dt_txt'][0:10] != data['list'][countList+1]['dt_txt'][0:10]):
                self.listOfDays.append(day.Day('fiveDays', 'need to fix this'))
                self.listOfDays[countDays].setWeather(data['list'][countList]['dt_txt'][0:10], min, max, data['list'][countList]['weather'][0]['description'],snow )
                self.totalOfDays = countDays +1
                min = 1000
                max = -1000
                snow = 0
                #print(self.listOfDays[])
                countDays = countDays + 1
            countList = countList + 1


    def getTotalOfDays(self):
        return self.totalOfDays

    def getMinTemperatureForDay(self, whatDay):
        """ returns the minimum temperature for the day informed
        """
        return self.listOfDays[whatDay-1].getMinTemp()

    def getMaxTemperatureForDay(self, whatDay):
        """ returns the maximum temperature for the day informed
        """
        return self.listOfDays[whatDay-1].getMaxTemp()

    def getDescriptionForDay(self, whatDay):
        """ returns the weather description for the day informed
        """
        return self.listOfDays[whatDay-1].getDescription()

    def getSnowForDay(self, whatDay):
        """ returns the weather description for the day informed
        """
        return self.listOfDays[whatDay-1].getSnow()

    def getDateForDay(self, whatDay):
        """ returns the weather description for the day informed
        """
        return self.listOfDays[whatDay-1].getDay()

    def printForecast(self):
        """ print all the data for the 5 days forecast

        """
        print('   Date      ', '  Weather   ', '\tMin Temp', '\t\tMax Temp', '  \t\tSnow')
        for eachDay in range(1,self.totalOfDays+1):
            print(self.getDateForDay(eachDay),'\t', self.getDescriptionForDay(eachDay), '\t\t', self.getMinTemperatureForDay(eachDay),'\t\t', self.getMaxTemperatureForDay(eachDay), '\t\t',self.getSnowForDay(eachDay))

