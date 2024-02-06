notes = {}

def add_note(notes, title, content):
    notes[title] = content
    
def list_notes(notes):
    if not notes:
        print("There aren't notes to show")
    else:
        for title, content in notes.items():
            print(f'--> {title}:\n{content}\n~~~~~~~~~~~~~~~~~~~~~')
            
def edit_note(notes, title, new_content):
    if title in notes:
        notes[title] = new_content
        print('The note was edited successfully')
    else:
        print('Note not found')

def delete_note(notes, title):
    if title in notes:
        del notes[title]
    else:
        print('Note not found')

print('''
 _____                           _        
(  _  )                         ( )       
| (_) |   __     __    ___     _| |   _ _ 
|  _  | /'_ `\ /'__`\/' _ `\ /'_` | /'_` )
| | | |( (_) |(  ___/| ( ) |( (_| |( (_| |
(_) (_)`\__  |`\____)(_) (_)`\__,_)`\__,_)
       ( )_) |                            
        \___/'                            
''')

while(True):
    print('''
        1. Add note
        2. View notes
        3. Edit note
        4. Delete note
        5. Exit
        '''
    )
    opt = int(input("Enter an option [1 - 5]: "))
    match opt:
        case 1:
            title = input('title: ')
            content = input('content: ')
            add_note(notes, title, content)
        case 2:
            list_notes(notes)
        case 3:
            title = input('title: ')
            new_content = input('new content: ')
            edit_note(notes, title, new_content)
        case 4:
            title = input('title: ')
            delete_note(notes, title)
        case 5:
            print(notes)
            break
        case _:
            print('Invalid option')