import tkinter.filedialog as guifile
import tkinter as gui


class DelManager():

    def __init__(self):
        self.to_delete = False
        self.buttonlist = []

    def get_list(self, list):
        self.buttonlist = list

    def delete_pressed(self):
        if self.to_delete is False:
            self.to_delete = True
            for button in self.buttonlist:
                button.set_to_delete(self.to_delete)
        elif self.to_delete is True:
            self.to_delete = False
            for button in self.buttonlist:
                button.set_to_delete(self.to_delete)

    def button_deleted(self):
        self.to_delete = False
        for button in self.buttonlist:
            button.set_to_delete(self.to_delete)

    def get_del_button_state(self):
        if self.to_delete is False:
            return "raised"
        elif self.to_delete is True:
            return "sunken"


def search_file():
    file = guifile.askopenfilename(filetypes=(("Mp3 Dateien", "*.mp3"),))
    return file


class Save():

    def __init__(self):
        self.name = "+"
        self.flag = True

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


def get_name_window():
    save = Save()

    def clicked(save):
        save.set_name(name=txt.get())
        window2.destroy()
        save.flag = False
    window2 = gui.Toplevel()
    window2.title("Naming")
    txt = gui.Entry(window2, width=35)
    txt.focus()
    txt.grid(row=0, column=0)
    btn = gui.Button(
        window2, text="OK", width=7, command=lambda: clicked(save))
    btn.grid(row=0, column=1)
    window2.bind("<Return>", lambda x: clicked(save=save))
    while save.flag:
        window2.update()
    return save.name


class Popup():

    def __init__(self, window):
        self.top = gui.Toplevel(window)
        self.entry = gui.Entry()
        self.entry.grid(row=0, column=0)
        self.button = gui.Button(text="OK", command=self.close)
        self.button.grid(row=0, column=1)
        self.value = ""

    def close(self):
        self.value = self.entry.get()
        self.window.destroy()
