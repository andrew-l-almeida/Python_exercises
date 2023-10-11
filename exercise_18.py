"""
Create a program that asks for the size of a file to download (in MB) and the speed of an Internet connection (in Mbps), calculate and inform the approximate download time for the file using this connection (in minutes).
"""

#Simple form

import math
import os
internetSpeed = float(input('Type the internet speed in Mbps: '))
choice = int(input('1 - Simple / 2 - Complex'))

def calculateDownloadTime(fileSize, internetSpeed):
        return math.ceil(fileSize / internetSpeed / 60)

if(choice == 1):
    fileSize = float(input('Type the size of the file in MB: '))
    print('Approximate download time is {} minutes'.format(calculateDownloadTime(fileSize, internetSpeed)))
else:
    path = "C:\FS\Emissao\EmissaoNFE.exe"
    size = os.path.getsize(path) / (1024 * 1024)

    print('Approximate download time is {} minutes'.format(calculateDownloadTime(size, internetSpeed)))