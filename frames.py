from res.terminalMenu.frame import Frame, Input
from res.terminalMenu.optionsFrame import OptionsFrame, Option

TITLE = 'Terminal Notepad'

# start frame
startFrame = OptionsFrame(
    name='main',
    title=TITLE,
    description='Type \'exit\' and press ENTER '
                'to return to menu from any point',
    options=[
        Option(name='add', description='add note'),
        Option(name='search', description='search note'),
        Option(name='list', description='list notes'),
        Option(name='quit', description='close the program')
    ],
    optionInput=Input(
        question='Choose an option: '
    )
)

# adding new note frame
addFrame = Frame(
    name='add',
    title=TITLE,
    description='Add a new note\n'
                'Type \'exit\' and press ENTER to return to menu',
    inputs=[
        Input(
            name='title',
            question='Enter a title: '
        ),
        Input(
            name='content',
            question='Enter a content: '
        )
    ]
)


def listFrame(notes: list[dict]) -> OptionsFrame:
    """
    Args:
        notes (list[dict]): notes list

    Returns:
        OptionsFrame: existing notes frame
    """
    return OptionsFrame(
        name='list',
        title=TITLE,
        options=[
            *list(
                map(
                    lambda note: Option(
                        name=note['pk'],
                        description=note['title']),
                    notes)),
            Option(
                name='back',
                description='back to menu')],
        optionInput=Input(
            question='Choose a note number: '))


def noteFrame(note: dict) -> OptionsFrame:
    """
    Args:
        note (dict): note from database

    Returns:
        OptionsFrame: note frame
    """
    return OptionsFrame(
        name=note['pk'],
        title=TITLE,
        description=f'title: {note["title"]}\n'
        f'content: {note["content"]}',
        options=[
            Option(name='delete', description='delete note'),
            Option(name='back', description='back to menu')
        ],
        optionInput=Input(question='Choose an option: ')
    )


# search by content match frame
searchFrame = Frame(
    name='search',
    title=TITLE,
    inputs=[
        Input(
            name='query',
            question='Enter a string to search in '
                     'notes (return to menu - \'back\'): ')])
