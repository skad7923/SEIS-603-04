from tkinter import *
import requests
import day, fiveDays, weather

class WeatherAppDisplay():
    """"
    """

    def __init__(self, master):

        self.window = master
        self.window.title("Weather Game")

        self.zipcode = 0
        self.weatherRequested = "todayWeather"
        self.unitRequested = "metric"

        self.topFrame = Frame(self.window, width=500, height=500)
        self.topFrame.pack(side=TOP)
        self.middleFrame = Frame(self.window)
        self.middleFrame.pack()
        self.bottomFrame = Frame(self.window)
        self.bottomFrame.pack(side=BOTTOM)

        self.title = Label(self.topFrame, text="What's the weather, Lucas?")
        self.title.pack()

        self.zipcodeLabel = Label(self.middleFrame, text='Zipcode')
        self.zipcodeEntry = Entry(self.middleFrame)
        self.zipcodeLabel.grid(row=0, column=1)
        self.zipcodeEntry.grid(row=0, column=2)

        self.weatherEntered = StringVar()
        self.unitEntered = StringVar()
        self.todayButton = Radiobutton(self.middleFrame, text='Today', justify=RIGHT, tristatevalue=0, variable=self.weatherEntered, value="todayWeather")
        self.todayButton.grid(row=1, column=1)

        self.tomorrowButton = Radiobutton(self.middleFrame, text='Tomorrow', justify=LEFT, tristatevalue=0, variable=self.weatherEntered, value="tomorrowWeather")
        self.tomorrowButton.grid(row=2, column=1)

        self.fiveDaysButton = Radiobutton(self.middleFrame, text='5 Days', justify=LEFT, tristatevalue=0, variable=self.weatherEntered, value="5daysWeather")
        self.fiveDaysButton.grid(row=3, column=1)

        self.celsiusButton = Radiobutton(self.middleFrame, text='Celsius', justify=LEFT, tristatevalue=0, variable=self.unitEntered, value="metric")
        self.celsiusButton.grid(row=1, column=4)

        self.fahrenheitButton = Radiobutton(self.middleFrame, text='Fahrenheit', justify=LEFT, tristatevalue=0, variable=self.unitEntered, value="imperial")
        self.fahrenheitButton.grid(row=2, column=4)

        self.submitButton = Button(self.bottomFrame, text='Submit', command=self.getInput)
        self.submitButton.pack()

    def getWeatherRequested(self):
        return self.weatherRequested

    def getUnitRequested(self):
        return self.unitRequested

    def getZipcode(self):
        return self.zipcode

    def getFutureWeather(self):
        return self.futureWeather

    def getInput(self):

        self.zipcode = self.zipcodeEntry.get()
        self.weatherRequested =self.weatherEntered.get()
        self.unitRequested = self.unitEntered.get()

        self.futureWeather = weather.WeatherForecast(self.zipcode, self.weatherRequested, self.unitRequested)
        self.window.withdraw()
        self.results = ShowWeather(self, self.futureWeather, self.zipcode, self.weatherRequested, self.unitRequested)

    def show(self):
        """"""
        self.window.update()
        self.window.deiconify()

class ShowWeather(Toplevel):

    def __init__(self, master, pFutureWeather, pZipcode, pWeatherRequested, pUnitRequested):

        self.window = master
        self.futureWeather = pFutureWeather
        self.zipcode = pZipcode
        self.unitRequested = pUnitRequested
        self.weatherRequested = pWeatherRequested

        Toplevel.__init__(self)
        self.title("Weather")

        self.topFrame = Frame(self, width=500, height=500)
        self.topFrame.pack(side=TOP)
        self.middleFrame = Frame(self, width=500, height=500)
        self.middleFrame.pack()
        self.bottomFrame = Frame(self)
        self.bottomFrame.pack(side=BOTTOM)

        self.titleText = "Weather Forecast for Zipcode "+self.zipcode
        self.titleLabel = Label(self.topFrame, text=self.titleText)
        self.titleLabel.grid(row=0, column=3)

    #---- Field Names----#
        self.dateLabel = Label(self.middleFrame, text="Date")
        self.dateLabel.grid(row=2, column=1)

        self.weatherDescrLabel = Label(self.middleFrame, text="Description")
        self.weatherDescrLabel.grid(row=2, column=3)

        self.minTempDescrLabel = Label(self.middleFrame, text="Min Temp")
        self.minTempDescrLabel.grid(row=2, column=4)

        self.maxTempDescrLabel = Label(self.middleFrame, text="Max Temp")
        self.maxTempDescrLabel.grid(row=2, column=5)
    #------------#
        #---------Today's weather data---------#
        if self.weatherRequested == "todayWeather":
            self.dateLabel = Label(self.middleFrame, text=self.futureWeather.getTodayDate())
            self.dateLabel.grid(row=3, column=1)

            self.minTempDescrLabel = Label(self.middleFrame, text="Cur Temp")
            self.minTempDescrLabel.grid(row=2, column=2)

            self.minTempDescrLabel = Label(self.middleFrame, text=self.futureWeather.getCurTemp(0))
            self.minTempDescrLabel.grid(row=3, column=2)

            self.weatherDescrLabel = Label(self.middleFrame, text=self.futureWeather.getDescription(0))
            self.weatherDescrLabel.grid(row=3, column=3)

            self.minTempDescrLabel = Label(self.middleFrame, text=self.futureWeather.getMinTemp(0))
            self.minTempDescrLabel.grid(row=3, column=4)

            self.maxTempDescrLabel = Label(self.middleFrame, text=self.futureWeather.getMaxTemp(0))
            self.maxTempDescrLabel.grid(row=3, column=5)

            print()

        elif self.weatherRequested == "5daysWeather":
            aDay = 0
            localRow= 3
            while aDay < self.futureWeather.getTotalOfDays():
                self.dateLabel = Label(self.middleFrame, text=self.futureWeather.getTodayDate())
                self.dateLabel.grid(row=localRow, column=1)

                self.weatherDescrLabel = Label(self.middleFrame, text=self.futureWeather.getDescription(aDay))
                self.weatherDescrLabel.grid(row=localRow, column=3)

                self.minTempDescrLabel = Label(self.middleFrame, text=self.futureWeather.getMinTemp(aDay))
                self.minTempDescrLabel.grid(row=localRow, column=4)

                self.maxTempDescrLabel = Label(self.middleFrame, text=self.futureWeather.getMaxTemp(aDay))
                self.maxTempDescrLabel.grid(row=localRow, column=5)

                self.maxTempDescrLabel = Label(self.middleFrame, text="Snow")
                self.maxTempDescrLabel.grid(row=localRow, column=6)

                self.maxTempDescrLabel = Label(self.middleFrame, text=self.futureWeather.getSnow(aDay))
                self.maxTempDescrLabel.grid(row=localRow, column=6)

                aDay = aDay + 1
                localRow = localRow+1

        else:
           print("interface - not yet")
        #-------------------#

        self.closeButton = Button(self.bottomFrame, text="Close", command=self.onClose)
        self.closeButton.grid(row=1, column=3)

        self.tryAgainButton = Button(self.bottomFrame, text="Try again", command=self.tryAgain)
        self.tryAgainButton.grid(row=1, column=2)

    def onClose(self):
        """"""
        self.destroy()
        exit()


    def tryAgain(self):
        """"""
        self.destroy()
        self.window.show()
