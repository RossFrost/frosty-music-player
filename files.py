import ntpath as path
from os import listdir
from os.path import isdir, splitext
from errorhandler import *


class file(str):
    def __init__(self, filepath: str) -> None:
        self.filepath: str = filepath

        if not path.exists(self.filepath):
            raise FILE_DOES_NOT_EXIST(FILE_DOES_NOT_EXIST.text)

    def getFileExtension(self) -> str:
        return splitext(self.filepath)[-1]


    def getFileBaseName(self) -> str:
        extension = self.getFileExtension()
        base = path.basename(self).replace(extension, '')

        return base

    def getMetaData():
        pass


class folder:
    def __init__(self, folderpath) -> None:
        self.folderpath: str = folderpath

    def getFilesInDirectory(self) -> list:
        directoryPath = self.folderpath
        if not isdir(directoryPath):
            raise FOLDER_DOES_NOT_EXIST(FOLDER_DOES_NOT_EXIST.text)

        directoryFiles = listdir(directoryPath)
        files = []

        files.extend(f"{path.abspath(self.folderpath)}\\{directoryFile}" for directoryFile in directoryFiles)
        return files


class audioFile(file):
    def __init__(self, filepath) -> None:
        super().__init__(filepath)

        extensions = [".mp3", ".wav", ".flac", ".ogg"]
        if not file.getFileExtension(filepath) in extensions:
            raise WRONG_VALUE_TYPE(WRONG_VALUE_TYPE.text)


