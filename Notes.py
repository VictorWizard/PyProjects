# -*- coding: utf-8 -*-

import os, json
from tkinter import *

directory = 'C:/Notes'
file = "C:/Notes/notes.json"

def checking():
    if not os.path.exists(directory):
        os.mkdir(directory)

    if not os.path.exists(file):
        open(file, "w").close()

class Notes:
    @staticmethod
    def add_note(event):
        global name, note

        a = Toplevel()
        a.geometry('500x630')

        frame1 = Frame(a)
        frame2 = Frame(a)
        frame3 = Frame(a)
        title = Label(frame1, text="Новая заметка", font="Arial 15")
        name_title = Label(frame2, text="Название", font="10")
        name = Entry(frame2, width=50)
        note_title = Label(frame2, text="Заметка", font="10")
        note = Text(frame2, width=40, font="Arial 12", wrap=WORD)
        add_button = Button(frame3, text="Сохранить")
        frame1.pack()
        frame2.pack()
        frame3.pack()
        title.grid(row=0, column=0, padx=0, pady=0)
        name_title.grid(row=0, column=0, padx=20, pady=10)
        name.grid(row=1, column=0, padx=20, pady=0)
        note_title.grid(row=2, column=0, padx=20, pady=10)
        note.grid(row=3, column=0, padx=20, pady=0)
        add_button.grid(row=0, column=0, padx=40, pady=10)
        add_button.bind("<Button-1>", Notes.saving_note)

    @staticmethod
    def saving_note(event):
        _name = name.get()
        _note = note.get(1.0, END)

        checking()

        notes = open(file, "r+")
        temp_notes = {}
        if os.path.getsize(file) > 0:
            temp_notes = json.load(notes)
        temp_notes[_name] = _note
        notes.close()
        open(file, "w").close()

        with open(file, "r+") as notes:
            json.dump(temp_notes, notes)

    @staticmethod
    def show_notes():
        checking()

        with open(file, "r") as notes:
            try:
                content = json.load(notes)
                notes_list = []
                for _name in content.keys():
                    notes_list.append(_name)
                return notes_list
            except:
                print("Couldn't show this")

class MainWindow:
    def __init__(self):
        root = Tk()
        root.title("Заметки")
        root.geometry('500x500')

        frame1 = Frame(root)
        frame2 = Frame(root)
        frame3 = Frame(root)
        title = Label(frame1, text="Список заметок", font="Arial 15")
        notes = Label(frame2, text=Notes.show_notes(), font="Arial 15")
        add_button = Button(frame3, text="Новая заметка")
        frame1.pack()
        frame2.pack()
        frame3.pack()
        title.grid(row=0, column=0, padx=40, pady=10)
        notes.grid(row=1, column=2, padx=20, pady=10)
        add_button.grid(row=0, column=0, padx=40, pady=10)
        add_button.bind("<Button-1>", Notes.add_note)

        root.mainloop()

    def output(self, event):
        pass

new = MainWindow()