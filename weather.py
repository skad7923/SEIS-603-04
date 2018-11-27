# Forecast module
import requests
from datetime import date
import day

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
        if self.weatherRequested == "todayWeather":
            url = 'http://api.openweathermap.org/data/2.5/weather?zip={}&appid=20376eb779c0af83f41165d793e494c0&units={}'.format(self.zipcode, self.unit)
            # Data for test purpose
            #self.rawData = {'coord': {'lon': -93.16, 'lat': 45.01}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}],'base': 'stations','main': {'temp': 259.21, 'pressure': 1033, 'humidity': 78, 'temp_min': 258.05, 'temp_max': 260.45},'visibility': 16093, 'wind': {'speed': 2.59, 'deg': 291.501}, 'clouds': {'all': 1},'dt': 1542114900,'sys': {'type': 1, 'id': 1570, 'message': 0.0049, 'country': 'US', 'sunrise': 1542114507,'sunset': 1542149103}, 'id': 420019793, 'name': 'Saint Paul', 'cod': 200}
        else:
            url = 'http://api.openweathermap.org/data/2.5/forecast?zip={}&appid=20376eb779c0af83f41165d793e494c0&units={}'.format(self.zipcode, self.unit)
            # Example of the data received above (a dictionary) for forecast - for test purpose
            #self.rawData={'cod': '200', 'message': 0.0075, 'cnt': 38, 'list': [{'dt': 1542088800, 'main': {'temp': 260.95, 'temp_min': 259.57, 'temp_max': 260.95, 'pressure': 1011.83, 'sea_level': 1049.14, 'grnd_level': 1011.83, 'humidity': 83, 'temp_kf': 1.38}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.76, 'deg': 305.001}, 'snow': {'3h': 0.0025}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-13 06:00:00'}, {'dt': 1542099600, 'main': {'temp': 258.11, 'temp_min': 257.076, 'temp_max': 258.11, 'pressure': 1011.69, 'sea_level': 1049.3, 'grnd_level': 1011.69, 'humidity': 83, 'temp_kf': 1.03}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.09, 'deg': 294.001}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-13 09:00:00'}, {'dt': 1542110400, 'main': {'temp': 255.52, 'temp_min': 254.829, 'temp_max': 255.52, 'pressure': 1011.33, 'sea_level': 1049.09, 'grnd_level': 1011.33, 'humidity': 90, 'temp_kf': 0.69}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.19, 'deg': 263.001}, 'snow': {'3h': 0.00375}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-13 12:00:00'}, {'dt': 1542121200, 'main': {'temp': 258.93, 'temp_min': 258.583, 'temp_max': 258.93, 'pressure': 1011.56, 'sea_level': 1048.95, 'grnd_level': 1011.56, 'humidity': 90, 'temp_kf': 0.34}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.04, 'deg': 263.007}, 'snow': {'3h': 0.005}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-13 15:00:00'}, {'dt': 1542132000, 'main': {'temp': 265.042, 'temp_min': 265.042, 'temp_max': 265.042, 'pressure': 1010.99, 'sea_level': 1047.66, 'grnd_level': 1010.99, 'humidity': 78, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.08, 'deg': 271.001}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-13 18:00:00'}, {'dt': 1542142800, 'main': {'temp': 267.69, 'temp_min': 267.69, 'temp_max': 267.69, 'pressure': 1009.17, 'sea_level': 1045.51, 'grnd_level': 1009.17, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.68, 'deg': 272.001}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-13 21:00:00'}, {'dt': 1542153600, 'main': {'temp': 263.149, 'temp_min': 263.149, 'temp_max': 263.149, 'pressure': 1009.47, 'sea_level': 1046.36, 'grnd_level': 1009.47, 'humidity': 85, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.86, 'deg': 253.001}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-14 00:00:00'}, {'dt': 1542164400, 'main': {'temp': 259.311, 'temp_min': 259.311, 'temp_max': 259.311, 'pressure': 1010.07, 'sea_level': 1047.32, 'grnd_level': 1010.07, 'humidity': 77, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.41, 'deg': 245.001}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-14 03:00:00'}, {'dt': 1542175200, 'main': {'temp': 257.277, 'temp_min': 257.277, 'temp_max': 257.277, 'pressure': 1010.15, 'sea_level': 1047.64, 'grnd_level': 1010.15, 'humidity': 73, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.22, 'deg': 242.003}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-14 06:00:00'}, {'dt': 1542186000, 'main': {'temp': 256.523, 'temp_min': 256.523, 'temp_max': 256.523, 'pressure': 1010.13, 'sea_level': 1047.69, 'grnd_level': 1010.13, 'humidity': 68, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.21, 'deg': 148.004}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-14 09:00:00'}, {'dt': 1542196800, 'main': {'temp': 256.915, 'temp_min': 256.915, 'temp_max': 256.915, 'pressure': 1009.82, 'sea_level': 1047.39, 'grnd_level': 1009.82, 'humidity': 66, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.34, 'deg': 132.504}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-14 12:00:00'}, {'dt': 1542207600, 'main': {'temp': 264.738, 'temp_min': 264.738, 'temp_max': 264.738, 'pressure': 1010.16, 'sea_level': 1046.91, 'grnd_level': 1010.16, 'humidity': 85, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.76, 'deg': 166}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-14 15:00:00'}, {'dt': 1542218400, 'main': {'temp': 271.74, 'temp_min': 271.74, 'temp_max': 271.74, 'pressure': 1008.06, 'sea_level': 1043.91, 'grnd_level': 1008.06, 'humidity': 79, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.76, 'deg': 174.007}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-14 18:00:00'}, {'dt': 1542229200, 'main': {'temp': 274.201, 'temp_min': 274.201, 'temp_max': 274.201, 'pressure': 1004.81, 'sea_level': 1040.27, 'grnd_level': 1004.81, 'humidity': 76, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.76, 'deg': 185.505}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-14 21:00:00'}, {'dt': 1542240000, 'main': {'temp': 272.042, 'temp_min': 272.042, 'temp_max': 272.042, 'pressure': 1002.41, 'sea_level': 1038.21, 'grnd_level': 1002.41, 'humidity': 80, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 6.81, 'deg': 188.504}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-15 00:00:00'}, {'dt': 1542250800, 'main': {'temp': 271.768, 'temp_min': 271.768, 'temp_max': 271.768, 'pressure': 1000.85, 'sea_level': 1036.67, 'grnd_level': 1000.85, 'humidity': 78, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 7.06, 'deg': 198.505}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-15 03:00:00'}, {'dt': 1542261600, 'main': {'temp': 271.126, 'temp_min': 271.126, 'temp_max': 271.126, 'pressure': 999.61, 'sea_level': 1035.43, 'grnd_level': 999.61, 'humidity': 76, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 6.66, 'deg': 208.001}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-15 06:00:00'}, {'dt': 1542272400, 'main': {'temp': 270.322, 'temp_min': 270.322, 'temp_max': 270.322, 'pressure': 997.61, 'sea_level': 1033.52, 'grnd_level': 997.61, 'humidity': 80, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.81, 'deg': 207.507}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-15 09:00:00'}, {'dt': 1542283200, 'main': {'temp': 269.248, 'temp_min': 269.248, 'temp_max': 269.248, 'pressure': 995.7, 'sea_level': 1031.67, 'grnd_level': 995.7, 'humidity': 87, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.06, 'deg': 205.004}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-15 12:00:00'}, {'dt': 1542294000, 'main': {'temp': 270.672, 'temp_min': 270.672, 'temp_max': 270.672, 'pressure': 994.47, 'sea_level': 1030, 'grnd_level': 994.47, 'humidity': 81, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.21, 'deg': 202.001}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-15 15:00:00'}, {'dt': 1542304800, 'main': {'temp': 275.669, 'temp_min': 275.669, 'temp_max': 275.669, 'pressure': 991.89, 'sea_level': 1026.84, 'grnd_level': 991.89, 'humidity': 78, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 48}, 'wind': {'speed': 4.21, 'deg': 205.504}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-15 18:00:00'}, {'dt': 1542315600, 'main': {'temp': 277.006, 'temp_min': 277.006, 'temp_max': 277.006, 'pressure': 989.74, 'sea_level': 1024.48, 'grnd_level': 989.74, 'humidity': 77, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 36}, 'wind': {'speed': 3.4, 'deg': 228.001}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-15 21:00:00'}, {'dt': 1542326400, 'main': {'temp': 272.872, 'temp_min': 272.872, 'temp_max': 272.872, 'pressure': 989.2, 'sea_level': 1024.25, 'grnd_level': 989.2, 'humidity': 90, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.43, 'deg': 265.007}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-16 00:00:00'}, {'dt': 1542337200, 'main': {'temp': 273.409, 'temp_min': 273.409, 'temp_max': 273.409, 'pressure': 988.82, 'sea_level': 1024.09, 'grnd_level': 988.82, 'humidity': 91, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 56}, 'wind': {'speed': 4.77, 'deg': 297.002}, 'rain': {'3h': 0.015}, 'snow': {'3h': 0.0125}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-16 03:00:00'}, {'dt': 1542348000, 'main': {'temp': 273.431, 'temp_min': 273.431, 'temp_max': 273.431, 'pressure': 988.54, 'sea_level': 1023.82, 'grnd_level': 988.54, 'humidity': 89, 'temp_kf': 0}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}], 'clouds': {'all': 68}, 'wind': {'speed': 6.06, 'deg': 306.004}, 'rain': {}, 'snow': {'3h': 0.095}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-16 06:00:00'}, {'dt': 1542358800, 'main': {'temp': 273.062, 'temp_min': 273.062, 'temp_max': 273.062, 'pressure': 988.5, 'sea_level': 1023.81, 'grnd_level': 988.5, 'humidity': 86, 'temp_kf': 0}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}], 'clouds': {'all': 80}, 'wind': {'speed': 7.01, 'deg': 309.501}, 'rain': {}, 'snow': {'3h': 0.1475}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-16 09:00:00'}, {'dt': 1542369600, 'main': {'temp': 273.085, 'temp_min': 273.085, 'temp_max': 273.085, 'pressure': 989.34, 'sea_level': 1024.77, 'grnd_level': 989.34, 'humidity': 83, 'temp_kf': 0}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}], 'clouds': {'all': 88}, 'wind': {'speed': 7.2, 'deg': 318.002}, 'rain': {}, 'snow': {'3h': 0.12}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-16 12:00:00'}, {'dt': 1542380400, 'main': {'temp': 273.097, 'temp_min': 273.097, 'temp_max': 273.097, 'pressure': 991.13, 'sea_level': 1026.53, 'grnd_level': 991.13, 'humidity': 81, 'temp_kf': 0}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'clouds': {'all': 88}, 'wind': {'speed': 6.81, 'deg': 325.501}, 'rain': {}, 'snow': {'3h': 0.11}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-16 15:00:00'}, {'dt': 1542391200, 'main': {'temp': 274.103, 'temp_min': 274.103, 'temp_max': 274.103, 'pressure': 992.02, 'sea_level': 1027.1, 'grnd_level': 992.02, 'humidity': 78, 'temp_kf': 0}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'clouds': {'all': 64}, 'wind': {'speed': 6.11, 'deg': 324.501}, 'rain': {}, 'snow': {'3h': 0.035}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-16 18:00:00'}, {'dt': 1542402000, 'main': {'temp': 273.863, 'temp_min': 273.863, 'temp_max': 273.863, 'pressure': 992.32, 'sea_level': 1027.52, 'grnd_level': 992.32, 'humidity': 72, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 64}, 'wind': {'speed': 5.55, 'deg': 321.001}, 'rain': {}, 'snow': {'3h': 0.005}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-16 21:00:00'}, {'dt': 1542412800, 'main': {'temp': 272.045, 'temp_min': 272.045, 'temp_max': 272.045, 'pressure': 994.46, 'sea_level': 1029.87, 'grnd_level': 994.46, 'humidity': 73, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 68}, 'wind': {'speed': 4.38, 'deg': 324.504}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-17 00:00:00'}, {'dt': 1542423600, 'main': {'temp': 270.706, 'temp_min': 270.706, 'temp_max': 270.706, 'pressure': 996.09, 'sea_level': 1031.85, 'grnd_level': 996.09, 'humidity': 78, 'temp_kf': 0}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13n'}], 'clouds': {'all': 76}, 'wind': {'speed': 3.74, 'deg': 339.001}, 'rain': {}, 'snow': {'3h': 0.03}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-17 03:00:00'}, {'dt': 1542434400, 'main': {'temp': 268.675, 'temp_min': 268.675, 'temp_max': 268.675, 'pressure': 997.83, 'sea_level': 1033.93, 'grnd_level': 997.83, 'humidity': 80, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 36}, 'wind': {'speed': 3.56, 'deg': 343.001}, 'rain': {'3h': 0.005}, 'snow': {'3h': 0.02}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-17 06:00:00'}, {'dt': 1542445200, 'main': {'temp': 266.461, 'temp_min': 266.461, 'temp_max': 266.461, 'pressure': 1000.34, 'sea_level': 1036.61, 'grnd_level': 1000.34, 'humidity': 86, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'clouds': {'all': 32}, 'wind': {'speed': 3.76, 'deg': 338.002}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-17 09:00:00'}, {'dt': 1542456000, 'main': {'temp': 265.161, 'temp_min': 265.161, 'temp_max': 265.161, 'pressure': 1002.5, 'sea_level': 1038.9, 'grnd_level': 1002.5, 'humidity': 86, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'clouds': {'all': 48}, 'wind': {'speed': 4, 'deg': 343.5}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-11-17 12:00:00'}, {'dt': 1542466800, 'main': {'temp': 266.031, 'temp_min': 266.031, 'temp_max': 266.031, 'pressure': 1005.8, 'sea_level': 1042.17, 'grnd_level': 1005.8, 'humidity': 76, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 44}, 'wind': {'speed': 4.46, 'deg': 337.001}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-17 15:00:00'}, {'dt': 1542477600, 'main': {'temp': 268.973, 'temp_min': 268.973, 'temp_max': 268.973, 'pressure': 1007.2, 'sea_level': 1043.36, 'grnd_level': 1007.2, 'humidity': 72, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'clouds': {'all': 20}, 'wind': {'speed': 5.27, 'deg': 334.509}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-17 18:00:00'}, {'dt': 1542488400, 'main': {'temp': 269.056, 'temp_min': 269.056, 'temp_max': 269.056, 'pressure': 1007.48, 'sea_level': 1043.65, 'grnd_level': 1007.48, 'humidity': 64, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 8}, 'wind': {'speed': 5.76, 'deg': 334.503}, 'rain': {}, 'snow': {'3h': 0.005}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-11-17 21:00:00'}], 'city': {'id': 420019793, 'name': 'Saint Paul', 'coord': {'lat': 45.0061, 'lon': -93.1567}, 'country': 'US'}}
        # API call
        res = requests.get(url)
        self.rawData = res.json()


    def readWeatherRawData(self):
        """
        Method responsible for reading the raw data received and creating 'Day' objects to sotre the weather information.
        """

        # Read today's weather
        if self.weatherRequested == 'todayWeather':
            self.weatherData.append(day.Day(curr=self.rawData['main']['temp'], min=self.rawData['main']['temp_min'], max=self.rawData['main']['temp_max'], description=self.rawData['weather'][0]['description'], snow=0, date=str(date.today())))

        # Read 5 days forecast
        elif self.weatherRequested == '5daysWeather':
            self.readFiveDaysRawData()

        else:
            print("tomorrow - not done")


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

        self.totalOfDays = 0

        while countList < self.rawData['cnt']:
            # Find the min and max temperatures for the same day and adds the amount of snow
            min = getTheLess(self.rawData['list'][countList]['main']['temp_min'], min)
            max = getTheGreater(self.rawData['list'][countList]['main']['temp_max'], max)
            if 'snow' in self.rawData['list'][countList]:
                value = list(self.rawData['list'][countList]['snow'].values())
                if value:
                    snow = snow + value[0]

            # If it is the last entry on data OR the next entry refers to a different day, then creates a new 'Day' and stores the data
            if (countList == self.rawData['cnt'] - 1) or (self.rawData['list'][countList]['dt_txt'][0:10] != self.rawData['list'][countList + 1]['dt_txt'][0:10]):
                self.weatherData.append(day.Day(0, min, max, self.rawData['list'][countList]['weather'][0]['description'], snow, self.rawData['list'][countList]['dt_txt'][0:10]))
                self.totalOfDays = countDays + 1
                min = 1000
                max = -1000
                snow = 0
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

    def getTotalOfDays(self):
        return self.totalOfDays

    def getDate(self, dayRequested):
        day = dayRequested
        return self.weatherData[day].getDay()