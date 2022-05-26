class WRONG_VALUE_TYPE(Exception):
    """
    Avoid using wrong file types or add in the extension list @ files.py
    Usually specific files types (like audioFile) would raise this issue
    """

    def __init__(self) -> None:
        text = "\n Your mom is very displeased... \n Not a valid audio file"
        super().__init__(text)


class FILE_DOES_NOT_EXIST(Exception):
    """
    Must pass a valid file
    """

    def __init__(self) -> None:
        text = "\n Your mom is very displeased... \n File does not exist"
        super().__init__(text)

class FOLDER_DOES_NOT_EXIST(Exception):
    """
    Must pass a valid folder
    """

    def __init__(self) -> None:
        text = "\n Your mom is very displeased... \n Entry error"
        super().__init__(text)


class AUDIO_ENTRY_NOT_IN_ENTRY_LIST(Exception):
    """
    Check entry method @ audio.py -> audioEntryManager
    """

    def __init__(self) -> None:
        text = "\n Your mom is very displeased... \n Entry error"
        super().__init__(text)


