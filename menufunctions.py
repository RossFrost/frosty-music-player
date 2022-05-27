from tkinter import N, Grid
from audio import audioEntryManager
from PySide6.QtWidgets import *


class displayDataEntryMain:
    def __init__(self, name, trackname, artist, composer, date, length, directory) -> None:
        self.name       = name
        self.trackname  = trackname
        self.artist     = artist
        self.composer   = composer
        self.date       = date
        self.length     = length
        self.directory  = directory

class displaySettingsMain:
    def __init__(self) -> None:
        self.name       = False, 0, "name"
        self.trackname  = True,  1, "trackname"
        self.artist     = True,  2, "artist"
        self.composer   = False, 3, "composer"
        self.date       = False, 4, "date"
        self.length     = True,  5, "length"
        self.playlist   = True,  6, "playlist"
        self.playlength = False, 7, "playlength"
        self.directory  = False, 8, "directory"

        self.settings = [
                        self.name,
                        self.trackname,
                        self.artist,
                        self.composer,
                        self.date,
                        self.length,
                        self.playlist,
                        self.playlength,
                        self.directory
                       ]

    def displayList(self) -> list:
        displayTrueList = []
        for item in self.settings:
            if item[0]:
                displayTrueList.append(item[2])
        return displayTrueList 

    def displayCount(self) -> int:
        return len(self.displayList())

    def displayOrder(self) -> list:
        positions = []
        for position in self.settings:
            if position[0]:
                positions.append((position[1], position[2]))
        positions.sort(key = lambda item: item[0])
        return positions
    

        
class settingsManager:
    def __init__(self) -> None:
        pass



class displayDumpWidgetProperties:
    textWidth       = 250
    textHeight      = 20

def updateDisplayMain():
    pass

def displayDump(manager: audioEntryManager) -> list:
    dump = manager.entries
    entryList = []

    for entry in dump:
        entry: str
        entryData = {}

        item    = QListWidgetItem()
        widget  = QWidget()
        layout  = QGridLayout()
        button  = QPushButton("Add")
        text    = QLabel(entry)

        text.setWordWrap(True)
        text.setFixedWidth(displayDumpWidgetProperties.textWidth)
            
        layout.addWidget(text, 0, 0)
        layout.addWidget(button, 0, 1)
        layout.setSizeConstraint(QLayout.SetFixedSize)
        widget.setLayout(layout)

        item.setSizeHint(layout.sizeHint())

        entryData["item"]   = item
        entryData["widget"] = widget

        entryList.append(entryData)

    return entryList

