from typing import Union

from .db import DB


class NotesDb(DB):
    """
    This class represents methods for operating notes database
    """

    def getNoteById(self, id: int) -> dict:
        """
        Args:
            id (int): note id

        Returns:
            dict: note
        """
        with self.connect() as con:
            return con.execute(
                f'SELECT * FROM notes WHERE pk={id}'
            ).fetchone()

    def getNoteByContentMatch(self, match: str) -> Union[dict, None]:
        """
        Args:
            match (str): string to search in notes contents

        Returns:
            Union[dict,None]: matching note or None
        """
        with self.connect() as con:
            try:
                return con.execute(
                    f'SELECT * FROM notes WHERE INSTR(content,\'{match}\')'
                ).fetchone()

            except BaseException:
                return

    def getNotes(self) -> list:
        """
        Returns:
            list: all notes
        """
        with self.connect() as con:
            return con.execute(
                'SELECT * FROM notes'
            ).fetchall()

    def addNote(self, title: str, content: str) -> bool:
        """
        Adds a note to database

        Args:
            title (str): new note title
            content (str): new note description
        """
        with self.connect() as con:
            con.execute(
                'INSERT INTO notes '
                '(title, content) '
                'VALUES (?,?)',
                (title, content)
            )

            return True

    def deleteNoteById(self, id: int) -> bool:
        """
        Deletes a note from database

        Args:
            id (int): note id
        """
        with self.connect() as con:
            con.execute(f'DELETE FROM notes WHERE pk={id}')

            return True
