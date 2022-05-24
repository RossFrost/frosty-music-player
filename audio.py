from errorhandler import WRONG_VALUE_TYPE
from files import audioFile, file
from playsound import *
from pyflac import *


def checkAudioType(audiofile, extension) -> None:
    if not file.getFileExtension(audiofile) == extension:
        raise WRONG_VALUE_TYPE(WRONG_VALUE_TYPE.text)


class audioEntryManager:
    def __init__(self, entry) -> None:
        self.entries = [] 
        self.entry = entry

    def addEntry(self):
        self.entries.append(self.entry)

    def removeEntry(self):
        if not self.entry in self.entries:
            raise 
        self.entries.remove(self.entry)


class audioMetaDataManager:
    def __init__(self, audioLength, artist, trackName) -> None:
        self.length = audioLength
        self.artist = artist
        self.trackname = trackName


class flac(audioFile):
    def __init__(self, flacFile: audioFile) -> None:
        super().__init__(flacFile)
        checkAudioType(self, ".flac")

    def playback():
        pass


class wav(audioFile):
    def __init__(self, wavFile: audioFile) -> None:
        super().__init__(wavFile)
        checkAudioType(self, ".wav")

    def playback():
        pass

class ogg(audioFile):
    def __init__(self, oggFile: audioFile) -> None:
        super().__init__(oggFile)
        checkAudioType(self, ".ogg")

    def playback():
        pass


class mp3(audioFile):
    def __init__(self, mp3: file):
        super().__init__(mp3)
        checkAudioType(self, ".mp3")
    
    def playback():
        pass


def retrieveMetaDataFromAudio(audio: audioFile) -> audioMetaDataManager:
    data = {}



