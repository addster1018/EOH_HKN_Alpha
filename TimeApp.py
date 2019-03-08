import datetime
import tkinter as tk

currentDT = datetime.datetime.now()
date_str = (currentDT.strftime("%a %b %d, %Y"))
time_str = (currentDT.strftime("%I:%M:%S %p"))

out_str = "The current time is " + time_str + " on " + date_str

m=tk.Tk(className = "TIME")

# widgets
Alexa_str = tk.Message(m, text="Alexa, What Time Is It?\n", width = 500, font=('Arial', 36))
Alexa_str.pack()
text = tk.Message(m, text = out_str, width=400, font=("Courier New", 24))
text.pack()
button = tk.Button(m, text='Stop', width=150, command=m.destroy)
button.pack()

m.mainloop()
