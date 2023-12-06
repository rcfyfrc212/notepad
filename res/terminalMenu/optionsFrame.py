from .frame import Frame, Input


class Option:
    """
    This class represents an option for OptionsFrame
    """

    def __init__(self, name: str, description: str):
        """
        Args:
            name (str): option name
            description (str): option description for user
        """
        self.name = name
        self.description = description


class OptionsFrame(Frame):
    """
    This class represents a terminal menu frame
    which ask a user to choose an option
    """

    def __init__(
            self,
            name: str,
            title: str,
            options: list[Option],
            optionInput: Input,
            description: str = ''
    ):
        """
        Args:
            name (str): frame name
            title (str): frame description
            options (list[Option]): options for user
            optionInput (Input): input to ask user option
            description (str, optional): frame description. Defaults to ''.
        """
        super().__init__(name, title, [optionInput], description)
        self.options = options
        self.optionResult: Option = None

    @property
    def optionName(self) -> str:
        """
        Returns:
            str: Returns user option name
        """
        if self.optionResult:
            return self.optionResult.name

    def showFrame(self):
        """
        Shows the frame title, description and options with indexes
        """
        super().showFrame()

        for i in range(len(self.options)):
            option = self.options[i]
            print(f'{i+1} - {option.description}')

        print()

    def showInputs(self):
        """
        Asks user to choose an option number
        """
        while True:
            try:
                inp = self.input(self.inputs[0].question)

                optionIndex = int(inp) - 1
                self.optionResult = self.options[optionIndex]

                break

            except (ValueError, IndexError):
                print(
                    'Input should be a number '
                    f'between ({1}-{len(self.options)})!\n')


__all__ = ['Option', 'OptionsFrame']
