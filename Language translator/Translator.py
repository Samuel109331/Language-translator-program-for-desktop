from tkinter import *
from tkinter import messagebox,ttk
import googletrans
from googletrans import Translator
from random import choice
import pyperclip as pc
def trans():
    global inpBox1
    global inpBox2
    global from_lang
    global to_lang
    global var1
    global var2
    text = inpBox1.get(1.0,END).replace("\n"," ")
    tr = Translator()
    if var1.get() == "Detect language":
        translated = tr.translate(text,dest=var2.get())
        inpBox2.delete(1.0,END)
        inpBox2.insert(END,f"{translated.text}+\nPronunciation:{translated.pronunciation}")
    else:
        translated = tr.translate(text,src=var1.get(),dest=var2.get())
        inpBox2.delete(1.0,END)
        inpBox2.insert(END,f"{translated.text}+\nPronunciation:{translated.pronunciation}")

#get clipboard text
def clipboard_text():
    global inpBox1
    inpBox1.delete(1.0,END)
    inpBox1.insert(END,pc.paste())
win = Tk()
win.iconphoto(True,PhotoImage(file="google.png"))
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry(f"{width}x{height}")
langs = []

for i,j in googletrans.LANGUAGES.items():
    langs.append(j)
t = Translator()
welcome_text = t.translate("Welcome to my simple translator program!",dest=choice(langs))
langs2 = langs.copy()
langs.insert(0,"Detect language")
#From
var1 = StringVar()
var1.set(langs[0])
from_lang = ttk.OptionMenu(win,var1,*langs)
from_lang.grid(row=0,column=0,ipadx=20,padx=15)
inpBox1 = Text(win,width=60,height=10,wrap=WORD,font=("Monospace 11"))
inpBox1.grid(row=0,column=1,padx=15)
#Submit Button
btn = Button(win,text="Translate",command=trans,font=("Consolas 20 bold"))
btn.grid(row=0,column=2,padx=15)
#Paste from clipboard button
clipBoard = Button(win,text="Paste",command=clipboard_text,font=("Consolas 20 bold"))
clipBoard.grid(row=1,column=2)
#To
var2 = StringVar()
var2.set(langs2[0])
to_lang = ttk.OptionMenu(win,var2,*langs2)
to_lang.grid(row=0,column=3,padx=15,ipadx=15)
inpBox2 = Text(win,width=55,height=10,wrap=WORD,font=("Monospace 11"))
inpBox2.grid(row=0,column=4,padx=10)
win.mainloop()