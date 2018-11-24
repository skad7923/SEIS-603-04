# Forecast module
import requests, pprint
import day, fiveDays, interface, weather
from tkinter import *

window = Tk()

inputData = interface.WeatherAppDisplay(window)

#weatherRequested = inputData.getWeatherRequested()
#zipcode = inputData.getZipcode()
#unit = inputData.getUnitRequested()
#
#futureWeather = inputData.getFutureWeather()



window.mainloop()


