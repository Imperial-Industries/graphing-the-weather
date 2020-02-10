from requests import get
import matplotlib.pyplot as plt
from dateutil import parser
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/2801460'
weather = get(url).json()
temperatures = []
for record in weather['items']:
	temperature = record['ambient_temp']
	temperatures.append(temperature)
timestamps = []
for record in weather['items']:
	timestamp = parser.parse(record['reading_timestamp'])
	timestamps.append(timestamp)
plt.plot(timestamps, temperatures)
plt.ylabel("Temperature")
plt.xlabel("Timestamp")
plt.show()
