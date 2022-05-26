from errorhandler import AUDIO_ENTRY_NOT_IN_ENTRY_LIST, WRONG_VALUE_TYPE
from files import audioFile, file
from playsound import *
from pyflac import *


def checkAudioType(audiofile, extension) -> None:
    if not file.getFileExtension(audiofile) == extension:
        raise WRONG_VALUE_TYPE


class audioEntryManager(str):
    entries = []
    stored  = []

    def __init__(self, name) -> None:
        self.name   = name

    def addEntry(self, entry) -> None:
        if entry in self.entries:
            return
        self.entries.append(entry)

    def removeEntry(self, entry):
        if not entry in self.entries:
            raise AUDIO_ENTRY_NOT_IN_ENTRY_LIST
        self.entries.remove(entry)

    def store(self, entry):
        self.stored.append(entry)

    def clean(self, entry):
        if not entry in self.stored:
            raise AUDIO_ENTRY_NOT_IN_ENTRY_LIST
        self.entries.remove(entry)


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



