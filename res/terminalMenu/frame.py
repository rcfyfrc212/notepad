import os

from .exceptions import FrameExitException


class Input:
    """
    This class represents an Input for Frame class
    """

    def __init__(self, name: str = '', question: str = ''):
        """
        Args:
            name (str, optional): input name. Defaults to ''.
            question (str, optional): input question for user. Defaults to ''.
        """
        self.name = name
        self.question = question


class Frame:
    """
    This class represents a terminal menu frame
    """

    FRAME_EXIT_KEYWORD = 'exit'

    def __init__(
            self,
            name: str,
            title: str,
            inputs: list[Input],
            description: str = ''
    ):
        """
        Args:
            name (str): frame name
            title (str): frame title
            inputs (list[Input]): inputs to ask user
            description (str, optional): frame description. Defaults to ''.
        """
        self.name = name
        self.title = title
        self.description = description
        self.inputs = inputs

        self.output = dict()

    def showFrame(self):
        """
        Shows the frame title, description
        """
        print(self.title, end='\n\n')

        if self.description:
            print(self.description, end='\n\n')

    def showInputs(self):
        """
        Asks user for inputs specified in self.inputs
        """
        for userInput in self.inputs:
            inp = self.input(userInput.question)

            self.output[userInput.name] = inp

    def show(self, handlerMessage=''):
        """
        Shows the frame in terminal

        Args:
            handlerMessage (str, optional): message for user. Defaults to ''.
        """
        self.__clearTerminal()

        if handlerMessage:
            print(handlerMessage, end='\n\n')

        self.showFrame()
        self.showInputs()

    def __checkInputExit(self, inp: str):
        """
        Checks if user want to return to the start frame

        Args:
            inp (str): user input

        Raises:
            FrameExitException: if user input is FRAME_EXIT_KEYWORD
        """
        if inp == self.FRAME_EXIT_KEYWORD:
            raise FrameExitException()

    def input(self, question: str) -> str:
        """
        Safe input method.
        Checks input for errors such as MemoryError to prevent program crashing

        Args:
            question (str): input question

        Returns:
            str: user input
        """
        while True:
            try:
                inp = input(question)
                break

            except BaseException:
                print('Try again')

        self.__checkInputExit(inp)
        return inp

    @staticmethod
    def __clearTerminal():
        """
        Clears the terminal
        """
        os.system('cls')


__all__ = ['Frame', 'Input']
