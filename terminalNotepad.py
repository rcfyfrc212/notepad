from res.terminalMenu.frame import Frame
from res.terminalMenu.optionsFrame import OptionsFrame
from res.terminalMenu.frameRouter import FrameRouter, FrameRoute

from res.db.notesDb import NotesDb

from frames import (
    startFrame, addFrame, listFrame,
    noteFrame, searchFrame
)


class TerminalNotepad(FrameRouter):
    """
    This class represents a frame router of terminal notepad
    """

    def __init__(self, db: NotesDb):
        """
        Args:
            db (NotesDb): notes database
        """
        super().__init__()
        self.db = db

    def startRoute(self) -> FrameRoute:
        """
        Returns:
            FrameRoute: start FrameRoute
        """
        return FrameRoute(startFrame, self.startFrameHandler)

    def startFrameHandler(self, frame: OptionsFrame) -> FrameRoute:
        """
        Args:
            frame (OptionsFrame): start frame

        Returns:
            FrameRoute: next route for router
        """
        if frame.optionName == 'add':
            return FrameRoute(addFrame, self.addHandler)

        if frame.optionName == 'list':
            notes = self.db.getNotes()
            return FrameRoute(listFrame(notes), self.listHandler)

        if frame.optionName == 'search':
            return FrameRoute(searchFrame, self.searchHandler)

        if frame.optionName == 'quit':
            print('Bye bye')
            raise SystemExit

    def addHandler(self, frame: Frame) -> FrameRoute:
        """
        Adding a new note

        Args:
            frame (Frame): add frame

        Returns:
            FrameRoute: next route for router
        """
        if self.db.addNote(
            title=frame.output['title'],
            content=frame.output['content']
        ):
            return FrameRoute(
                startFrame,
                self.startFrameHandler,
                'New note added')

        else:
            return FrameRoute(
                startFrame,
                self.startFrameHandler,
                'New note hasn\'t been added')

    def listHandler(self, frame: OptionsFrame) -> FrameRoute:
        """
        Args:
            frame (OptionsFrame): list frame

        Returns:
            FrameRoute: next route for router
        """
        optionName = frame.optionResult.name

        if optionName == 'back':
            return self.startRoute()

        else:
            noteId = int(optionName)
            note = self.db.getNoteById(noteId)

            return FrameRoute(noteFrame(note), self.noteHandler)

    def noteHandler(self, frame: OptionsFrame) -> FrameRoute:
        """
        Args:
            frame (OptionsFrame): note frame

        Returns:
            FrameRoute: next route for router
        """
        if frame.optionName == 'delete':
            noteId = int(frame.name)

            if self.db.deleteNoteById(noteId):
                return FrameRoute(
                    startFrame,
                    self.startFrameHandler,
                    'Note has been deleted')

            else:
                return FrameRoute(
                    startFrame,
                    self.startFrameHandler,
                    'Note hasn\'t been deleted')

        elif frame.optionName == 'back':
            return self.startRoute()

    def searchHandler(self, frame: Frame) -> FrameRoute:
        """
        Args:
            frame (Frame): search frame

        Returns:
            FrameRoute: next route for router
        """
        query = frame.output['query']

        if query == 'back':
            return self.startRoute()

        note = self.db.getNoteByContentMatch(query)

        if note:
            return FrameRoute(noteFrame(note), self.noteHandler)

        else:
            return FrameRoute(
                searchFrame,
                self.searchHandler,
                'No matches found')
