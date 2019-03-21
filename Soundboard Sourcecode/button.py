from mutagen.mp3 import MP3
import filehandler as fh
import misc


class Button():
    """Kümmert sich um die Speicherung von
     Daten und handled den eigenen button"""

    def __init__(self, number):
        self.songadress = ""
        self.songlength = 0
        self.songname = "+"
        self.todelete = False
        self.number = number
        self.player = ""
        self.manager = None

    def clicked(self):
        if self.todelete is True:
            self.reset()
        elif self.songadress == "":
            self.add()
        elif self.songadress:
            self.player.update_song(
                adress=self.songadress,
                length=self.songlength, name=self.songname)
            self.player.start_song()

    def init_song(self, player, manager):
        self.player = player
        self.manager = manager
        self.update()
        self.get_songlength()

    def get_songlength(self):
        try:
            audio = MP3(self.songadress)
            length = audio.info.length
            self.songlength = round(length)
        except Exception:
            self.songlength = 0

    def add(self):
        name = ""
        adress = misc.search_file()
        if adress.strip() != "":
            name = misc.get_name_window()
        if name.strip() == "" or adress.strip() == "":
            name = ""
            adress = ""
        fh.save_values(self.number, name, adress)
        self.update()
        self.get_songlength()

    def update(self):
        try:
            list = fh.get_button_info(self.number)
            self.songname, self.songadress = list
            self.songadress = self.songadress.strip()
        except Exception:
            pass

    def buttonname(self):
        return self.songname

    def set_to_delete(self, bool):
        self.todelete = bool

    def reset(self):
        songadress = self.songadress
        songname = self.songname
        self.songadress = ""
        self.songlength = 0
        self.songname = "+"
        fh.delete_value(self.number)
        self.manager.button_deleted()
        self.player.del_update(songadress, songname)
