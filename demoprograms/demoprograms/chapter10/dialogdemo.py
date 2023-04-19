"""
File: dialogdemo.py
Author: Kenneth A. Lambert
"""

from breezypythongui import EasyFrame, EasyDialog
from song import Song

class DialogDemo(EasyFrame):
    """Demonstrates a dialog."""
    
    def __init__(self):
        """Sets up the model, window, and widgets."""
        EasyFrame.__init__(self, "Dialog Demo")
        self.song = Song("Let It Be", "The Beatles", 0.99)
        self.outputArea = self.addTextArea(text = str(self.song),
                                           row = 0, column = 0,
                                           width = 30, height = 4)
        self.addButton(text = "Edit", row = 1, column = 0,
                       command = self.editSong)
        
    # Event handling method
    def editSong(self):
        """Pops up a dialog to edit the model.
        Updates app window if song was modified."""
        dialog = SongDialog(self, self.song)
        if dialog.modified():
            self.outputArea.setText(str(self.song))

class SongDialog(EasyDialog):
    """Opens a dialog on a song object."""

    def __init__(self, parent, song):
        """Sets up the window."""
        self.song = song
        EasyDialog.__init__(self, parent, "Song Editor")
    
    def body(self, master):
        """Sets up the widgets."""
        self.addLabel(master, text = "Title", row = 0, column = 0)
        self.addLabel(master, text = "Artist", row = 1, column = 0)
        self.addLabel(master, text = "Price", row = 2, column = 0)
        self.titleFld = self.addTextField(master, text = self.song.title,
                                          row = 0, column = 1)
        self.artistFld = self.addTextField(master, text = self.song.artist,
                                           row = 1, column = 1)
        self.priceFld = self.addFloatField(master, value = self.song.price,
                                           row = 2, column = 1, precision = 2)

    # Event handling method
    def apply(self):
        """When the OK button is clicked, transfers data from the
        fields to the song."""
        self.song.title = self.titleFld.getText()
        self.song.artist = self.artistFld.getText()
        self.song.price = self.priceFld.getNumber()
        self.setModified()


if __name__ == "__main__":
    DialogDemo().mainloop()
