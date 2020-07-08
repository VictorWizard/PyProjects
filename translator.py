# -*- coding: utf-8 -*-

import requests
import sys
from tkinter import *


def translate(mytext):
    global lang
    key = 'trnsl.1.1.20191101T085633Z.a3db60cbc3e01343.1423cca2c7aa1755c4ce5d6c44f8c330b992599d'
    data = {'lang':lang,
            'key':key,
            'text':mytext, 
            'format':'plain'
            } 
    r = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', data = data).json()
    if r['code'] == 200:
        global result
        result = r['text'][0] + '\n'
        return result
    else:
        return 'error'


def output(event):
    global lang
    text = ent.get()
    lang = lan.get()
    translate(text)
    tex.delete(1.0,END)
    tex.insert(1.0, result)
    

def translator():
    global lan, ent, but, tex
    root = Tk()
    root.title("Переводчик")
    root.minsize(width = 400, height=400)
    frame1 = LabelFrame(text="Введите язык перевода")
    frame2 = Frame(root)
    frame3 = Frame(root)
    frame4 = Frame(root)
    lan = Entry(frame1,width=10)
    ent = Entry(frame2,width=50)
    but = Button(frame3,text="Перевод")
    tex = Text(frame4,width=50,font="12")
    frame1.pack()
    frame2.pack()
    frame3.pack()
    frame4.pack()
    lan.grid(row=0,column=0,padx=40,pady=10)
    ent.grid(row=1,column=0,padx=20, pady=20)
    but.grid(row=1,column=1)
    tex.grid(row=1,column=2,padx=20,pady=10)
    but.bind("<Button-1>",output)
    root.mainloop()


translator()
        
        
