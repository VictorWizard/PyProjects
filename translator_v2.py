# -*- coding: utf-8 -*-

import requests
import sys
from tkinter import *

class yandex_translate(object):
    def __init__(self):
        root = Tk()
        root.title("Переводчик")
        root.minsize(width = 400, height=400)
        frame1 = LabelFrame(text="Введите язык перевода")
        frame2 = Frame(root)
        frame3 = Frame(root)
        frame4 = Frame(root)
        self.lan = Entry(frame1,width=10)
        self.ent = Entry(frame2,width=50)
        self.but = Button(frame3,text="Перевод")
        self.tex = Text(frame4,width=50,font="12")
        frame1.pack()
        frame2.pack()
        frame3.pack()
        frame4.pack()
        self.lan.grid(row=0,column=0,padx=40,pady=10)
        self.ent.grid(row=1,column=0,padx=20, pady=20)
        self.but.grid(row=1,column=1)
        self.tex.grid(row=1,column=2,padx=20,pady=10)
        self.but.bind("<Button-1>",self.output)
        root.mainloop()
    def output(self, event):
        self.event = event
        text = self.ent.get()
        self.lang = self.lan.get()
        self.translate(text)
        self.tex.delete(1.0,END)
        self.tex.insert(1.0, self.result)
    def translate(self, mytext):
        self.mytext = mytext
        key = 'trnsl.1.1.20191101T085633Z.a3db60cbc3e01343.1423cca2c7aa1755c4ce5d6c44f8c330b992599d'
        data = {'lang':self.lang,
                'key':key,
                'text':mytext, 
                'format':'plain'
                } 
        r = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', data = data).json()
        if r['code'] == 200:
            self.result = r['text'][0] + '\n'
            return self.result
        else:
            return 'error'


new = yandex_translate()

