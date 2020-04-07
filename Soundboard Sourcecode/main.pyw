import tkinter.ttk as ttk
import tkinter as gui
import button as btn
import player
from filehandler import is_file_there
import misc


def higher_volume():
    vol = volume.get()
    vol = vol + 3
    if vol <= 100:
        volume.set(vol)
    elif vol > 100:
        volume.set(100)


def lower_volume():
    vol = volume.get()
    vol = vol - 3
    if vol >= 0:
        volume.set(vol)
    elif vol < 0:
        volume.set(0)


def updateloop():
    try:
        while True:
            progressvar.set(dj.progressmeter())
            loop.configure(text=dj.get_elogo())
            dj.restart_loop()
            play.configure(text=dj.get_plogo())
            btn1.configure(text=nb1.buttonname())
            btn2.configure(text=nb2.buttonname())
            btn3.configure(text=nb3.buttonname())
            btn4.configure(text=nb4.buttonname())
            btn5.configure(text=nb5.buttonname())
            btn6.configure(text=nb6.buttonname())
            btn7.configure(text=nb7.buttonname())
            btn8.configure(text=nb8.buttonname())
            btn9.configure(text=nb9.buttonname())
            current.configure(text=dj.get_current_song())
            delete.configure(relief=delete_manager.get_del_button_state())
            window.update()
        window.after(0, updateloop)
    except Exception:
        pass


is_file_there()

window = gui.Tk()
window.title("Soundboard")

window.iconbitmap(default="lavalamp.ico")


delete_manager = misc.DelManager()
progressvar = gui.DoubleVar()
play = gui.StringVar()

dj = player.Player()

nb1 = btn.Button(1)
nb1.init_song(dj, delete_manager)

nb2 = btn.Button(2)
nb2.init_song(dj, delete_manager)

nb3 = btn.Button(3)
nb3.init_song(dj, delete_manager)

nb4 = btn.Button(4)
nb4.init_song(dj, delete_manager)

nb5 = btn.Button(5)
nb5.init_song(dj, delete_manager)

nb6 = btn.Button(6)
nb6.init_song(dj, delete_manager)

nb7 = btn.Button(7)
nb7.init_song(dj, delete_manager)

nb8 = btn.Button(8)
nb8.init_song(dj, delete_manager)

nb9 = btn.Button(9)
nb9.init_song(dj, delete_manager)


btn_list = [nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]
delete_manager.get_list(btn_list)

btn1 = gui.Button(window, command=nb1.clicked, width=11)
btn2 = gui.Button(window, command=nb2.clicked, width=11)
btn3 = gui.Button(window, command=nb3.clicked, width=11)
btn4 = gui.Button(window, command=nb4.clicked, width=11)
btn5 = gui.Button(window, command=nb5.clicked, width=11)
btn6 = gui.Button(window, command=nb6.clicked, width=11)
btn7 = gui.Button(window, command=nb7.clicked, width=11)
btn8 = gui.Button(window, command=nb8.clicked, width=11)
btn9 = gui.Button(window, command=nb9.clicked, width=11)

progress = ttk.Progressbar(
    orient="horizontal", length=170, variable=progressvar)
play = gui.Button(window, text="▶", width=11, command=dj.play, pady=2.5)
restart = gui.Button(
    window, text="Restart", width=11, command=dj.restart, pady=2.5)
open = gui.Button(window, text="Open", width=11, pady=2.5)
delete = gui.Button(
    window, text="Delete", width=11, pady=0.01,
    command=delete_manager.delete_pressed
    )
loop = gui.Button(
    window, text="Loop" + " ✓", width=11, command=dj.endlesssong, pady=2.5)
current = gui.Label(window, text="Der aktuelle Song", anchor="e")
volume = ttk.Scale(
    window, from_=100, to=0, orient="vertical", command=dj.volumecontrol)
whitespace = gui.Label(window, text="", height=1)
volume.set(100)


btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
progress.grid(row=5, column=0, columnspan=2)
play.grid(row=4, column=0)
restart.grid(row=4, column=1)
delete.grid(row=5, column=2)
loop.grid(row=4, column=2)
current.grid(row=6, column=0, columnspan=4)
volume.grid(row=0, rowspan=5, column=3)

window.bind("1", lambda x: nb1.clicked())
window.bind("2", lambda x: nb2.clicked())
window.bind("3", lambda x: nb3.clicked())
window.bind("4", lambda x: nb4.clicked())
window.bind("5", lambda x: nb5.clicked())
window.bind("6", lambda x: nb6.clicked())
window.bind("7", lambda x: nb7.clicked())
window.bind("8", lambda x: nb8.clicked())
window.bind("9", lambda x: nb9.clicked())
window.bind("r", lambda x: dj.restart())
window.bind("p", lambda x: dj.play())
window.bind("<space>", lambda x: dj.play())
window.bind("l", lambda x: dj.endlesssong())
window.bind("<Up>", lambda x: higher_volume())
window.bind("<Down>", lambda x: lower_volume())

updateloop()
window.mainloop()
