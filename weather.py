import tkinter as tk
import requests

HEIGHT = 300   
WIDTH = 400

#f986c757443523b20c36ac886090f9a1
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

def test_function(entry):
    print("This is the entry", entry)

def get_weather(city):
    weather_key = 'f986c757443523b20c36ac886090f9a1'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'APPID': weather_key,
        'q': city,
        'units': 'imperial'
    }
    response = requests.get(url, params = params) 
    weather = response.json() 

    print(weather['name'])
    print(weather['weather'][0]['description']) # weather is the '' in json file. Inside weather we want the first entry, which is the first {}, from there we want description that is in the first {}
    print(weather['main']['temp'])



root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame1 = tk.Frame(root, bg = "#80c1ff")  #it will be passed in root
frame1.place(relx = 0.5, rely = 0.1, relheight = 0.1, relwidth = 0.8, anchor = 'n')

entry = tk.Entry(frame1, fg = 'black', bg = 'white')
entry.place(relx = 0.05, rely = 0.2, relwidth = 0.5, relheight = 0.6)

button = tk.Button(frame1, text = "Get Weather", fg = 'black', bg = '#D8D8D8', command = lambda: get_weather(entry.get())) #entry.get gets the information from entry, lambda temporarily stores the variable in memory to be passed into the function
button.place(relx = 0.65, rely = 0.2, relwidth = 0.3, relheight = 0.6)

lowerFrame = tk.Frame(root, bg = "#80c1ff", bd = 10)  #it will be passed in root
lowerFrame.place(relx = 0.5, rely = 0.25, relheight = 0.6, relwidth = 0.8, anchor = 'n')

label_empty = tk.Label(lowerFrame)
label_empty.place(relheight = 1, relwidth = 1)


root.mainloop()