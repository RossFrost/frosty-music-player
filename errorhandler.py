class WRONG_VALUE_TYPE(Exception):
    """
    Avoid using wrong file types or add in the extension list @ files.py
    Usually specific files types (like audioFile) would raise this issue
    """

    text = "\n Your mom is very displeased... \n Not a valid audio file"

class FILE_DOES_NOT_EXIST(Exception):
    """
    Must pass a valid file
    """

    text = "\n Your mom is very displeased... \n File does not exist"

class FOLDER_DOES_NOT_EXIST(Exception):
    """
    Must pass a valid folder
    """

    text = "\n Your mom is very displeased... \n Folder does not exist"

class AUDIO_ENTRY_NOT_IN_ENTRY_LIST(Exception):
    """
    Check entry method @ audio.py -> audioEntryManager
    """

    text = "\n Your mom is very displeased... \n Entry error"

