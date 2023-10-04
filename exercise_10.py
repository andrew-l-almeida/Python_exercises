#Write a program that asks the temperature in Celsius and transform to Fahreinheit  

def fahreinheitConverter(temperatureInCelsius):
    return int((1.8 * temperatureInCelsius + 32))

temperature = int(input('Type the temperature in Celsius: '))

print('The temperature {} Celsius equals to {} Fahreinheit'.format(temperature, fahreinheitConverter(temperature)))