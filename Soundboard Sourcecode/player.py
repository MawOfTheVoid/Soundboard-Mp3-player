from pygame import mixer


class Player():
    """Handles everything concerning the current song"""

    def __init__(self):
        mixer.init()
        self.currentlength = 0
        self.currentadress = ""
        self.name = ""
        self.plogo = "||"
        self.endless = True
        self.elogo = "Loop ✓"
        self.percent = 0
        self.playing = False

    def update_song(self, adress, length, name):
        try:
            self.currentadress = adress
            self.currentlength = length
            self.name = name
            mixer.music.load(adress)
        except Exception:
            pass

    def play(self):
        if self.playing is True:
            mixer.music.pause()
            self.plogo = "▶"
            self.playing = False
        elif self.playing is False:
            mixer.music.unpause()
            self.plogo = "||"
            self.playing = True
        if mixer.music.get_busy() == 0:
            self.plogo = "||"

    def endlesssong(self):
        if self.endless is True:
            self.endless = False
            self.elogo = "Loop ✗"
        elif self.endless is False:
            self.endless = True
            self.elogo = "Loop ✓"

    def volumecontrol(self, volume):
        volume = float(volume) * 0.01
        mixer.music.set_volume(volume)

    def progressmeter(self):
        current = mixer.music.get_pos()
        current = current / 1000
        try:
            self.percent = (current / self.currentlength) * 100
        except Exception:
            self.percent = 0
        return self.percent

    def restart(self):
        if self.playing is False:
            self.plogo = "||"
        mixer.music.load(self.currentadress)
        mixer.music.play()

    def get_plogo(self):
        return self.plogo

    def get_elogo(self):
        return self.elogo

    def start_song(self):
        mixer.music.load(self.currentadress)
        mixer.music.play()
        self.playing = True

    def restart_loop(self):
        if self.endless is True:
            if self.percent <= 101 and self.percent >= 100:
                mixer.music.load(self.currentadress)
                mixer.music.play()
            elif self.percent <= 100 and self.percent >= 99:
                mixer.music.load(self.currentadress)
                mixer.music.play()
            elif self.percent > 100:
                mixer.music.load(self.currentadress)
                mixer.music.play()

    def get_current_song(self):
        if self.name == "+":
            return ""
        else:
            return self.name

    def del_update(self, adress, name):
        if adress == self.currentadress and \
                name == self.name:
            mixer.music.stop()
            self.update_song("", 0, "")
