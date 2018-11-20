from tkinter import *
import requests
import day, fiveDays, weather

class firstWindow():
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

        self.fahreinheitButton = Radiobutton(self.middleFrame, text='Fahreinheit', justify=LEFT, tristatevalue=0, variable=self.unitEntered, value="imperial")
        self.fahreinheitButton.grid(row=2, column=4)

        self.buttonSubmit = Button(self.bottomFrame, text='Submit', command=self.showWeather)
        self.buttonSubmit.pack()

    def getWeatherRequested(self):
        return self.weatherRequested

    def getUnitRequested(self):
        return self.unitRequested

    def getZipcode(self):
        return self.zipcode

    def showWeather(self):
        self.zipcode = self.zipcodeEntry.get()
        self.weatherRequested =self.weatherEntered.get()
        self.unitRequested = self.unitEntered.get()

        results = weather.getWeather(self.zipcode, self.weatherRequested, self.unitRequested)

        if self.weatherRequested == "todayWeather":
            results.printWeather()
        else:
            results.printForecast()
