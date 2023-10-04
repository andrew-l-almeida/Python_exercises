# Write a program that converts meters to centimeters.

def centimetersConverter(meters):
    return meters*100

meters = float(input('Type a distance to convert to centimeters: '))
centimeters = centimetersConverter(meters)

print('{} meters in centimeters = {}.'.format(meters,centimeters))
