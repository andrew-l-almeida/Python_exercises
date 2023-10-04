#Make a program that asks the temperature in Fahrenheit, transform and show the temperature in Celsius
# C = (F - 32) / 1,8
def celsiusConverter(temperatureInFahrenheit):
    return ((temperatureInFahrenheit - 32) / 1.8)

temperature = int(input('Type a temperature in fahreinheint: '))

print('The temperature {} fahreinheint is equal to {} Celsius'.format(temperature, int(celsiusConverter(temperature))))