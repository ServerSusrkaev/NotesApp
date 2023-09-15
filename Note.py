import json
import uuid
from datetime import datetime


class Note:
    def __init__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date


def add_note(notes):
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    id = str(uuid.uuid4())
    note = Note(id, title, body, date)
    notes.append(note)
    save_notes(notes)


def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump([note.__dict__ for note in notes], file, ensure_ascii=False, indent=4, separators=(',', ': '))


def read_notes():
    with open('notes.json', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip())


def edit_note(notes):
    id = input("Введите индентификатор заметки для редактирования:")
    note = next((note for note in notes if note.id == id), None)
    if note:
        print(f'Редактирование заметки: {note.title}')
        title = input('Введите новый заголовок заметки (оствьте пустым чтобы не менять): ')
        body = input('Введите ноый текст заметки (оствьте пустым чтобы не менять): ')
        date = input('Введите новую дату заметки в формате dd.mm.yyyy hh:mm:ss (оствьте пустым чтобы не менять): ')

        if title:
            note.title = title
        if body:
            note.body = body
        if date:
            note.date = date
    else:
        print('Заметка не найдена!')
    save_notes(notes)


def delete_note(notes):
    id = input('Введите идентификатор для удаления: ')
    note = next((note for note in notes if note.id == id), None)
    if note:
        notes.remove(note)
        save_notes(notes)
    else:
        print('Заметка не найдена!')


def view_notes(notes):
    date_str = input('Введите дату для фильтрации заметок (в формате dd.mm.yyyy): ')
    try:
        filter_date = datetime.strptime(date_str, '%d.%m.%Y').date()
        filtered_notes = [note for note in notes if datetime.strptime(note.date, '%d.%m.%Y' '%H:%M:%S').date() == filter_date.date()]
    except ValueError:
        filtered_notes = notes

    if filtered_notes:
        for note in notes:
            print(f'{note.id} {note.title} {note.date} {note.body}')
    else:
        print('Нет заметок для отображения')
