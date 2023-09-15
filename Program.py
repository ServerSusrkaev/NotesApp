import Note
import os
notes = []

while True:
    print("ВЫБЕРИТЕ ОПЕРАЦИЮ: \n" "- Добавить заметку           - 1\n" "- Просмотреть список заметок - 2\n" "- Редактировать заметку      - 3\n" "- Удалить заметку            - 4\n" "- Просмотр заметок           - 5\n" "- Заверишть работу           - 6")
    choice = int(input())

    if choice == 1:
        Note.add_note(notes)
    elif choice == 2:
        Note.read_notes()
    elif choice == 3:
        Note.edit_note(notes)
    elif choice == 4:
        Note.delete_note(notes)
    elif choice == 5:
        Note.view_notes(notes)
    elif choice == 6:
        os.system('cls')
        break
    else:
        print("Недопустимый выбор!")
