from typing import Union, Callable

from .frame import Frame
from .optionsFrame import OptionsFrame


class FrameRoute:
    """
    This class represents routes for FrameRouter
    FrameRoute objects must be returned by FrameRouter handler methods
    """

    def __init__(self, frame: Union[Frame, OptionsFrame],
                 handler: Callable, message: str = ''):
        """
        Args:
            frame (Union[Frame, OptionsFrame]): menu frame
            handler (Callable): frame handler
            message (str, optional): frame message. Defaults to ''.
        """
        self.frame = frame
        self.handler = handler
        self.message = message


class FrameRouter:
    """
    This class is used as the parent class for frame router
    """

    def __init__(self):
        pass

    def startRoute(self) -> FrameRoute:
        """
        Returns:
            FrameRoute: returns start FrameRoute for router
        """
        pass

    def run(self):
        """
        Launches the loop of router
        """
        currentRoute = self.startRoute()

        while True:
            # Cycle shows the current frame, executes its handler
            # and receives the next frame and handler from it
            try:
                currentRoute.frame.show(handlerMessage=currentRoute.message)

                newRoute = currentRoute.handler(currentRoute.frame)

                currentRoute = newRoute

            except SystemExit:
                quit()

            except BaseException:
                currentRoute = self.startRoute()


__all__ = ['FrameRoute', 'FrameRouter']
