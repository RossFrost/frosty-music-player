from genericpath import isfile
from pathlib import Path
import sys
import ntpath as path
import PySide6.QtGui as gui
from menufunctions import *
from PyQt6 import *
from PySide6 import QtCore as core
from PySide6.QtWidgets import *
from files import *
from audio import *
from os import listdir
from os.path import splitext


class definitions:
    top         = core.Qt.AlignTop
    center      = core.Qt.AlignCenter 
    bottom      = core.Qt.AlignBottom

    left        = core.Qt.AlignLeft
    right       = core.Qt.AlignRight





class main(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500, 400)


        queue           = QWidget()
        title           = QLabel("Music Player")
        searchLabel     = QLabel("Search: ", alignment = definitions.center)
        search          = QLineEdit()
        searchButton    = QPushButton("Submit")
        queueLayout     = QGridLayout()

        importLayout    = QGridLayout()
        fileSelector    = QPushButton("Import File")
        folderSelector  = QPushButton("Import Folder")

        menu            = QGroupBox()
        play            = QPushButton("Play")
        stop            = QPushButton("Stop")
        next            = QPushButton("Next")
        previous        = QPushButton("Previous")
        display         = QListWidget()
        menuLayout      = QGridLayout()
        menuShellLayout = QGridLayout()

        importLayout.addWidget(fileSelector,    0, 0    )
        importLayout.addWidget(folderSelector,  0, 1    )

        queueLayout.addWidget(title,            0, 1    )
        queueLayout.addWidget(searchLabel,      1, 0    )
        queueLayout.addWidget(search,           1, 1    )   
        queueLayout.addWidget(searchButton,     1, 2    )
        title.setAlignment(core.Qt.AlignCenter)
        queueLayout.setRowStretch(4, 1)
        queueLayout.setContentsMargins(0, 0, 0, 0)
        queue.setLayout(queueLayout)

        menuLayout.addWidget(play,              0, 0    )   
        menuLayout.addWidget(stop,              1, 0    )
        menuLayout.addWidget(next,              2, 0    )
        menuLayout.addWidget(previous,          3, 0    )
        menu.setLayout(menuLayout)
        menuShellLayout.addWidget(menu,         0, 0    )
        menuShellLayout.addWidget(display,      0, 1    )


        self.layout = QGridLayout(self)
        self.layout.addWidget(queue,            0, 0    )
        self.layout.addLayout(importLayout,     1, 0    )
        self.layout.addLayout(menuShellLayout,  2, 0    )
        self.layout.setRowStretch(4, 1)


        manager = audioEntryManager("display")
        def fileSelectorClick():
            dialog = QFileDialog.getOpenFileNames(self, "Open audio files...", "C:\\", "Audio Files (*.wav *.flac *.ogg *.mp3)")
            
            for filePath in dialog[0]:
                audioName = file(filePath).getFileBaseName()
                manager.addEntry(audioName)
            
            for entry in displayDump(manager):
                display.addItem(entry["item"])
                display.setItemWidget(entry["item"], entry["widget"])

            manager.entries = []
                
        def folderSelectorClick():
            dialog = QFileDialog.getExistingDirectory(self, "Select Folder", "C:\\")
            fold = folder(dialog).getFilesInDirectory()
            
            for filePath in fold:
                file(filePath).getFileBaseName()
                    
                manager.entries.append(file(filePath).getFileBaseName())

            for entry in displayDump(manager):
                display.addItem(entry["item"])
                display.setItemWidget(entry["item"], entry["widget"])   

            manager.entries = []             

        fileSelector.clicked.connect(fileSelectorClick)
        folderSelector.clicked.connect(folderSelectorClick)


if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("Frosty's Music Player")
    out = main()
    out.show()

    sys.exit(app.exec())