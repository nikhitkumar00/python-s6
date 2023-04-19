"""
File: songbrowser2.py
Author: Kenneth A. Lambert
"""

from breezypythongui import EasyFrame, EasyDialog
from tkinter import END, NORMAL, DISABLED
import tkinter.filedialog
from song import SongDatabase, Song

class SongBrowser(EasyFrame):
    """Allows the user to browse songs in a database file, create them,
    edit them, delete them, and save the database to a file."""
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Song Browser",
                           width = 300, height = 150)

        # Create a model
        self.database = SongDatabase()
        self.selectedTitle = ""

        # Set up the menus
        menuBar = self.addMenuBar(row = 0, column = 0, columnspan = 2)
        fileMenu = menuBar.addMenu("File")
        fileMenu.addMenuItem("Open", self.openFile)
        fileMenu.addMenuItem("Save", self.saveFile)
        fileMenu.addMenuItem("Save As...", self.saveFileAs)
        
        editMenu = menuBar.addMenu("Edit")
        self.findMI = editMenu.addMenuItem("Find", self.findSong,
                                           state = DISABLED)
        editMenu.addMenuItem("New", self.newSong)
        self.modifyMI = editMenu.addMenuItem("Modify", self.editSong,
                                             state = DISABLED)
        self.deleteMI = editMenu.addMenuItem("Delete", self.deleteSong,
                                             state = DISABLED)

        # Set up the list box
        self.listBox = self.addListbox(row = 1, column = 0, width = 20,
                                       listItemSelected = self.listItemSelected)

        # Set the text area
        self.outputArea = self.addTextArea("", row = 1, column = 1,
                                           width = 30, height = 4)


    # Event handling methods
    def listItemSelected(self, index):
        """Responds to the selection of an item in the list box.
        Updates the selected title and the text area with the
        current song's info."""
        self.selectedTitle = self.listBox.getSelectedItem()
        if self.selectedTitle == "":
            self.outputArea.setText("")
            self.findMI.setState(DISABLED)
            self.modifyMI.setState(DISABLED)
            self.deleteMI.setState(DISABLED)
        else:
            self.outputArea.setText(str(self.database[self.selectedTitle]))
            self.findMI.setState(NORMAL)
            self.modifyMI.setState(NORMAL)
            self.deleteMI.setState(NORMAL)

    def openFile(self):
        """Pops up an open file dialog.  Updates the view if
        a file is opened."""
        filetypes = [("Database files", "*.dat")]
        fileName = tkinter.filedialog.askopenfilename(parent = self,
                                                      filetypes = filetypes)
        if fileName == "": return
        self.database = SongDatabase(fileName)
        self.listBox.clear()
        for title in self.database.getTitles():
            self.listBox.insert(END, title)
        self.listBox.setSelectedIndex(0)
        self.listItemSelected(0)

    def saveFile(self):
        """If the database has a file name, saves it to the file.
        Otherwise, calls saveFileAs to prompt the user for a file
        name."""
        if self.database.fileName != "":
            self.database.save()
        else:
            self.saveFileAs()

    def saveFileAs(self):
        """Pops up a dialog to save the database to a file."""
        fileName = tkinter.filedialog.asksaveasfilename(parent = self)
        if fileName != "":
            self.database.save(fileName)

    def findSong(self):
        """Prompts the user for a title and searches for the song.
        Selects and updates if found."""
        if self.selectedTitle == "": return
        title = self.prompterBox(title = "Find",
                                 promptString = "Enter a song's title")
        if title == "": return
        song = self.database[title]
        if not song:
            self.messageBox(message = title + " was not found")
        else:
            index = self.listBox.getIndex(title)
            self.listBox.setSelectedIndex(index)            
            self.listItemSelected(index)

    def newSong(self):
        """Pops up a dialog to edit a new song.  Adds the song to the
        database and updates the app window if song was modified."""
        song = Song("", "", 0.00)
        dialog = SongDialog(self, song)
        if dialog.modified():
            self.insertSong(song)

    def editSong(self):
        """Pops up a dialog to edit the currently selected song.
        Updates the app window if song was modified."""
        if self.selectedTitle == "": return
        song = self.database[self.selectedTitle]
        dialog = SongDialog(self, song)
        if dialog.modified():
            self.deleteSong()
            self.insertSong(song)

    def insertSong(self, song):
        """Inserts song and updates the view."""
        self.database[song.title] = song
        self.listBox.clear()
        for title in self.database.getTitles():
            self.listBox.insert(END, title)
        index = self.listBox.getIndex(song.title)
        self.listBox.setSelectedIndex(index)            
        self.listItemSelected(index)

    def deleteSong(self):
        """Deletes the selected song from the database and updates the view."""
        if self.selectedTitle:
            self.database.pop(self.selectedTitle)
            index = self.listBox.getSelectedIndex()
            self.listBox.delete(index)
            if self.listBox.size() > 0:
                if index > 0:
                    index -= 1
                self.listBox.setSelectedIndex(index)
                self.listItemSelected(index)
            else:
                self.listItemSelected(-1)


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


# Instantiate and pop up the window."""
if __name__ == "__main__":
    SongBrowser().mainloop()
