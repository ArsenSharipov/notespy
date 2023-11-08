import Note


def create_note(number):
    title = check_len_text_input(
        input('Title: '), number)
    body = check_len_text_input(
        input('Start typing: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nWhat do You want?:\n\n1 - show all notes\n2 - new note\n3 - delete note\n4 - edit note\n5 - selection of notes by date\n6 - selection of notes by id\n7 - exit\n\nPrint the number of function: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Note cannot be empty\n')
        text = input('Start typing: ')
    else:
        return text