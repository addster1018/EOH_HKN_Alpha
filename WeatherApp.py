import urllib
from urllib.request import urlopen
import ast

url = "http://api.openweathermap.org/data/2.5/weather?zip=61801,us&APPID=d556e90c6c6276a06c70a7a304572772"

#req = urllib.Request(url)
response = urlopen(url)
the_page = response.read()

#print(the_page)

page_dict = ast.literal_eval(the_page.decode('UTF-8'))

temp_F = (float(page_dict['main']['temp']) - 273.15) * 9/5 + 32

print("Temp: " + str(temp_F) + " degrees Fahrenheit")