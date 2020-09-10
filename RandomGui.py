import tkinter as tk

HEIGHT = 250   
WIDTH = 300

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

""" frame = tk.Frame(root, bg = "#80c1ff")  #it will be passed in root
frame.place(relx = 0.1, rely = 0.1, relheight = 0.8, relwidth = 0.8)

button = tk.Button(frame, text = "Test Button", bg = "gray") #frame is where we pass it in
button.place(relx=0, rely=0, relheight=0.25, relwidth=0.4) """

""" label = tk.Label(frame, text="This is a label", bg='yellow')
label.pack(side = 'top')

entry = tk.Entry(frame, bg='green')
entry.pack(side = 'top')
 """


root.mainloop()