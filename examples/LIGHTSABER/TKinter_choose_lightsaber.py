import tkinter as tk

window = tk.Tk() #object that is root window
window.title('TKInter')

text = tk.Label(text = "CHOOSE a lightsaber colour", foreground='yellow',
                background='black', width=30, height=3)
#text.pack()

entry = tk.Entry(width=30)
#entry.pack()

def save_and_print():
    name=entry.get() #colour, type 'string'
    entry.delete(0, tk.END)
    print(name)
    
def colourchangebg():
    entry.delete
    button.delete
    label.delete
    print(button)
    
buttonblue=tk.Button(text='Blue', width=30, height=1, background='blue',
                 foreground='white', command = save_and_print)
buttongreen=tk.Button(text='Green', width=30, height=1, background='green',
                 foreground='white', command = save_and_print)
buttonpurple=tk.Button(text='Purple', width=30, height=1, background='purple',
                 foreground='white', command = save_and_print)
buttonyellow=tk.Button(text='Yellow', width=30, height=1, background='yellow',
                 foreground='black', command = save_and_print)
buttonwhite=tk.Button(text='White', width=30, height=1, background='white',
                 foreground='black', command = save_and_print)

#button.pack(padx = 5, pady = 5)

window.bind('<Return>', lambda event:save_and_print())

frame = tk.Frame(master = window)
label = tk.Label(master = window, text = 'Frame!', bg='black',
                 fg='white')

frame.columnconfigure(0, weight = 1)
frame.columnconfigure(1, weight = 3)

text.grid(column = 0, row = 0, padx = 5, pady = 5)
entry.grid(column = 0, row = 1, padx = 5, pady = 5)
buttonblue.grid(column = 1, row = 0, padx = 5, pady = 5)
buttongreen.grid(column = 1, row = 1, padx = 5, pady = 5)
buttonpurple.grid(column = 1, row = 2, padx = 5, pady = 5)
buttonyellow.grid(column = 1, row = 3, padx = 5, pady = 5)
buttonwhite.grid(column = 1, row = 4, padx = 5, pady = 5)


window.mainloop() #start event loop

