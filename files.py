import ntpath as path
from os import listdir, getcwd
from os.path import isdir, splitext
from errorhandler import *


class file(str):
    def __init__(self, filepath: str) -> None:
        self.filepath: str = filepath

        if not path.exists(self.filepath):
            raise FILE_DOES_NOT_EXIST

    def getFileExtension(self) -> str:
        return splitext(self.filepath)[-1]


    def getFileBaseName(self) -> str:
        extension = self.getFileExtension()
        base = path.basename(self).replace(extension, '')

        return base


class folder(str):
    def __init__(self, folderpath) -> None:
        self.folderpath: str = folderpath

    def getFilesInDirectory(self) -> list:
        directoryPath = self.folderpath
        if not isdir(directoryPath):
            raise FOLDER_DOES_NOT_EXIST

        directoryFiles = listdir(directoryPath)
        files = []

        for file in directoryFiles:
            files.append(self.folderpath + '/' + file)
            
        return files


class audioFile(file):
    def __init__(self, filepath) -> None:
        super().__init__(filepath)

        extensions = [".mp3", ".wav", ".flac", ".ogg"]
        if not file.getFileExtension(filepath) in extensions:
            raise WRONG_VALUE_TYPE

    def getMeta():
        pass

