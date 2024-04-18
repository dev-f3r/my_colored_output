"""
    Example:
    >>> print('\033[34mBlue\033[0m text, \033[31mRed\033[0m text, \033[32mGreen\033[0m text')
    Blue text, Red text, Green text
"""

class Colored:
    def __init__(self, s: str) -> None:
        self.__s = s

    def __process(self, s: str) -> str:
        pass