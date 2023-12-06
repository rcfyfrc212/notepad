from res.db.notesDb import NotesDb
from terminalNotepad import TerminalNotepad

if __name__ == '__main__':
    db = NotesDb(dbpath='notes.db')
    notepad = TerminalNotepad(db=db)

    notepad.run()
