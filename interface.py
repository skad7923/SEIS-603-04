from tkinter import *
from datetime import date
import zipcodes
from PIL import Image, ImageTk

import weather, weatherMeme
import constant as c

class WeatherAppDisplay():
    """"
    Class responsible for first interface - gathering user's input and generating weather forecast reports
                                                                        (with the help of the Weather Class)
    Attributes:
        zipcode: zipcode informed by the user
        weatherRequested: type of forecast the user wants to know - today's, tomorrow or 5 days
        unitRequested: metric (Celsius) or imperial (Fahrenheit) informed by the user
        futureWeather: data type responsible for storing the weather data - it is a list of objects of type 'Day'

        zipcodeEntered: temporary variable until user clicks Submit
        weatherEntered: temporary variable until user clicks Submit
        unitEntered: temporary variable until user clicks Submit

        The other attributes belongs to what is shown on the screen, labels and fields
    """

    def __init__(self, master):
        """"
        Creates the first screen, where the user enters his input for asking for the forecast. When the user clicks 'Submit',
        the method getInput is called.
        """

        self.window = master
        self.window.title("Weather")

        self.zipcode = 0
        self.weatherRequested = c.FIVE_DAYS_WEATHER
        self.unitRequested = c.CELSIUS

        self.topFrame = Frame(self.window, width=500, height=500)
        self.topFrame.pack(side=TOP)
        self.middleFrame = Frame(self.window)
        self.middleFrame.pack()
        self.bottomFrame = Frame(self.window)
        self.bottomFrame.pack(side=BOTTOM)

        self.title = Label(self.topFrame, text="What's the weather?")
        self.title.pack()

        self.zipcodeLabel = Label(self.middleFrame, text='Zipcode' )
        self.zipcodeEntered = Entry(self.middleFrame)
        self.zipcodeLabel.grid(row=0, column=1)
        self.zipcodeEntered.grid(row=0, column=2)

        self.weatherEntered = StringVar()
        self.unitEntered = StringVar()
        self.todayButton = Radiobutton(self.middleFrame, state='active',text='Today', justify=RIGHT, variable=self.weatherEntered, value=c.TODAY_WEATHER)
        self.todayButton.grid(row=1, column=1)

        self.tomorrowButton = Radiobutton(self.middleFrame, text='Tomorrow', justify=LEFT, tristatevalue=0, variable=self.weatherEntered, value=c.TOMORROW_WEATHER)
        self.tomorrowButton.grid(row=2, column=1)

        self.fiveDaysButton = Radiobutton(self.middleFrame, text='5 Days', justify=LEFT, tristatevalue=0, variable=self.weatherEntered, value=c.FIVE_DAYS_WEATHER)
        self.fiveDaysButton.grid(row=3, column=1)

        self.celsiusButton = Radiobutton(self.middleFrame, state='active', text='Celsius', justify=LEFT, variable=self.unitEntered, value=c.CELSIUS)
        self.celsiusButton.grid(row=1, column=4)

        self.fahrenheitButton = Radiobutton(self.middleFrame, text='Fahrenheit', justify=LEFT, tristatevalue=0, variable=self.unitEntered, value=c.FAHRENHEIT)
        self.fahrenheitButton.grid(row=2, column=4)

        # Default values
        self.unitEntered.set(c.CELSIUS)
        self.weatherEntered.set(c.TODAY_WEATHER)

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
        """
        This method is called after the user clicks on 'Submit'. It gathers all the user's input and calls other methods
        get the weather forecast.
        """

        #Getting user's input
        self.zipcode = self.zipcodeEntered.get()
        self.weatherRequested =self.weatherEntered.get()
        self.unitRequested = self.unitEntered.get()

        # Test if a valid zipcode was provided
        if self.zipcode != '' and self.zipcode.isdigit() and zipcodes.is_valid(self.zipcode):
            # Call method to create an object with the the forecast received from the API
            self.futureWeather = weather.WeatherForecast(self.zipcode, self.weatherRequested, self.unitRequested)
            # Clears the input window
            self.window.withdraw()
            # Call method for showing the forecast
            self.results = ShowWeather(self, self.futureWeather, self.zipcode, self.weatherRequested, self.unitRequested)
        else:
            print("Provide a valid zipcode.")

    def show(self):
        """"""
        self.window.update()
        self.window.deiconify()

class ShowWeather(Toplevel):
    """
       Class responsible for the interface that shows the forecast - it receives as parameters all the input necessary
    Attributes:
        zipcode: zipcode informed by the user
        weatherRequested: type of forecast the user wants to know - today's, tomorrow or 5 days
        unitRequested: metric (Celsius) or imperial (Fahrenheit) informed by the user
        futureWeather: data type responsible for storing the weather data - it is a list of objects of type 'Day'

        The other attributes belongs to what is shown on the screen, labels and fields
    """

    def __init__(self, master, pFutureWeather, pZipcode, pWeatherRequested, pUnitRequested):

        self.window = master
        self.zipcode = pZipcode
        self.weatherRequested = pWeatherRequested
        self.unitRequested = pUnitRequested
        self.futureWeather = pFutureWeather

        if self.unitRequested == 'metric':
            self.unitDisplay = '(C)'
        else:
            self.unitDisplay = '(F)'

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

        self.weatherDescrLabel = Label(self.middleFrame, text="   Description   ")
        self.weatherDescrLabel.grid(row=2, column=2)

        self.minTempDescrLabel = Label(self.middleFrame, text=" Min Temp " +self.unitDisplay)
        self.minTempDescrLabel.grid(row=2, column=4)

        self.maxTempDescrLabel = Label(self.middleFrame, text=" Max Temp "+self.unitDisplay)
        self.maxTempDescrLabel.grid(row=2, column=5)

        #---------Today's weather data---------#
        if self.weatherRequested == c.TODAY_WEATHER:
            self.dateLabel = Label(self.middleFrame, text=self.futureWeather.getDate(0))
            self.dateLabel.grid(row=3, column=1)

            self.weatherDescrLabel = Label(self.middleFrame, text=self.futureWeather.getDescription(0))
            self.weatherDescrLabel.grid(row=3, column=2)

            self.minTempDescrLabel = Label(self.middleFrame, text=" Cur Temp " + self.unitDisplay)
            self.minTempDescrLabel.grid(row=2, column=3)

            self.minTempDescrLabel = Label(self.middleFrame, text=self.futureWeather.getCurTemp(0))
            self.minTempDescrLabel.grid(row=3, column=3)

            self.minTempDescrLabel = Label(self.middleFrame, text=self.futureWeather.getMinTemp(0))
            self.minTempDescrLabel.grid(row=3, column=4)

            self.maxTempDescrLabel = Label(self.middleFrame, text=self.futureWeather.getMaxTemp(0))
            self.maxTempDescrLabel.grid(row=3, column=5)

        # ---------5 days weather data---------#
        elif self.weatherRequested == c.FIVE_DAYS_WEATHER:
            aDay = 0
            localRow= 3
            self.snowLabel = Label(self.middleFrame, text="Snow (mm)")
            self.snowLabel.grid(row=2, column=6)
            self.rainLabel = Label(self.middleFrame, text="Rain (mm)")
            self.rainLabel.grid(row=2, column=7)

            # Reads everyday in the list of Days
            while aDay < self.futureWeather.getTotalOfDays():
                self.dateLabel = Label(self.middleFrame, text=self.futureWeather.getDate(aDay))
                self.dateLabel.grid(row=localRow, column=1)

                self.weatherDescrLabel = Label(self.middleFrame, text=self.futureWeather.getDescription(aDay))
                self.weatherDescrLabel.grid(row=localRow, column=2)

                self.minTempDescrLabel = Label(self.middleFrame, text=self.futureWeather.getMinTemp(aDay))
                self.minTempDescrLabel.grid(row=localRow, column=4)

                self.maxTempDescrLabel = Label(self.middleFrame, text=self.futureWeather.getMaxTemp(aDay))
                self.maxTempDescrLabel.grid(row=localRow, column=5)

                self.snowLabel = Label(self.middleFrame, text=self.futureWeather.getSnow(aDay))
                self.snowLabel.grid(row=localRow, column=6)

                self.rainLabel = Label(self.middleFrame, text=self.futureWeather.getRain(aDay))
                self.rainLabel.grid(row=localRow, column=7)

                aDay = aDay + 1
                localRow = localRow+1

        else:
            self.snowLabel = Label(self.middleFrame, text="Snow (mm)")
            self.snowLabel.grid(row=2, column=6)
            self.rainLabel = Label(self.middleFrame, text="Rain (mm)")
            self.rainLabel.grid(row=2, column=7)

            if self.futureWeather.getDate(0) == str(date.today()):
                tomorrowDay = 1
            else:
                tomorrowDay = 0
            self.dateLabel = Label(self.middleFrame, text=self.futureWeather.getDate(tomorrowDay))
            self.dateLabel.grid(row=3, column=1)

            self.weatherDescrLabel = Label(self.middleFrame, text=self.futureWeather.getDescription(tomorrowDay))
            self.weatherDescrLabel.grid(row=3, column=3)

            self.minTempDescrLabel = Label(self.middleFrame, text=self.futureWeather.getMinTemp(tomorrowDay))
            self.minTempDescrLabel.grid(row=3, column=4)

            self.maxTempDescrLabel = Label(self.middleFrame, text=self.futureWeather.getMaxTemp(tomorrowDay))
            self.maxTempDescrLabel.grid(row=3, column=5)

            self.snowLabel = Label(self.middleFrame, text=self.futureWeather.getSnow(tomorrowDay))
            self.snowLabel.grid(row=3, column=6)

            self.rainLabel = Label(self.middleFrame, text=self.futureWeather.getRain(tomorrowDay))
            self.rainLabel.grid(row=3, column=7)

        # Select and show weather meme
        self.image = weatherMeme.WeatherMeme()
        self.imageName = self.image.findMeme(self.futureWeather, self.unitRequested)
        try:
            self.loadImage = Image.open(self.imageName)
            self.renderImage = ImageTk.PhotoImage(self.loadImage)
            self.img = Label(self.middleFrame, image=self.renderImage)
            self.img.image = self.renderImage
            self.img.grid(row=9, columnspan=8)
        except IOError:
            print("Image not found.")

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
