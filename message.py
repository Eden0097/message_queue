from abc import ABC, abstractmethod


class Message(ABC):
    """
    A simple abstract message base class.
    """

    def __init__(self):
        pass

    @abstractmethod
    def convert():
        """Convert self.message into whatever format the API call accepts."""
        pass


class APIMessage(Message):
    """
    A simple string message for api.py.
    """

    def __init__(self, message: str):
        self._message = message

    @property
    def message(self):
        return self._message

    def convert(self) -> str:
        """api.py takes in a string."""
        return self.message
