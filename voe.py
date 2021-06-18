import pyttsx3
import datetime
from tkinter import ttk
import os
from tkinter import *


voe_app = Tk()

voe_app.title('Voice Over Engine')
# voe_app.wm_iconbitmap('icon.ico')
voe_app.maxsize(900, 600)
voe_app.minsize(900, 600)
voe_app.configure(bg='red') 


engine = pyttsx3.init()

# function for speaking or responding
def speaking():  
	data = enter_text_entry.get(1.0, END)
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	rate = rate_data.get()
	if rate:
		engine.setProperty('rate', rate)
		engine.say(data)
		engine.runAndWait()


def clear_all():
	enter_text_entry.delete(1.0, END)


def save_audio():
	data = enter_text_entry.get(1.0, END)
	if data:
		date = datetime.datetime.now().day
		engine.save_to_file(data, 'voe_' + str(date) + '.mp3')
		engine.runAndWait()
		print('Done')

mytext = "Voice Over Engine"

header = Frame(voe_app, height=5)
header.pack(pady=10, padx=10)

enter_text_label = Label(header, text='Enter Text', font=('bold', 14), padx=5)
enter_text_label.grid(row=1, column=2, pady=5, padx=50)

middle = Frame(voe_app, height=20)
middle.pack(pady=10)

enter_text_entry = Text(middle, width=60, height=15, font=('helvetica', 14))
enter_text_entry.grid(row=2, column=3)

footer = Frame(voe_app, height=7)
footer.pack(padx=10, pady=10)

clear_btn = Button(footer, text='Clear Text!', font=('bold', 11), pady=5, padx=3, command=clear_all)
clear_btn.grid(row=0, column=1, pady=5, padx=10)

save_btn = Button(footer, text='Save Audio', font=('bold', 12), pady=5, padx=3, command=save_audio)
save_btn.grid(row=0, column=2, pady=5)

genarate_btn = Button(footer, text='Genarate Audio', font=('bold', 11), command=speaking, pady=5, padx=3)
genarate_btn.grid(row=0, column=3, pady=5, padx=10)

rate_data = IntVar()
rateLabel = Label(footer, text='Rate Range', font=('bold', 11), padx=5)
rateLabel.grid(row=1, column=2, padx=5, pady=10)
rate_comboBtn = ttk.Combobox(footer, textvariable=rate_data, width = 10)
rate_comboBtn['values'] = (100, 125, 130, 135, 150, 175, 185)
rate_comboBtn.grid(row=1, column=3, columnspan=2, padx=5, pady=10)

voe_app.mainloop()