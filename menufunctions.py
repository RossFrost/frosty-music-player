from main import definitions
from tkinter import N, Grid
from audio import audioEntryManager
from PySide6.QtWidgets import *
from math import floor


class displayDumpWidgetProperties:
    textWidth       = 250
    textHeight      = 20


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
