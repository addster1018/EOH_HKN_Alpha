import urllib
from urllib.request import urlopen
import ast
import tkinter as tk

url = "http://api.openweathermap.org/data/2.5/weather?zip=61801,us&APPID=d556e90c6c6276a06c70a7a304572772"

#req = urllib.Request(url)
response = urlopen(url)
the_page = response.read()

#print(the_page)

page_dict = ast.literal_eval(the_page.decode('UTF-8'))

temp_F = (float(page_dict['main']['temp']) - 273.15) * 9/5 + 32

out_str = "The Current Temperature in Urbana, IL is: " + str(temp_F) + " °F"

m=tk.Tk(className = "WEATHER")

# widgets
Alexa_str = tk.Message(m, text="Alexa, What's the Temperature Outside?\n", width = 500, font=('Arial', 36))
Alexa_str.pack()
text = tk.Message(m, text = out_str, width=400, font=("Courier New", 24))
text.pack()
button = tk.Button(m, text='Stop', width=150, command=m.destroy)
button.pack()

m.mainloop()
